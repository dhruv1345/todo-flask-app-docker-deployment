from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client.todo_db
todos = db.todos

@app.route('/add', methods=['POST'])
def add_task():
    data = request.json
    task_id = todos.insert_one({"task": data["task"]}).inserted_id
    return jsonify({"message": "Task added", "id": str(task_id)})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [{"id": str(task["_id"]), "task": task["task"]} for task in todos.find()]
    return jsonify(task_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


