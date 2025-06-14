# Event Management API

A FastAPI-based system for managing events, registrations, and attendance tracking.

## Features

- User Management (Create, Read, Update)
- Event Management with Speakers
- Registration System
- Attendance Tracking

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/JoseAyobami/event-track>
cd event-track
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server:
```bash
uvicorn main:app --reload
```

The API will be available at: http://127.0.0.1:8000

