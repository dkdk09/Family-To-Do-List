from flask import Flask, jsonify, request, send_from_directory
import json

app = Flask(__name__)

# Store family members with their tasks
FamilyNames = []

# FUNCTION 1: Add family member (NO MORE input() calls!)
def AddFamilyMember(name):
    """Add a family member to the list"""
    if name not in [m['name'] for m in FamilyNames]:
        # Store as dictionary with name and empty tasks list
        FamilyNames.append({'name': name, 'tasks': []})
        return True
    return False

# FUNCTION 2: Add task for a family member (accepts parameters!)
def AddTaskForFamilyMember(member_name, task_text, urgency='none'):
    """Add a task to a family member"""
    for member in FamilyNames:
        if member['name'].lower() == member_name.lower():
            member['tasks'].append({'text': task_text, 'urgency': urgency})
            return True
    return False

# FLASK ENDPOINTS (connect the web form to your functions)

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
        data = request.get_json()
        member_name = data['member']
        task_index = int(data['taskIndex'])
        
        # Find the member and delete the task
        for member in FamilyNames:
            if member['name'].lower() == member_name.lower():
                if 0 <= task_index < len(member['tasks']):
                    member['tasks'].pop(task_index)
                    return jsonify({'success': True, 'message': 'Task deleted!'})
                else:
                    return jsonify({'success': False, 'message': 'Task not found'}), 404
        
        return jsonify({'success': False, 'message': 'Member not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)