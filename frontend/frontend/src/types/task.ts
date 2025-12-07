export interface Task {
    id: number;
    title: string;
    description?: string;
    status: boolean; // true if completed
}

export type TaskCreate = Omit<Task, 'id' | 'status'> & { status?: boolean };
export type TaskUpdate = Partial<TaskCreate>;
