def run_quiz():
    print("🧪 Welcome to the Python Quiz Game!\n")
    
    questions = [
        {
            "question": "1. Which of the following is a Python keyword?",
            "options": {
                "a": "repeat",
                "b": "pass",
                "c": "loop",
                "d": "then"
            },
            "answer": "b"
        },
        {
            "question": "2. What is the output of: print(2 ** 3)?",
            "options": {
                "a": "6",
                "b": "8",
                "c": "9",
                "d": "Error"
            },
            "answer": "b"
        },
        {
            "question": "3. Which function is used to get the ASCII value of a character?",
            "options": {
                "a": "ascii()",
                "b": "ord()",
                "c": "chr()",
                "d": "asc()"
            },
            "answer": "b"
        },
        {
            "question": "4. What is the output of: print(type({}))?",
            "options": {
                "a": "<class 'dict'>",
                "b": "<class 'set'>",
                "c": "<class 'list'>",
                "d": "<class 'tuple'>"
            },
            "answer": "a"
        },
        {
            "question": "5. Which method is used to remove whitespace from the beginning and end of a string?",
            "options": {
                "a": "strip()",
                "b": "trim()",
                "c": "remove()",
                "d": "cut()"
            },
            "answer": "a"
        },
        {
            "question": "6. What is the correct way to write a comment in Python?",
            "options": {
                "a": "// comment",
                "b": "<!-- comment -->",
                "c": "# comment",
                "d": "** comment **"
            },
            "answer": "c"
        },
        {
            "question": "7. What is the output of: print(bool(1))?",
            "options": {
                "a": "True",
                "b": "False",
                "c": "1",
                "d": "None"
            },
            "answer": "a"
        },
        {
            "question": "8. Which operator is used for floor division in Python?",
            "options": {
                "a": "/",
                "b": "//",
                "c": "%",
                "d": ""
            },
            "answer": "b"
        },
        {
            "question": "9. Which of the following is NOT a built-in data type in Python?",
            "options": {
                "a": "list",
                "b": "set",
                "c": "array",
                "d": "dict"
            },
            "answer": "c"
        },
        {
            "question": "10. What is the default value of the 'end' parameter in print()?",
            "options": {
                "a": "\\n",
                "b": "space",
                "c": "None",
                "d": "\\t"
            },
            "answer": "a"
        },
        {
            "question": "11. Which built-in function returns the length of an object?",
            "options": {
                "a": "size()",
                "b": "len()",
                "c": "length()",
                "d": "count()"
            },
            "answer": "b"
        },
        {
            "question": "12. What is the output of: print(10 % 3)?",
            "options": {
                "a": "3",
                "b": "1",
                "c": "0.3",
                "d": "0"
            },
            "answer": "b"
        },
        {
            "question": "13. Which keyword is used to exit a loop?",
            "options": {
                "a": "continue",
                "b": "stop",
                "c": "break",
                "d": "exit"
            },
            "answer": "c"
        },
        {
            "question": "14. What is the correct way to define a tuple?",
            "options": {
                "a": "[1, 2, 3]",
                "b": "{1, 2, 3}",
                "c": "(1, 2, 3)",
                "d": "<1, 2, 3>"
            },
            "answer": "c"
        },
        {
            "question": "15. Which statement is used to handle exceptions?",
            "options": {
                "a": "error",
                "b": "try-except",
                "c": "catch",
                "d": "handle"
            },
            "answer": "b"
        },
        {
            "question": "16. Which function converts a string to lowercase?",
            "options": {
                "a": "tolower()",
                "b": "lowercase()",
                "c": "lower()",
                "d": "downcase()"
            },
            "answer": "c"
        },
        {
            "question": "17. What is the output of: print('Hello' * 2)?",
            "options": {
                "a": "HelloHello",
                "b": "Hello Hello",
                "c": "Error",
                "d": "2Hello"
            },
            "answer": "a"
        },
        {
            "question": "18. Which of these is a mutable data type?",
            "options": {
                "a": "tuple",
                "b": "list",
                "c": "str",
                "d": "int"
            },
            "answer": "b"
        },
        {
            "question": "19. Which function is used to read input from the user?",
            "options": {
                "a": "scan()",
                "b": "input()",
                "c": "read()",
                "d": "get()"
            },
            "answer": "b"
        },
        {
            "question": "20. Which keyword is used to create a class in Python?",
            "options": {
                "a": "define",
                "b": "func",
                "c": "class",
                "d": "object"
            },
            "answer": "c"
        }
    ]
    
    score = 0
    
    for q in questions:
        print(q["question"])
        for option, value in q["options"].items():
            print(f"{option}) {value}")
        
        user_answer = input("Your answer (a/b/c/d): ").lower()
        
        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            correct_value = q["options"][q["answer"]]
            print(f"❌ Wrong! The correct answer is '{q['answer']}) {correct_value}'\n")
    
    print(f"🎯 Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Perfect Score! You're a Python pro!")
    elif score >= 15:
        print("🎉 Great job! Keep practicing!")
    else:
        print("📚 Keep learning and try again!")

run_quiz()