# Poll App

A simple Django-based polling application.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ in your web browser

## Features

- Create and manage polls
- Vote on polls
- View poll results with animated progress bars
- Responsive design using Bootstrap
