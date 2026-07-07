interface AgentCardProps {
  name: string
  type: string
  description: string
  onRun?: () => void
}

export default function AgentCard({ name, type, description, onRun }: AgentCardProps) {
  const icons: Record<string, string> = {
    chat: '🤖',
    web_scraper: '🕸️',
    content_generator: '✍️',
    data_analyzer: '📊',
  }
  return (
    <div className="bg-white rounded-xl border border-gray-100 p-5 card-hover">
      <div className="flex items-start justify-between mb-3">
        <div>
          <div className="text-2xl mb-2">{icons[type] || '🤖'}</div>
          <h3 className="font-bold">{name}</h3>
        </div>
        <span className="text-xs bg-neural-100 text-neural-700 px-2 py-1 rounded-full">{type}</span>
      </div>
      <p className="text-sm text-gray-500 mb-4">{description || 'Sin descripción'}</p>
      {onRun && (
        <button onClick={onRun} className="w-full py-2 gradient-bg text-white rounded-lg text-sm font-medium hover:opacity-90 transition">
          Ejecutar
        </button>
      )}
    </div>
  )
}
