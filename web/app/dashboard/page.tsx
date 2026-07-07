'use client'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'

interface Agent { id: number; name: string; type: string; description: string }
interface User { id: number; email: string; username: string }

export default function DashboardPage() {
  const [user, setUser] = useState<User | null>(null)
  const [agents, setAgents] = useState<Agent[]>([])
  const [loading, setLoading] = useState(true)
  const router = useRouter()

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (!token) { router.push('/login'); return }
    fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/auth/me`, {
      headers: { Authorization: `Bearer ${token}` }
    }).then(r => r.ok ? r.json() : Promise.reject()).then(setUser).catch(() => { localStorage.clear(); router.push('/login') })
  }, [router])

  useEffect(() => {
    if (!user) return
    const token = localStorage.getItem('token')
    fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/agents/`, {
      headers: { Authorization: `Bearer ${token}` }
    }).then(r => r.json()).then(setAgents).finally(() => setLoading(false))
  }, [user])

  function logout() {
    localStorage.clear()
    router.push('/login')
  }

  if (!user) return null

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="glass border-b sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 gradient-bg rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-sm">N</span>
            </div>
            <span className="font-bold">NeuralFlow</span>
            <span className="text-gray-400 text-sm ml-2">/ Dashboard</span>
          </div>
          <div className="flex items-center gap-4">
            <span className="text-sm text-gray-500">{user.email}</span>
            <button onClick={logout} className="px-4 py-2 text-sm bg-red-50 text-red-600 rounded-lg hover:bg-red-100 transition">Salir</button>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-6 py-8">
        <div className="mb-8">
          <h1 className="text-2xl font-bold">Bienvenido, {user.username} 👋</h1>
          <p className="text-gray-500">Gestiona tus agentes y automatizaciones</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          {[
            { label: 'Agentes', value: agents.length, color: 'bg-neural-500' },
            { label: 'Tareas', value: '0', color: 'bg-green-500' },
            { label: 'Ejecuciones', value: '0', color: 'bg-purple-500' },
            { label: 'Estado', value: 'Online', color: 'bg-emerald-500' },
          ].map((stat, i) => (
            <div key={i} className="bg-white rounded-xl p-4 border border-gray-100">
              <div className="flex items-center gap-3">
                <div className={`w-3 h-3 rounded-full ${stat.color}`}></div>
                <span className="text-gray-500 text-sm">{stat.label}</span>
              </div>
              <p className="text-2xl font-bold mt-2">{stat.value}</p>
            </div>
          ))}
        </div>

        <div className="bg-white rounded-2xl border border-gray-100 p-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-lg font-bold">Mis Agentes</h2>
            <button className="px-4 py-2 gradient-bg text-white rounded-lg text-sm font-medium hover:opacity-90 transition">+ Nuevo Agente</button>
          </div>
          {loading ? (
            <div className="text-center py-12 text-gray-400">Cargando...</div>
          ) : agents.length === 0 ? (
            <div className="text-center py-12">
              <div className="text-4xl mb-4">🤖</div>
              <p className="text-gray-500 mb-4">No tienes agentes aún</p>
              <button className="px-6 py-3 gradient-bg text-white rounded-xl font-medium hover:opacity-90 transition">Crear tu primer agente</button>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {agents.map(agent => (
                <div key={agent.id} className="border border-gray-100 rounded-xl p-4 card-hover">
                  <h3 className="font-bold">{agent.name}</h3>
                  <span className="text-xs bg-neural-100 text-neural-700 px-2 py-1 rounded-full">{agent.type}</span>
                  <p className="text-sm text-gray-500 mt-2">{agent.description || 'Sin descripción'}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  )
}
