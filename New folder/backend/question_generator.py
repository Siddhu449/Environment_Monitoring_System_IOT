import requests
import json
import os

class QuestionGenerator:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
        self.api_url = "https://api.openai.com/v1/chat/completions"
        self.model = "gpt-3.5-turbo"
    
    def generate_questions(self, subject, num_questions=5):
        """Generate subject-specific questions using OpenAI API"""
        
        prompt = f"""Generate {num_questions} multiple choice questions for {subject}. 
        Each question should have:
        - A clear question
        - 4 answer options (A, B, C, D)
        - The correct answer indicated
        - Questions should be beginner to intermediate level
        
        Format the response as a JSON array with this structure:
        [
            {{
                "question": "question text",
                "options": ["option1", "option2", "option3", "option4"],
                "correct": 0,
                "explanation": "brief explanation"
            }}
        ]
        
        Make sure the questions are relevant to {subject} programming concepts."""
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 1000,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            
            content = response.json()['choices'][0]['message']['content']
            
            # Parse the JSON response
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                questions = json.loads(json_match.group())
                return questions
            else:
                # Fallback to manual parsing if JSON format is not clean
                return self._parse_questions_fallback(content)
                
        except Exception as e:
            print(f"Error generating questions: {e}")
            return self._get_fallback_questions(subject)
    
    def _parse_questions_fallback(self, content):
        """Fallback method to parse questions if JSON format fails"""
        # This is a simple fallback that creates basic questions
        # In production, you might want more sophisticated parsing
        return [
            {
                "question": f"What is the basic concept in programming?",
                "options": ["Variables", "Functions", "Loops", "All of the above"],
                "correct": 3,
                "explanation": "All are fundamental programming concepts"
            }
        ]
    
    def _get_fallback_questions(self, subject):
        """Return fallback questions if API fails"""
        fallback_questions = {
            'Python': [
                {
                    "question": "What is the output of print('Hello World')?",
                    "options": ["Hello World", "Error", "None", "hello world"],
                    "correct": 0,
                    "explanation": "The print function displays the string as-is"
                },
                {
                    "question": "Which data type is used for whole numbers in Python?",
                    "options": ["float", "int", "str", "bool"],
                    "correct": 1,
                    "explanation": "int is used for whole numbers"
                }
            ],
            'HTML': [
                {
                    "question": "What does HTML stand for?",
                    "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlink and Text Markup Language"],
                    "correct": 0,
                    "explanation": "HTML stands for Hyper Text Markup Language"
                },
                {
                    "question": "Which tag is used for the largest heading?",
                    "options": ["<heading>", "<h6>", "<h1>", "<head>"],
                    "correct": 2,
                    "explanation": "<h1> is used for the largest heading"
                }
            ],
            'JavaScript': [
                {
                    "question": "Which company developed JavaScript?",
                    "options": ["Microsoft", "Sun Microsystems", "Netscape", "Google"],
                    "correct": 2,
                    "explanation": "JavaScript was developed by Netscape"
                },
                {
                    "question": "What is the correct way to create a function in JavaScript?",
                    "options": ["function = myFunction()", "function myFunction()", "create myFunction()", "def myFunction()"],
                    "correct": 1,
                    "explanation": "function keyword is used to define functions"
                }
            ],
            'SQL': [
                {
                    "question": "What does SQL stand for?",
                    "options": ["Structured Query Language", "Simple Query Language", "Standard Question Language", "Structured Question Language"],
                    "correct": 0,
                    "explanation": "SQL stands for Structured Query Language"
                },
                {
                    "question": "Which SQL statement is used to extract data from a database?",
                    "options": ["GET", "EXTRACT", "SELECT", "OPEN"],
                    "correct": 2,
                    "explanation": "SELECT statement is used to extract data"
                }
            ]
        }
        
        return fallback_questions.get(subject, fallback_questions['Python'])
