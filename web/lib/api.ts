const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export async function apiFetch(path: string, options: RequestInit = {}) {
  const token = typeof window !== 'undefined' ? localStorage.getItem('token') : null
  const headers: any = { 'Content-Type': 'application/json', ...options.headers }
  if (token) headers.Authorization = `Bearer ${token}`
  const res = await fetch(`${API_URL}${path}`, { ...options, headers })
  if (!res.ok) {
    if (res.status === 401 && typeof window !== 'undefined') {
      localStorage.clear()
      window.location.href = '/login'
    }
    const data = await res.json().catch(() => ({}))
    throw new Error(data.detail || 'API Error')
  }
  return res.json()
}

export const auth = {
  login: (username: string, password: string) => apiFetch('/auth/login', { method: 'POST', body: JSON.stringify({ username, password }) }),
  register: (email: string, username: string, password: string) => apiFetch('/auth/register', { method: 'POST', body: JSON.stringify({ email, username, password }) }),
  me: () => apiFetch('/auth/me'),
}

export const agents = {
  list: () => apiFetch('/agents/'),
  create: (data: any) => apiFetch('/agents/', { method: 'POST', body: JSON.stringify(data) }),
  run: (id: number, input: string) => apiFetch(`/agents/${id}/run`, { method: 'POST', body: JSON.stringify({ input }) }),
  types: () => apiFetch('/agents/types'),
}
