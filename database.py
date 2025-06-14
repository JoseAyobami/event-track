from models import User, Event, Speaker, Registration

users: list[User] = []
events: list[Event] = []
speakers: list[Speaker] = [
    Speaker(id=1, name="Ayobami Jose", topic="Machine Learning and the Future"),
    Speaker(id=2, name="Abiola Martins", topic="Cybersecurity Trends"),
    Speaker(id=3, name="Olagoke Prudence", topic="Cloud Computing 101"),
]
registrations: list[Registration] = []