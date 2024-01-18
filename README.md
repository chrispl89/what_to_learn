# Learning Tracker

Learning Tracker is a Django application designed for tracking progress in learning Python and sharing comments about the learning process.


### Learn - Progress Tracking

In the Learn section, you can:

- Add Python topics you want to learn.
- Define the proficiency status for each topic.
- Attach links to GitHub projects if they already exist.

### Comments - Sharing Comments

In the Comments section, you can:

- Write comments related to the learning process.
- Manage comments, which are also visible in the Learn section.

## Installation without using Docker

1. Clone the repository:

    git clone https://github.com/chrispl89/what_to_learn.git

2. Navigate to the project directory:

    cd LearnPython

3. Install dependencies:
    pip install -r requirements.txt

4. Run migrations:

    python manage.py migrate

5. Start the development server:

    python manage.py runserver

6. Open your browser and go to http://127.0.0.1:8000/.


## Installation when using Docker

1. Clone the repository:

    git clone https://github.com/chrispl89/what_to_learn.git

2. Go to the directory:
   
    cd what_to_learn

3. Start Docker container

    docker-compose up

4. Open your browser and go to http://127.0.0.1:8000/.


## Technologies Used:
Django

Django Rest Framework

HTML, CSS

Docker

## Author
Krzysztof Jaroński

