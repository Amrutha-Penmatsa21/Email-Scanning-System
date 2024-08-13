import string

class EmailScanner:
    def __init__(self):
        self.email_content = ""
        
    def input_email(self):
        try:
            self.email_content = input("Please enter the email content: ")
        except Exception as e:
            print("Error while reading email content:", e)
    
    def preprocess_email(self):
        self.email_content = self.email_content.lower()
        self.email_content = self.email_content.translate(str.maketrans('', '', string.punctuation))
        class SuspicionCalculator:
    def __init__(self, keyword_weights):
        self.keyword_weights = keyword_weights
    
    def calculate_suspicion(self, email_content):
        total_weight = 0
        for keyword, weight in self.keyword_weights.items():
            if keyword in email_content:
                total_weight += weight
        
        # Assume the maximum possible weight sum for simpler calculation
        max_possible_weight = sum(self.keyword_weights.values())
        suspicion_percentage = (total_weight / max_possible_weight) * 100 if max_possible_weight != 0 else 0
        return suspicion_percentage

    # Time complexity analysis: O(n * m), where n is the number of keywords, and m is the length of the email content.
    import json

class KeywordWeights:
    def __init__(self):
        self.weights = {}
    
    def load_weights(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.weights = json.load(file)
        except FileNotFoundError as e:
            print("File not found:", e)
    
    def add_weight(self, keyword, weight):
        self.weights[keyword] = weight
    
    def update_weight(self, keyword, weight):
        self.weights[keyword] = weight
    
    def get_weight(self, keyword):
        return self.weights.get(keyword, 0)
class InvalidInputException(Exception):
    pass

class FileNotFoundException(Exception):
    pass
import re

class EmailContentAnalyzer:
    def extract_information(self, email_content):
        sender = re.search(r"From: (.+)", email_content)
        recipient = re.search(r"To: (.+)", email_content)
        subject = re.search(r"Subject: (.+)", email_content)
        
        return {
            'sender': sender.group(1) if sender else None,
            'recipient': recipient.group(1) if recipient else None,
            'subject': subject.group(1) if subject else None
        }
    
    def identify_suspicious_content(self, email_content):
        # Placeholder for advanced pattern matching
        return "Suspicious content identified" in email_content
    class SuspiciousKeywordManager:
    def __init__(self):
        self.keywords = {}
    
    def add_keyword(self, keyword, weight):
        self.keywords[keyword] = weight
    
    def remove_keyword(self, keyword):
        if keyword in self.keywords:
            del self.keywords[keyword]
    
    def search_keyword(self, keyword):
        return keyword in self.keywords
    
    def update_keyword_weights(self, keyword, new_weight):
        if keyword in self.keywords:
            self.keywords[keyword] = new_weight
            from datetime import datetime

class EmailHistoryTracker:
    def __init__(self):
        self.history = []
    
    def add_email_history(self, email, suspicion_level):
        date_scanned = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append((email, suspicion_level, date_scanned))
    
    def get_email_history(self):
        return self.history
    
    def sort_history(self, by='date'):
        if by == 'date':
            self.history.sort(key=lambda x: x[2], reverse=True)
        elif by == 'suspicion':
            self.history.sort(key=lambda x: x[1], reverse=True)
            