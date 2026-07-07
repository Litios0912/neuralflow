# AI Agents

NeuralFlow comes with 4 built-in AI agents.

## Chat Agent 🤖

General purpose AI assistant powered by Groq.

### Configuration
- `system_prompt`: Custom system prompt
- `model`: Model to use (default: mixtral-8x7b-32768)
- `api_key`: Custom Groq API key

### Usage
```
Input: Explain quantum computing in simple terms
Output: [AI-generated explanation]
```

## Web Scraper Agent 🕸️

Extract content from websites intelligently.

### Features
- Extracts main content (removes ads, nav, scripts)
- Supports multiple URLs per request
- Returns clean, readable text

### Usage
```
Input: https://example.com
Output: [Extracted content from the page]
```

## Content Generator Agent ✍️

Generate various types of content with AI.

### Configuration
- `type`: blog, social, email, code
- `tone`: professional, casual, formal
- `length`: short, medium, long

### Usage
```
Input: Write a blog post about AI automation trends
Output: [Generated blog post]
```

## Data Analyzer Agent 📊

Analyze JSON data and extract insights.

### Features
- Detects arrays and objects
- Calculates statistics for numeric fields
- Shows field names and counts

### Usage
```
Input: [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
Output: [Analysis with min, max, avg for age, etc.]
```

## Custom Agents

The agent system is extensible. Create your own by subclassing `BaseAgent` and registering with the `AgentFactory`.
