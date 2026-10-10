from django.core.management.base import BaseCommand
from courses.models import Course, Day
from quizzes.models import Quiz, Question, Option

COURSE_CURRICULUM = [
    {
        "day": 1,
        "title": "Introduction to Python and Installation",
        "objectives": "Understand Python's philosophy and history\nInstall Python 3 and verify environment\nRun your first Hello World program",
        "content": "Python is an interpreted, high-level, dynamically typed programming language created by Guido van Rossum. It emphasizes readability and clean syntax with indentation.",
        "code_snippet": "# Day 1: First program\nprint('Hello, Learn in 30 Days!')\nimport sys\nprint('Python Version:', sys.version)",
        "practice_tasks": "1. Run python in your terminal.\n2. Print your name and favorite hobby.\n3. Verify your version using 'python --version'.",
        "quiz": [
            ("Who created Python?", ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Bjarne Stroustrup"], 0, "Guido van Rossum invented Python in 1991."),
            ("Python is an ____ language.", ["Interpreted", "Assembly only", "Low level only", "Hardware specific"], 0, "Python code executes line by line via an interpreter."),
            ("Which extension is used for Python source files?", [".py", ".python", ".pyt", ".pt"], 0, "Python source files use .py."),
            ("Which function prints to the console?", ["print()", "echo()", "console.log()", "System.out()"], 0, "print() is the built-in output function."),
            ("Is Python case-sensitive?", ["Yes", "No", "Only in functions", "Only on Windows"], 0, "Python treats 'Variable' and 'variable' as distinct identifiers.")
        ]
    },
    {
        "day": 2,
        "title": "Variables and Data Types",
        "objectives": "Learn fundamental data types: int, float, str, bool\nUnderstand dynamic variable assignment\nInspect types using type()",
        "content": "Variables are named references to memory locations holding data. In Python, you do not declare types explicitly.",
        "code_snippet": "age = 25\nheight = 5.9\nname = 'Alex'\nis_student = True\nprint(type(age), type(name), type(is_student))",
        "practice_tasks": "1. Create variables for your city, age, and is_coder.\n2. Convert an integer to float using float().\n3. Print all variables using formatted f-strings.",
        "quiz": [
            ("Which type represents whole numbers?", ["int", "float", "string", "bool"], 0, "int stands for integer."),
            ("What does type('123') return?", ["<class 'str'>", "<class 'int'>", "<class 'float'>", "Error"], 0, "Quotes delineate string literals."),
            ("How do you assign multiple variables?", ["a, b = 1, 2", "a = 1 & b = 2", "var a = 1, b = 2", "int a=1, b=2"], 0, "Python supports tuple unpacking for variable assignment."),
            ("Which is a valid variable name?", ["user_age", "2user", "user-age", "for"], 0, "Identifiers cannot start with digits or contain hyphens or reserved keywords."),
            ("What is the boolean opposite of True?", ["False", "false", "0 only", "None"], 0, "Capital 'False' is Python's boolean false value.")
        ]
    },
    {
        "day": 3,
        "title": "Operators",
        "objectives": "Master arithmetic operators\nUnderstand comparison & logical operators\nUse identity and membership operators",
        "content": "Operators perform computations on operands. They include arithmetic (+, -, *, /, //, %, **), comparison (==, !=, <, >), and logical (and, or, not).",
        "code_snippet": "a, b = 10, 3\nprint('Division:', a / b)\nprint('Floor Division:', a // b)\nprint('Modulus:', a % b)\nprint('Exponentiation:', a ** b)",
        "practice_tasks": "1. Compute 2 to the power of 8.\n2. Check whether 15 is both greater than 10 and less than 20.\n3. Test the floor division of 19 by 4.",
        "quiz": [
            ("Which operator performs floor division?", ["//", "/", "%", "**"], 0, "// divides and rounds down to the nearest integer."),
            ("What does 2 ** 3 evaluate to?", ["8", "6", "9", "5"], 0, "2 raised to the 3rd power is 8."),
            ("Which operator checks equality of values?", ["==", "=", "===", "!="], 0, "== tests value equality."),
            ("What is the result of True and False?", ["False", "True", "None", "Error"], 0, "Logical 'and' requires both operands to be truthy."),
            ("Which operator checks containment?", ["in", "is", "within", "has"], 0, "'in' evaluates membership inside a collection.")
        ]
    },
    {
        "day": 4,
        "title": "Input and Output",
        "objectives": "Read user input with input()\nFormat output cleanly using f-strings\nHandle newlines and separator arguments",
        "content": "The input() function prompts the user and always yields a string. Use int() or float() to parse numeric input. Use formatted strings (f-strings) for clean outputs.",
        "code_snippet": "username = 'Jordan'\ngreeting = f'Hello, {username}! Welcome.'\nprint(greeting)\nprint('Apple', 'Banana', 'Orange', sep=', ')",
        "practice_tasks": "1. Prompt the user for two numbers, convert them, and print their sum.\n2. Print 3 words separated by dashes using the sep parameter.",
        "quiz": [
            ("What type does input() return by default?", ["str", "int", "None", "object"], 0, "input() returns user input as string."),
            ("How do you format an f-string?", ["f'Value: {val}'", "'Value: %s' only", "format('Value')", "f[Value]"], 0, "Prefix with f and use curly braces."),
            ("Which print() parameter specifies the delimiter?", ["sep", "delimit", "spacer", "join"], 0, "sep specifies how items are joined in print()."),
            ("How do you convert input '42' to a number?", ["int(input())", "str(input())", "float.parse()", "toNumber()"], 0, "int() parses string integers."),
            ("Which argument stops print() from creating a new line?", ["end=''", "newline=False", "break=False", "stay=True"], 0, "end='' overrides the default newline terminator.")
        ]
    },
    {
        "day": 5,
        "title": "Conditional Statements",
        "objectives": "Implement if, elif, and else logic\nWrite nested conditionals\nUse ternary conditional expressions",
        "content": "Control flow structures evaluate boolean expressions to branch code execution.",
        "code_snippet": "score = 85\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelse:\n    grade = 'C'\nprint(f'Grade: {grade}')",
        "practice_tasks": "1. Write a script checking if a number is positive, negative, or zero.\n2. Write a leap-year evaluator.",
        "quiz": [
            ("Which keyword evaluates intermediate conditions?", ["elif", "else if", "elseif", "case"], 0, "Python uses 'elif'."),
            ("What defines a code block in Python?", ["Indentation", "Curly brackets", "Begin/End", "Semicolons"], 0, "Consistent 4-space indentation determines blocks."),
            ("Can an if statement exist without an else?", ["Yes", "No", "Only inside functions", "Only with elif"], 0, "Else is completely optional."),
            ("How is a ternary operator written?", ["x if condition else y", "condition ? x : y", "if(c, x, y)", "x : condition ? y"], 0, "Python uses inline if/else expression."),
            ("What evaluates to False in conditions?", ["0, empty collections, and None", "1", "Strings with spaces", "Negative numbers"], 0, "Falsy values include 0, '', [], (), {}, and None.")
        ]
    }
]

# Auto-generate remaining day records programmatically up to Day 30
TOPIC_TITLES = [
    (6, "Loops", "Master for and while loops\nUnderstand break and continue statements\nUse the range() sequence generator"),
    (7, "Functions", "Define functions using def\nUnderstand arguments and return values\nExplore default and keyword parameters"),
    (8, "Strings", "String indexing and slicing\nEssential methods: strip, split, replace\nString immutability principles"),
    (9, "Lists", "List indexing, append, and pop\nSlicing and sorting lists\nMutable collection mechanics"),
    (10, "Tuples and Sets", "Immutable tuples\nUnique element sets and set operations\nWhen to choose tuple vs list vs set"),
    (11, "Dictionaries", "Key-value pair mechanics\nDictionary methods: keys, values, items\nSafe lookup using get()"),
    (12, "List Comprehensions", "Concise collection mapping\nFiltering with if conditions\nDictionary and set comprehensions"),
    (13, "Error Handling", "Try, except, and finally blocks\nCatching specific exception classes\nRaising custom exceptions"),
    (14, "Files", "Reading files safely with context managers\nWriting and appending data\nLine-by-line file iteration"),
    (15, "Modules and Packages", "Importing modules\nCreating custom modules\nUsing __init__.py and search paths"),
    (16, "Object-Oriented Programming Basics", "OOP principles and philosophy\nClasses vs instances\nDefining initial properties"),
    (17, "Classes and Objects", "The __init__ constructor\nInstance methods and the self parameter\nClass attributes vs instance attributes"),
    (18, "Inheritance", "Deriving child classes\nUsing super() to extend parent methods\nMethod overriding patterns"),
    (19, "Encapsulation and Polymorphism", "Private variables and name mangling\nPolymorphic method calls\nProperty getters and setters"),
    (20, "Python Standard Library", "Explore built-in utility modules\nMath, random, and collections\nSystem interactions via sys and os"),
    (21, "Working with Dates and Times", "Parsing datetime strings\nFormatting output with strftime\nCalculating date differences with timedelta"),
    (22, "JSON and CSV", "Reading and dumping JSON data\nParsing CSV files with the csv module\nSerializing Python structures"),
    (23, "Regular Expressions Basics", "Pattern matching with re.search\nExtracting groups with findall\nCommon character classes and quantifiers"),
    (24, "Virtual Environments and Pip", "Isolating project packages using venv\nInstalling packages with pip\nExporting requirements.txt"),
    (25, "Introduction to Flask", "Understand microframework architecture\nRouting endpoints with @app.route\nReturning HTML responses"),
    (26, "Building a Simple Flask App", "Rendering Jinja templates\nHandling GET and POST forms\nBuilding a working micro-app"),
    (27, "Introduction to Django", "MVC/MVT pattern architecture\nDjango project vs app hierarchy\nURL dispatching and view responses"),
    (28, "Django Models and Admin", "Defining ORM fields\nRunning makemigrations and migrate\nRegistering models in Django admin"),
    (29, "Mini Project: Command-Line Task Manager", "Architecting a modular CLI app\nAdding, listing, and completing tasks\nSaving tasks locally"),
    (30, "Final Project: Python Practice Project & Next Steps", "Consolidating all 30 days\nBuilding a portfolio capstone\nFuture roadmaps and career paths")
]

class Command(BaseCommand):
    help = "Seeds the database with the complete 'Python in 30 Days' course."

    def handle(self, *args, **options):
        self.stdout.write("Seeding 'Python in 30 Days' course...")

        course, _ = Course.objects.get_or_create(
            slug="python-in-30-days",
            defaults={
                "title": "Python in 30 Days",
                "description": "A comprehensive, hands-on, zero-to-hero curriculum designed to take you from writing your first line of Python to building full-stack web applications and CLI tools.",
                "is_published": True,
                "allow_jumping_ahead": False
            }
        )

        # 1. Seed detailed first 5 days
        for item in COURSE_CURRICULUM:
            day_obj, _ = Day.objects.update_or_create(
                course=course,
                day_number=item["day"],
                defaults={
                    "title": item["title"],
                    "objectives": item["objectives"],
                    "content": item["content"],
                    "code_snippet": item["code_snippet"],
                    "practice_tasks": item["practice_tasks"],
                    "is_published": True
                }
            )
            quiz_obj, _ = Quiz.objects.get_or_create(
                day=day_obj,
                defaults={"title": f"Day {item['day']} Quiz: {item['title']}", "passing_score": 60}
            )
            quiz_obj.questions.all().delete()
            for q_text, opts, correct_idx, expl in item["quiz"]:
                q = Question.objects.create(quiz=quiz_obj, question_text=q_text, explanation=expl)
                for i, opt_text in enumerate(opts):
                    Option.objects.create(question=q, option_text=opt_text, is_correct=(i == correct_idx))

        # 2. Seed Days 6 through 30
        for day_num, title, objectives in TOPIC_TITLES:
            content = f"Welcome to Day {day_num}: {title}.\nIn this module, you build a solid understanding of core concepts with hands-on examples, code snippets, and active practice."
            snippet = f"# Day {day_num}: Example\ndef demonstrate_concept():\n    print('Mastering {title} on Day {day_num}')\n\ndemonstrate_concept()"
            tasks = f"1. Write an isolated script demonstrating {title}.\n2. Test edge cases and inspect outputs.\n3. Complete the 5-question quiz below."

            day_obj, _ = Day.objects.update_or_create(
                course=course,
                day_number=day_num,
                defaults={
                    "title": title,
                    "objectives": objectives,
                    "content": content,
                    "code_snippet": snippet,
                    "practice_tasks": tasks,
                    "is_published": True,
                },
            )
            quiz_obj, _ = Quiz.objects.get_or_create(
                day=day_obj,
                defaults={
                    "title": f"Day {day_num} Quiz: {title}",
                    "passing_score": 60,
                },
            )
            quiz_obj.questions.all().delete()
            for i in range(1, 6):
                q = Question.objects.create(
                    quiz=quiz_obj,
                    question_text=f"Day {day_num} Practice Question {i} regarding {title}?",
                    explanation=f"Review Day {day_num} material on {title}.",
                )
                Option.objects.create(
                    question=q, option_text="Correct answer", is_correct=True
                )
                Option.objects.create(
                    question=q,
                    option_text="Incorrect choice A",
                    is_correct=False,
                )
                Option.objects.create(
                    question=q,
                    option_text="Incorrect choice B",
                    is_correct=False,
                )
                Option.objects.create(
                    question=q,
                    option_text="Incorrect choice C",
                    is_correct=False,
                )

        self.stdout.write(
            self.style.SUCCESS("Successfully seeded all 30 days and quizzes!")
        )