// frontend/services/api.ts

import axios from 'axios';

// Define the structure for a Task
export interface Task {
    id: number;
    title: string;
    description: string;
    completed: boolean;
}

// Initialize Axios instance
const api = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8001",
});

// 1. fetchTasks: GET /tasks/
export const fetchTasks = async (): Promise<Task[]> => {
    const response = await api.get<Task[]>('/tasks/');
    return response.data;
};

// 2. createTask: POST /tasks/
export const createTask = async (title: string, description: string = ''): Promise<Task> => {
    const response = await api.post<Task>('/tasks/', { title, description });
    return response.data;
};

// 3. updateTask: PUT /tasks/{id}
export const updateTask = async (id: number, taskData: Partial<Task>): Promise<Task> => {
    const response = await api.put<Task>(`/tasks/${id}`, taskData);
    return response.data;
};

// 4. deleteTask: DELETE /tasks/{id}
export const deleteTask = async (id: number): Promise<void> => {
    await api.delete(`/tasks/${id}`);
};

// 5. toggleTask: PUT /tasks/{id} (flips the status)
export const toggleTask = async (id: number, currentStatus: boolean, currentTitle: string): Promise<Task> => {
    // We update the task's completion status by flipping the currentStatus
    const newStatus = !currentStatus;
    const response = await api.put<Task>(`/tasks/${id}`, {
        completed: newStatus,
        title: currentTitle // Assuming we need to send the title as well, based on the backend schema.
    });
    return response.data;
};
