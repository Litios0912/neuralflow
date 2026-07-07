'use client'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'

export default function AgentsPage() {
  const [agentTypes, setAgentTypes] = useState<any[]>([])
  const [selectedAgent, setSelectedAgent] = useState<string>('chat')
  const [input, setInput] = useState('')
  const [output, setOutput] = useState('')
  const router = useRouter()

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (!token) { router.push('/login'); return }
    fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/agents/types`, {
      headers: { Authorization: `Bearer ${token}` }
    }).then(r => r.json()).then(d => setAgentTypes(d.agent_types || [])).catch(() => {})
  }, [router])

  async function runAgent() {
    if (!input) return
    setOutput('Procesando...')
    try {
      const token = localStorage.getItem('token')
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/agents/1/run`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({ input }),
      })
      const data = await res.json()
      setOutput(data.output || 'Error ejecutando agente')
    } catch {
      setOutput('Error de conexión')
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-2xl font-bold mb-6">🧪 Probar Agentes</h1>
        <div className="bg-white rounded-2xl border p-6">
          <div className="mb-4">
            <label className="block text-sm font-medium mb-2">Tipo de Agente</label>
            <select value={selectedAgent} onChange={e => setSelectedAgent(e.target.value)} className="w-full px-4 py-2 border rounded-xl">
              <option value="chat">Chat IA</option>
              <option value="web_scraper">Web Scraper</option>
              <option value="content_generator">Content Generator</option>
              <option value="data_analyzer">Data Analyzer</option>
            </select>
          </div>
          <div className="mb-4">
            <label className="block text-sm font-medium mb-2">Input</label>
            <textarea value={input} onChange={e => setInput(e.target.value)} rows={4} className="w-full px-4 py-3 border rounded-xl focus:ring-2 focus:ring-neural-500" placeholder="Escribe tu consulta aquí..." />
          </div>
          <button onClick={runAgent} className="px-6 py-3 gradient-bg text-white rounded-xl font-medium hover:opacity-90 transition">Ejecutar</button>
          {output && (
            <div className="mt-6">
              <label className="block text-sm font-medium mb-2">Output</label>
              <pre className="bg-gray-50 rounded-xl p-4 whitespace-pre-wrap text-sm">{output}</pre>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
