let currentQuestion = 0;
let questions = [];
let correct = 0;
let hintCount = 0;
let userId = 1;
let currentSubject = '';

const API_BASE = 'http://localhost:5000';

// Function to fetch users
async function fetchUsers() {
    try {
        const response = await fetch(`${API_BASE}/users`);
        const users = await response.json();
        if (users.length > 0) {
            userId = users[0].id;
        }
        return users;
    } catch (error) {
        console.error('Error fetching users:', error);
        return [];
    }
}

// Function to generate questions using OpenAI API
async function generateQuestions(subject) {
    try {
        const response = await fetch(`${API_BASE}/generate_questions/${subject}?num=5`);
        const data = await response.json();
        
        if (data.error) {
            console.error('Error generating questions:', data.error);
            // Fallback to sample questions
            return getSampleQuestions(subject);
        }
        
        return data.questions;
    } catch (error) {
        console.error('Error generating questions:', error);
        // Fallback to sample questions
        return getSampleQuestions(subject);
    }
}

// Function to submit score
async function submitScore(scoreData) {
    try {
        const response = await fetch(`${API_BASE}/submit_score`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(scoreData)
        });
        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Error submitting score:', error);
        return { error: 'Failed to submit score' };
    }
}

// Function to get leaderboard
async function getLeaderboard() {
    try {
        const response = await fetch(`${API_BASE}/leaderboard`);
        const leaderboard = await response.json();
        return leaderboard;
    } catch (error) {
        console.error('Error fetching leaderboard:', error);
        return [];
    }
}

// Sample questions as fallback
function getSampleQuestions(subject) {
    const sampleQuestions = {
        'Python': [
            {
                question: "What is the output of print(2 + 3)?",
                options: ["5", "23", "Error", "None"],
                correct: 0,
                explanation: "The + operator adds the numbers"
            },
            {
                question: "Which keyword is used to define a function in Python?",
                options: ["function", "def", "define", "fun"],
                correct: 1,
                explanation: "The 'def' keyword is used to define functions"
            },
            {
                question: "What is the correct way to create a list in Python?",
                options: ["list[]", "[]", "{}", "list()"],
                correct: 1,
                explanation: "Square brackets [] are used to create lists"
            },
            {
                question: "Which method adds an element to the end of a list?",
                options: ["add()", "append()", "push()", "insert()"],
                correct: 1,
                explanation: "The append() method adds elements to the end"
            },
            {
                question: "What does len() function return?",
                options: ["Length of object", "Type of object", "Value of object", "None"],
                correct: 0,
                explanation: "len() returns the length of the object"
            }
        ],
        'HTML': [
            {
                question: "What does HTML stand for?",
                options: ["Hyper Text Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlink and Text Markup Language"],
                correct: 0,
                explanation: "HTML stands for Hyper Text Markup Language"
            },
            {
                question: "Which HTML tag is used for the largest heading?",
                options: ["<heading>", "<h6>", "<h1>", "<head>"],
                correct: 2,
                explanation: "<h1> is used for the largest heading"
            },
            {
                question: "What is the correct HTML element for inserting a line break?",
                options: ["<break>", "<br>", "<lb>", "<newline>"],
                correct: 1,
                explanation: "<br> tag creates a line break"
            },
            {
                question: "Which attribute is used to provide an alternate text for an image?",
                options: ["src", "alt", "title", "text"],
                correct: 1,
                explanation: "The alt attribute provides alternate text"
            },
            {
                question: "What is the correct HTML for creating a hyperlink?",
                options: ["<a href='url'>link</a>", "<link href='url'>link</link>", "<a url='url'>link</a>", "<hyperlink>url</hyperlink>"],
                correct: 0,
                explanation: "The correct format is <a href='url'>link</a>"
            }
        ],
        'JavaScript': [
            {
                question: "Which company developed JavaScript?",
                options: ["Microsoft", "Sun Microsystems", "Netscape", "Google"],
                correct: 2,
                explanation: "JavaScript was developed by Netscape"
            },
            {
                question: "What is the correct way to create a function in JavaScript?",
                options: ["function = myFunction()", "function myFunction()", "create myFunction()", "def myFunction()"],
                correct: 1,
                explanation: "Use 'function' keyword to define functions"
            },
            {
                question: "Which method is used to add an element to the end of an array?",
                options: ["push()", "append()", "add()", "insert()"],
                correct: 0,
                explanation: "push() adds elements to the end of an array"
            },
            {
                question: "What does 'DOM' stand for?",
                options: ["Document Object Model", "Data Object Model", "Display Object Management", "Document Oriented Model"],
                correct: 0,
                explanation: "DOM stands for Document Object Model"
            },
            {
                question: "Which operator is used to check both value and type?",
                options: ["==", "===", "=", "!="],
                correct: 1,
                explanation: "=== checks both value and type"
            }
        ],
        'SQL': [
            {
                question: "What does SQL stand for?",
                options: ["Structured Query Language", "Simple Query Language", "Standard Question Language", "Structured Question Language"],
                correct: 0,
                explanation: "SQL stands for Structured Query Language"
            },
            {
                question: "Which SQL statement is used to extract data from a database?",
                options: ["GET", "EXTRACT", "SELECT", "OPEN"],
                correct: 2,
                explanation: "SELECT statement is used to extract data"
            },
            {
                question: "Which SQL clause is used to filter records?",
                options: ["FILTER", "WHERE", "SORT", "EXTRACT"],
                correct: 1,
                explanation: "WHERE clause filters records"
            },
            {
                question: "What is the correct SQL syntax to select all records from a table?",
                options: ["SELECT * FROM table_name", "SELECT all FROM table_name", "SELECT table_name", "GET * FROM table_name"],
                correct: 0,
                explanation: "SELECT * FROM table_name selects all records"
            },
            {
                question: "Which SQL statement is used to insert new records?",
                options: ["ADD", "INSERT INTO", "NEW", "CREATE"],
                correct: 1,
                explanation: "INSERT INTO is used to insert new records"
            }
        ]
    };
    
    return sampleQuestions[subject] || sampleQuestions['Python'];
}

// Start quiz with generated questions
async function startQuiz() {
    currentSubject = document.getElementById("subjectSelect").value;
    
    // Show loading message
    document.getElementById("quizContainer").innerHTML = `
        <div class="loading">
            <h3>Generating questions for ${currentSubject}...</h3>
            <p>Please wait while we create your quiz.</p>
        </div>
    `;
    
    // Generate questions
    questions = await generateQuestions(currentSubject);
    
    if (questions.length === 0) {
        document.getElementById("quizContainer").innerHTML = `
            <div class="error">
                <h3>No questions available</h3>
                <p>Unable to generate questions for ${currentSubject}. Please try again.</p>
            </div>
        `;
        return;
    }
    
    currentQuestion = 0;
    correct = 0;
    hintCount = 0;
    
    displayQuestion();
}

// Display current question
function displayQuestion() {
    if (currentQuestion >= questions.length) {
        endQuiz();
        return;
    }
    
    const question = questions[currentQuestion];
    const quizContainer = document.getElementById("quizContainer");
    
    let html = `
        <div class="quiz-container">
            <div class="question-header">
                <h3>Question ${currentQuestion + 1} of ${questions.length}</h3>
                <p class="subject">Subject: ${currentSubject}</p>
            </div>
            <div class="question">
                <p>${question.question}</p>
            </div>
            <div class="options">
    `;
    
    question.options.forEach((option, index) => {
        html += `
            <label class="option">
                <input type="radio" name="answer" value="${index}">
                <span>${option}</span>
            </label>
        `;
    });
    
    html += `
            </div>
            <div class="quiz-controls">
                <button onclick="submitAnswer()" class="submit-btn">Submit Answer</button>
                <button onclick="showHint()" class="hint-btn">Show Hint</button>
            </div>
            <div class="progress">
                <div class="progress-bar" style="width: ${((currentQuestion + 1) / questions.length) * 100}%"></div>
            </div>
        </div>
    `;
    
    quizContainer.innerHTML = html;
}

// Submit answer
function submitAnswer() {
    const selectedAnswer = document.querySelector('input[name="answer"]:checked');
    
    if (!selectedAnswer) {
        alert("Please select an answer!");
        return;
    }
    
    const answerIndex = parseInt(selectedAnswer.value);
    const question = questions[currentQuestion];
    
    if (answerIndex === question.correct) {
        correct++;
        alert("Correct! 🎉");
    } else {
        alert(`Incorrect. The correct answer is: ${question.options[question.correct]}`);
    }
    
    currentQuestion++;
    displayQuestion();
}

// Show hint
function showHint() {
    hintCount++;
    const question = questions[currentQuestion];
    alert(`Hint: ${question.explanation || "Think carefully about the options!"}`);
}

// End quiz
async function endQuiz() {
    const score = correct;
    const total = questions.length;
    
    // Submit score to backend
    const result = await submitScore({
        user_id: userId,
        subject: currentSubject,
        score: score,
        hint_count: hintCount
    });
    
    const quizContainer = document.getElementById("quizContainer");
    
    let html = `
        <div class="quiz-complete">
            <h3>Quiz Complete! 🎉</h3>
            <div class="score-summary">
                <p><strong>Subject:</strong> ${currentSubject}</p>
                <p><strong>Score:</strong> ${score}/${total}</p>
                <p><strong>Hints Used:</strong> ${hintCount}</p>
                <p><strong>Percentage:</strong> ${Math.round((score/total) * 100)}%</p>
            </div>
            <div class="quiz-actions">
                <button onclick="showLeaderboard()" class="leaderboard-btn">View Leaderboard</button>
                <button onclick="startQuiz()" class="restart-btn">Try Again</button>
            </div>
        </div>
    `;
    
    quizContainer.innerHTML = html;
}

// Show leaderboard
async function showLeaderboard() {
    const leaderboard = await getLeaderboard();
    
    if (leaderboard.length === 0) {
        alert("No leaderboard data available");
        return;
    }
    
    let html = `
        <div class="leaderboard">
            <h3>🏆 Leaderboard</h3>
            <table>
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>Username</th>
                        <th>Subject</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
    `;
    
    leaderboard.forEach((entry, index) => {
        html += `
            <tr>
                <td>${index + 1}</td>
                <td>${entry.username}</td>
                <td>${entry.subject}</td>
                <td>${entry.score}</td>
            </tr>
        `;
    });
    
    html += `
                </tbody>
            </table>
            <button onclick="closeLeaderboard()" class="close-btn">Close</button>
        </div>
    `;
    
    document.getElementById("quizContainer").innerHTML = html;
}

// Close leaderboard
function closeLeaderboard() {
    document.getElementById("quizContainer").innerHTML = '';
}

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    fetchUsers();
});
