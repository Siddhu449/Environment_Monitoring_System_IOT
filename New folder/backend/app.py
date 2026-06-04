from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from question_generator import QuestionGenerator

app = Flask(__name__)
CORS(app)

# Use SQLite database
DB_PATH = os.path.join(os.path.dirname(__file__), 'ai_quiz.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return jsonify({"message": "AI Quiz API is running!"})

@app.route("/submit_score", methods=["POST"])
def submit_score():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO scores (user_id, subject, score, hint_count) VALUES (?, ?, ?, ?)",
        (data["user_id"], data["subject"], data["score"], data["hint_count"])
    )
    
    conn.commit()
    conn.close()
    return jsonify({"message": "Score saved successfully!"})

@app.route("/leaderboard", methods=["GET"])
def leaderboard():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT users.username, scores.subject, scores.score 
        FROM scores 
        JOIN users ON scores.user_id = users.id 
        ORDER BY score DESC 
        LIMIT 5
    """)
    
    results = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in results])

@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, username FROM users")
    results = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in results])

@app.route("/generate_questions/<subject>", methods=["GET"])
def generate_questions(subject):
    """Generate questions for a specific subject using OpenAI API"""
    try:
        generator = QuestionGenerator()
        num_questions = request.args.get('num', 5, type=int)
        
        questions = generator.generate_questions(subject, num_questions)
        
        return jsonify({
            "subject": subject,
            "questions": questions,
            "count": len(questions)
        })
    except Exception as e:
        return jsonify({
            "error": str(e),
            "subject": subject,
            "questions": []
        }), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
