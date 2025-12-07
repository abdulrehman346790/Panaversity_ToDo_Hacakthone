// frontend/app/page.tsx

'use client';

import React, { useEffect, useState, useCallback } from 'react';
import TaskForm from '../components/TaskForm'; // Relative path
import TaskList from '../components/TaskList'; // Relative path
import { fetchTasks, createTask, deleteTask, toggleTask, Task } from '../services/api'; // Relative path

const Home: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const refreshTasks = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchTasks();
      setTasks(data);
    } catch (e) {
      console.error('Failed to fetch tasks:', e);
      setError('Failed to fetch tasks. Ensure the backend API is running at http://127.0.0.1:8001 or configured via NEXT_PUBLIC_API_URL.');
    } finally {
      setLoading(false);
    }
  }, []);

  // Fetch tasks on mount
  useEffect(() => {
    refreshTasks();
  }, [refreshTasks]);

  const handleAddTask = useCallback(async (title: string) => {
    try {
      await createTask(title);
      // Refresh the list to show the new task
      await refreshTasks();
    } catch (e) {
      console.error('Failed to create task:', e);
      setError('Failed to create task.');
    }
  }, [refreshTasks]);

  const handleDelete = useCallback(async (id: number) => {
    try {
      await deleteTask(id);
      // Optimistically update the UI before refreshing (optional, but faster)
      setTasks(currentTasks => currentTasks.filter(task => task.id !== id));
      // Since the API only returns 204 on delete, we rely on the optimistic update.
    } catch (e) {
      console.error('Failed to delete task:', e);
      setError('Failed to delete task.');
    }
  }, []);

  const handleToggle = useCallback(async (id: number, currentStatus: boolean, currentTitle: string) => {
    try {
      await toggleTask(id, currentStatus, currentTitle);
      // Update state locally based on the expected outcome for immediate feedback
      setTasks(currentTasks => currentTasks.map(task =>
        task.id === id ? { ...task, completed: !currentStatus } : task
      ));
    } catch (e) {
      console.error('Failed to toggle task:', e);
      setError('Failed to toggle task.');
    }
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-xl mx-auto space-y-8">
        <h1 className="text-4xl font-extrabold text-center text-gray-800">
          Evolution of Todo - Phase II
        </h1>

        {error && (
          <div className="p-4 text-red-700 bg-red-100 border border-red-300 rounded-lg">
            {error}
          </div>
        )}

        <TaskForm onTaskAdded={handleAddTask} />

        {loading ? (
          <p className="text-center text-gray-500 py-8">Loading tasks...</p>
        ) : (
          <TaskList
            tasks={tasks}
            onDelete={handleDelete}
            onToggle={handleToggle}
          />
        )}
      </div>
    </div>
  );
};

export default Home;
