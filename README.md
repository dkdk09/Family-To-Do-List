# Family To-Do List

Hi guys, this is a quick project I made. It is a web app to manage family tasks with priority levels. I built this thing with Flask. 

## Features

**Add Family Members** - Create a list of your family members
**Assign Tasks** - Give tasks to specific family members
**Priority Levels** - Mark tasks as Not Urgent, Mildly Urgent, or Extremely Urgent (color-coded)
**Delete Tasks** - Remove completed tasks with one click
**Real-time Updates** - See changes instantly on the web interface

## How to Install
- So you need Python 3.6 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository:**
```bash
git clone https://github.com/dkdk09/Family-To-Do-List.git
cd Family-To-Do-List
```

2. **Create a virtual environment (recommended but completely optional):**
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On Mac/Linux
```

3. **Install Flask:**
```bash
pip install flask
```

## How to Run

```bash
python todo.py
```

Then open your browser and go to:
```
http://localhost:5000
```

And yeah that is all. It should be working. 

## How to Use

### Adding a Family Member
1. Type a name in the **"Add Family Member"** box
2. Click **"Add Member"**
3. The member appears on the page!!! WOOHOOO.. thats kinda it

### Adding a Task
1. Enter the task and like write about the task
2. Choose the family member it is for
3. After that choose the urgency level:
   - **Not Urgent**
   - **Mildly Urgent**
   - **Extremely Urgent**
4. Yeah then click  **"Add Task"**

### Completing/Deleting Tasks
- If you(or someone else) finished the task, click the **✓** button 
- Click the **✕** button if you wanna delete the task

## Project Structure

```
Family-To-Do-List/
├── todo.py          # Flask backend (Python)
├── index.html       # Frontend (HTML, CSS, and JavaScript)
└── README.md        # This file
```

## Technologies that I used

- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, Vanilla JavaScript

## Learning Notes

Basically I built this project while learning how to use Python dictionaries and JSON. So yeah I was just getting more experience with like web app fundamentals (Frontend ↔ Backend communication), flask routing and HTTP requests, HTML forms and JavaScript fetch API, and Error handling with try/except


## License

Free to use and modify! DO NOT TAKE CREDIT. I will be very upset. Please do not upset me. 
