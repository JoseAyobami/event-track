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
git clone <repository-url>
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

## API Endpoints

### Users
- `POST /users/` - Create new user
- `GET /users/{user_id}` - Get user by ID
- `PATCH /users/{user_id}` - Update user
- `POST /users/{user_id}/deactivate` - Deactivate user

### Events
- `POST /events/` - Create new event
- `GET /events/{event_id}` - Get event by ID
- `GET /events/` - Get all events
- `POST /events/{event_id}/close` - Close event registration

### Registrations
- `POST /registrations/` - Register user for event
- `GET /registrations/` - Get all registrations
- `GET /registrations/user/{user_id}` - Get user's registrations
- `POST /registrations/{event_id}/attendance` - Mark attendance

## Data Models

### User
- id: Unique identifier
- name: Full name
- email: Email address
- is_active: Boolean (default: True)

### Event
- id: Unique identifier
- title: Event name
- location: Event location
- date: Event date
- is_open: Boolean (default: True)
- speaker_id: ID of assigned speaker

### Speaker
- id: Unique identifier
- name: Speaker name
- topic: Presentation topic

### Registration
- id: Unique identifier
- user_id: ID of registering user
- event_id: ID of event
- registration_date: Date of registration
- attended: Boolean (default: False)

## Business Rules
- Only active users can register for events
- Users cannot register more than once for the same event
- Events must be open for registration
- Speakers must exist when creating an event
