import Link from 'next/link'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 via-white to-neural-50">
      <header className="glass border-b border-gray-100 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 gradient-bg rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-sm">N</span>
            </div>
            <span className="font-bold text-xl">NeuralFlow</span>
          </div>
          <div className="flex items-center gap-4">
            <Link href="/login" className="px-4 py-2 text-gray-600 hover:text-gray-900 font-medium">Iniciar Sesión</Link>
            <Link href="/login" className="px-6 py-2 gradient-bg text-white rounded-xl font-medium hover:opacity-90 transition">Comenzar</Link>
          </div>
        </div>
      </header>

      <main>
        <section className="max-w-7xl mx-auto px-6 pt-24 pb-16 text-center">
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-neural-100 text-neural-700 rounded-full text-sm font-medium mb-8">
            ⚡ Plataforma de Automatización con IA
          </div>
          <h1 className="text-6xl font-bold mb-6 leading-tight">
            Automatiza tu mundo con{' '}
            <span className="gradient-text">Inteligencia Artificial</span>
          </h1>
          <p className="text-xl text-gray-500 max-w-3xl mx-auto mb-10">
            Agentes IA, automatización de tareas, web scraping, análisis de datos y más.
            Todo en una plataforma unificada.
          </p>
          <div className="flex items-center justify-center gap-4">
            <Link href="/login" className="px-8 py-4 gradient-bg text-white rounded-xl font-semibold text-lg hover:opacity-90 transition shadow-lg shadow-neural-500/25">
              Comenzar Gratis
            </Link>
            <a href="https://github.com/Litios0912/neuralflow" target="_blank" className="px-8 py-4 bg-white border border-gray-200 rounded-xl font-semibold text-lg hover:bg-gray-50 transition shadow-sm flex items-center gap-2">
              ⭐ GitHub
            </a>
          </div>
        </section>

        <section className="max-w-7xl mx-auto px-6 py-20">
          <h2 className="text-3xl font-bold text-center mb-4">Agentes de IA</h2>
          <p className="text-gray-500 text-center mb-12 max-w-2xl mx-auto">
            Cuatro agentes especializados para cubrir todas tus necesidades
          </p>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              { icon: '🤖', title: 'Chat IA', desc: 'Asistente conversacional con Groq AI. Responde preguntas, ayuda con código y más.' },
              { icon: '🕸️', title: 'Web Scraper', desc: 'Extrae contenido de cualquier sitio web de forma inteligente.' },
              { icon: '✍️', title: 'Content Generator', desc: 'Genera blogs, posts, emails y código con IA.' },
              { icon: '📊', title: 'Data Analyzer', desc: 'Analiza datos JSON y obtén estadísticas al instante.' },
            ].map((agent, i) => (
              <div key={i} className="glass rounded-2xl p-6 card-hover">
                <div className="text-4xl mb-4">{agent.icon}</div>
                <h3 className="text-lg font-bold mb-2">{agent.title}</h3>
                <p className="text-gray-500 text-sm">{agent.desc}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="bg-gray-900 text-white py-20">
          <div className="max-w-7xl mx-auto px-6">
            <h2 className="text-3xl font-bold text-center mb-16">Características</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {[
                { num: '🤖', title: 'Múltiples Agentes', desc: 'Chat, web scraping, generación de contenido y análisis de datos' },
                { num: '⚡', title: 'Automatización', desc: 'Programa tareas recurrentes con scheduling inteligente' },
                { num: '🔗', title: 'Multi-Plataforma', desc: 'Accede via Web, CLI, o Telegram' },
                { num: '🔐', title: 'Seguro', desc: 'Autenticación JWT y datos encriptados' },
                { num: '🐳', title: 'Docker Listo', desc: 'Despliegue fácil con docker-compose' },
                { num: '📱', title: 'Responsive', desc: 'Diseño adaptativo para cualquier dispositivo' },
              ].map((feat, i) => (
                <div key={i} className="text-center p-6">
                  <div className="text-4xl mb-4">{feat.num}</div>
                  <h3 className="text-xl font-bold mb-2">{feat.title}</h3>
                  <p className="text-gray-400">{feat.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </section>
      </main>

      <footer className="bg-gray-50 border-t py-12">
        <div className="max-w-7xl mx-auto px-6 text-center text-gray-500">
          <p>© 2026 NeuralFlow. Built by Litios0912</p>
        </div>
      </footer>
    </div>
  )
}
