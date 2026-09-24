let tasks = JSON.parse(localStorage.getItem("tasks")) || [];


// ========================================
// ADD TASK
// ========================================

function addTask() {

    const input = document.getElementById("taskInput");

    const taskText = input.value.trim();

    if (taskText === "") {

        alert("Please enter a task!");

        return;
    }

    const task = {

        id: Date.now(),

        text: taskText,

        completed: false

    };

    tasks.push(task);

    saveTasks();

    input.value = "";

    displayTasks();
}


// ========================================
// DISPLAY TASKS
// ========================================

function displayTasks(taskArray = tasks) {

    const taskList = document.getElementById("taskList");

    taskList.innerHTML = "";

    taskArray.forEach(function(task) {

        const li = document.createElement("li");

        li.className = "task";

        li.innerHTML = `

            <span
                class="task-text ${task.completed ? "completed" : ""}"
            >
                ${task.text}
            </span>

            <div class="task-buttons">

                <button
                    class="complete-btn"
                    onclick="completeTask(${task.id})"
                >
                    ✓
                </button>

                <button
                    class="edit-btn"
                    onclick="editTask(${task.id})"
                >
                    ✏️
                </button>

                <button
                    class="delete-btn"
                    onclick="deleteTask(${task.id})"
                >
                    🗑️
                </button>

            </div>
        `;

        taskList.appendChild(li);

    });

    updateCounter();
}


// ========================================
// COMPLETE TASK
// ========================================

function completeTask(id) {

    const task = tasks.find(function(task) {

        return task.id === id;

    });

    if (task) {

        task.completed = !task.completed;

    }

    saveTasks();

    displayTasks();
}


// ========================================
// DELETE TASK
// ========================================

function deleteTask(id) {

    tasks = tasks.filter(function(task) {

        return task.id !== id;

    });

    saveTasks();

    displayTasks();
}


// ========================================
// EDIT TASK
// ========================================

function editTask(id) {

    const task = tasks.find(function(task) {

        return task.id === id;

    });

    if (!task) {
        return;
    }

    const newText = prompt(
        "Update your task:",
        task.text
    );

    if (newText !== null && newText.trim() !== "") {

        task.text = newText.trim();

        saveTasks();

        displayTasks();
    }
}


// ========================================
// SAVE TASKS
// ========================================

function saveTasks() {

    localStorage.setItem(
        "tasks",
        JSON.stringify(tasks)
    );
}


// ========================================
// SEARCH TASKS
// ========================================

function searchTasks() {

    const searchText =
        document.getElementById("searchInput")
        .value
        .toLowerCase();

    const filteredTasks = tasks.filter(function(task) {

        return task.text
            .toLowerCase()
            .includes(searchText);

    });

    displayTasks(filteredTasks);
}


// ========================================
// UPDATE COUNTER
// ========================================

function updateCounter() {

    document.getElementById("totalTasks")
        .textContent = tasks.length;

    const completed =
        tasks.filter(function(task) {

            return task.completed;

        }).length;

    document.getElementById("completedTasks")
        .textContent = completed;
}


// ========================================
// LOAD TASKS WHEN PAGE OPENS
// ========================================

displayTasks();