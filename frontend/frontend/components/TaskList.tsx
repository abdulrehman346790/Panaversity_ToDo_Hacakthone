// frontend/components/TaskList.tsx

import React from 'react';
import { Task } from '../services/api'; // Use relative path as constrained

interface TaskListProps {
  tasks: Task[];
  onDelete: (id: number) => void;
  onToggle: (id: number, currentStatus: boolean, currentTitle: string) => void;
}

const TaskList: React.FC<TaskListProps> = ({ tasks, onDelete, onToggle }) => {
  if (tasks.length === 0) {
    return (
      <p className="text-center text-gray-500 py-8">
        No tasks yet! Add one above.
      </p>
    );
  }

  return (
    <div className="space-y-3 p-4 bg-white rounded-lg shadow-md">
      {tasks.map((task) => (
        <div
          key={task.id}
          className={`flex items-center justify-between p-3 border rounded-lg transition-all ${
            task.completed ? 'bg-green-50 border-green-200' : 'bg-gray-50 border-gray-200'
          }`}
        >
          <div className="flex items-center flex-grow min-w-0">
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => onToggle(task.id, task.completed, task.title)}
              className="w-5 h-5 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 mr-4 flex-shrink-0"
            />
            <span
              className={`text-gray-900 truncate ${task.completed ? 'line-through text-gray-500' : ''}`}
              title={task.title}
            >
              {task.title}
            </span>
          </div>
          <button
            onClick={() => onDelete(task.id)}
            className="ml-4 p-1 text-red-500 hover:text-red-700 transition duration-150 ease-in-out flex-shrink-0"
            aria-label={`Delete task: ${task.title}`}
          >
            🗑️
          </button>
        </div>
      ))}
    </div>
  );
};

export default TaskList;
