// frontend/components/TaskForm.tsx

'use client';

import React, { useState } from 'react';

interface TaskFormProps {
  onTaskAdded: (title: string) => void;
}

const TaskForm: React.FC<TaskFormProps> = ({ onTaskAdded }) => {
  const [title, setTitle] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (title.trim()) {
      onTaskAdded(title.trim());
      setTitle('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-4 p-4 bg-white rounded-lg shadow-md">
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="What needs to be done?"
        className="flex-grow p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
      <button
        type="submit"
        className="px-4 py-2 text-white bg-blue-600 rounded-lg hover:bg-blue-700 transition duration-150 ease-in-out disabled:bg-blue-300"
        disabled={!title.trim()}
      >
        Add
      </button>
    </form>
  );
};

export default TaskForm;
