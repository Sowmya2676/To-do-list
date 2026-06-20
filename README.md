✨ To-Do List Web Application

A simple and user-friendly To-Do List Web Application built using Python, Flask, HTML, CSS, and JSON.

This application helps users manage daily tasks efficiently by allowing them to add tasks, set deadlines, update tasks, mark tasks as completed, and delete tasks.

🚀 Features
➕ Add new tasks
📅 Set deadlines for tasks
✏️ Update task details and deadlines
✅ Mark tasks as completed
🗑️ Delete tasks
📋 View all tasks
📊 Dashboard with:
Total tasks
Completed tasks
Pending tasks
⏰ Next due task notification
💾 Persistent storage using JSON


🛠️ Technologies Used
Backend: Python, Flask
Frontend: HTML5, CSS3
Data Storage: JSON
Template Engine: Jinja2


📂 Project Structure
to-do-list/
│
├── app.py
├── tasks.json
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

    
⚙️ Installation and Setup
1. Clone the Repository
git clone <repository-url>
Or download the ZIP file and extract it.

2. Navigate to the Project Folder
cd to-do-list

3. Install Dependencies
pip install flask

4. Create tasks.json
Create a file named tasks.json in the project root directory and add:
[]

5. Run the Application
python app.py

6. Open the Browser
Visit:
http://127.0.0.1:5000

📸 Application Workflow
Enter a task name.
Select a deadline.
Click Add Task.
View all tasks in the dashboard.
Update task details if needed.
Mark tasks as completed.
Delete tasks that are no longer needed.
Monitor upcoming deadlines using the Next Due Task section.

🧠 How It Works
User actions from the frontend are sent to Flask routes.

Flask processes the request and updates the task data.

Tasks are stored in tasks.json.

Updated data is rendered back to the webpage.

HTML Form → Flask Route → tasks.json → Flask Route → HTML Page
📋 Task Data Format

Each task is stored in the following format:

{
    "name": "Complete project documentation",
    "deadline": "2026-06-20T18:00",
    "completed": false
}
🔮 Future Enhancements
🌙 Dark mode
🔍 Search tasks
🏷️ Priority levels (High, Medium, Low)
📌 Filter tasks (All / Completed / Pending)
🗄️ SQLite database integration
👤 User authentication
📱 Responsive mobile design
🔔 Email or browser notifications
🎯 Learning Outcomes

Through this project, you will learn:

Flask fundamentals
Routing in Flask
Handling forms using POST requests
CRUD operations
Template rendering with Jinja2
Frontend and backend integration
Working with JSON files
Basic web application architecture
👩‍💻 Author

Sowmya M

Machine Learning Enthusiast | Python Learner | Aspiring AI Engineer

📜 License

This project is created for educational purposes and is free to use and modify.
