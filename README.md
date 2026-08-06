# 👨‍👩‍👧‍👦 Family To-Do List

A simple, retro-styled web app to manage family tasks with priority levels. Built with Flask and designed to look like old-school paperwork.

## Features

**Add Family Members** - Create a list of your family members
**Assign Tasks** - Give tasks to specific family members
**Priority Levels** - Mark tasks as Not Urgent, Mildly Urgent, or Extremely Urgent (color-coded)
**Delete Tasks** - Remove completed tasks with one click
**Real-time Updates** - See changes instantly on the web interface

## How to Install

### Prerequisites
- Python 3.6 or higher
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

That's it! Your app is running. 🎉

## How to Use

### Adding a Family Member
1. Type a name in the **"Add Family Member"** box
2. Click **"Add Member"**
3. The member appears on the page!!! WOOHOOO

### Adding a Task
1. Enter the task description
2. Select which family member it's for
3. Choose the urgency level:
   - **Not Urgent**
   - **Mildly Urgent**
   - **Extremely Urgent**
4. Then click **"Add Task"**

### Completing/Deleting Tasks
- Click the **✓** button to mark as complete (removes the task)
- Click the **✕** button to delete the task

## Project Structure

```
Family-To-Do-List/
├── todo.py          # Flask backend (Python)
├── index.html       # Frontend (HTML/CSS/JavaScript)
└── README.md        # This file
```

## Technologies Used

- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Styling:** Courier New font, retro aesthetic

## Learning Notes

I built this project to learn:
- Web app fundamentals (Frontend ↔ Backend communication)
- Python dictionaries and JSON
- Flask routing and HTTP requests
- HTML forms and JavaScript fetch API
- Error handling with try/except

## Future Features (Maybe!)

- Save the data to a file so tasks persist after closing
- Add due dates to tasks
- Edit existing tasks
- Mobile app version
- Customizable themes

## Author

Created as a learning project for web development with Python and JSON.

## License

Free to use and modify!
