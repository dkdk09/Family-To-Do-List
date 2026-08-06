from flask import Flask, jsonify, request, send_from_directory
import json
import os

app = Flask(__name__)

# File where we save the data
DATA_FILE = 'data.json'

# Load data from file on startup
def load_data():
    """Load family members and tasks from the JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

# Save data to file
def save_data(data):
    """Save family members and tasks to the JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Load data when app starts
FamilyNames = load_data()

# FUNCTION 1: Add family member
def AddFamilyMember(name):
    """Add a family member to the list"""
    global FamilyNames
    if name not in [m['name'] for m in FamilyNames]:
        FamilyNames.append({'name': name, 'tasks': []})
        save_data(FamilyNames)  # Save to file
        return True
    return False

# FUNCTION 2: Add task for a family member
def AddTaskForFamilyMember(member_name, task_text, urgency='none'):
    """Add a task to a family member"""
    global FamilyNames
    for member in FamilyNames:
        if member['name'].lower() == member_name.lower():
            member['tasks'].append({'text': task_text, 'urgency': urgency})
            save_data(FamilyNames)  # Save to file
            return True
    return False

# FLASK ENDPOINTS

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/add_member', methods=['POST'])
def add_member():
    try:
        data = request.get_json()
        name = data['name'].strip()
        
        if AddFamilyMember(name):
            return jsonify({'success': True, 'message': 'Member added!'})
        else:
            return jsonify({'success': False, 'message': 'Member already exists'}), 400
    except KeyError:
        return jsonify({'success': False, 'message': 'Name is required'}), 400

@app.route('/add_task', methods=['POST'])
def add_task():
    try:
        data = request.get_json()
        member_name = data['member']
        task_text = data['task']
        urgency = data.get('urgency', 'none')
        
        if AddTaskForFamilyMember(member_name, task_text, urgency):
            return jsonify({'success': True, 'message': 'Task added!'})
        else:
            return jsonify({'success': False, 'message': 'Member not found'}), 404
    except KeyError:
        return jsonify({'success': False, 'message': 'Member and task required'}), 400

@app.route('/get_members', methods=['GET'])
def get_members():
    return jsonify(FamilyNames)

@app.route('/delete_task', methods=['POST'])
def delete_task():
    try:
        global FamilyNames
        data = request.get_json()
        member_name = data['member']
        task_index = int(data['taskIndex'])
        
        for member in FamilyNames:
            if member['name'].lower() == member_name.lower():
                if 0 <= task_index < len(member['tasks']):
                    member['tasks'].pop(task_index)
                    save_data(FamilyNames)  # Save to file
                    return jsonify({'success': True, 'message': 'Task deleted!'})
                else:
                    return jsonify({'success': False, 'message': 'Task not found'}), 404
        
        return jsonify({'success': False, 'message': 'Member not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)