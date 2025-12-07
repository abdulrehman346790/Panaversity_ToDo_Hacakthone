import axios from 'axios';
import { Task, TaskCreate, TaskUpdate } from '@/types/task';

const BASE_URL = 'http://127.0.0.1:8001';

const api = axios.create({
    baseURL: BASE_URL,
});

export const getTasks = async (): Promise<Task[]> => {
    const response = await api.get<Task[]>('/tasks/');
    return response.data;
};

export const createTask = async (data: TaskCreate): Promise<Task> => {
    const response = await api.post<Task>('/tasks/', data);
    return response.data;
};

export const updateTask = async (id: number, data: TaskUpdate): Promise<Task> => {
    const response = await api.put<Task>(`/tasks/${id}`, data);
    return response.data;
};

export const deleteTask = async (id: number): Promise<boolean> => {
    await api.delete(`/tasks/${id}`);
    return true; // API returns 204 No Content on success
};

export const toggleTask = async (id: number, status: boolean): Promise<Task> => {
    return updateTask(id, { status: status });
};

