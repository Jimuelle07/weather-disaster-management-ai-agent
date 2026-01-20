# 🌍 Weather Disaster Management AI Agent System

A comprehensive **agentic AI** system for real-time disaster management using multiple autonomous agents, machine learning, and advanced decision-making.

## 🎯 What You're Building

This project teaches you **agentic AI** - AI systems that **autonomously perceive, reason, and act** without waiting for human commands.

### Key Components:

✅ **Real Weather API Integration** - Fetch actual weather data from OpenWeatherMap  
✅ **Machine Learning Risk Assessment** - Trained ML model for disaster prediction  
✅ **Database Integration** - SQLite database to track all observations and actions  
✅ **Multi-Agent System** - Multiple autonomous agents coordinating disaster response  
✅ **Web Dashboard** - Real-time visualization of system activities  
✅ **Advanced Decision Trees** - Sophisticated action planning based on conditions

---

## 📚 Learning Path

### Level 1: Basic Agent (main.py)

Start here to understand agent fundamentals:

- Perceive-Reason-Act Loop
- Tools and Sensors
- Risk Assessment
- Simple Decision Making

```bash
python main.py
```

### Level 2: Advanced System (advanced_agent.py)

Learn production-grade features:

- Database persistence
- ML-based decision making
- Multi-agent coordination
- API interfaces

```bash
python advanced_agent.py
```

### Level 3: Web Dashboard (dashboard.py)

See it all in action with real-time visualization:

```bash
# First install dependencies
pip install -r requirements.txt

# Run the dashboard
python dashboard.py

# Open http://localhost:5000 in your browser
```

---

## 🔧 Installation

### 1. Clone/Setup Project

```bash
cd weather-disaster-management-ai-agent
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Set OpenWeatherMap API Key

```bash
# Windows PowerShell
$env:OPENWEATHER_API_KEY="your_api_key_here"

# Or Windows Command Prompt
set OPENWEATHER_API_KEY=your_api_key_here
```

Get free API key at: https://openweathermap.org/api

---

## 🚀 Quick Start

### Run All Components

```bash
# 1. Basic agent demo
python main.py

# 2. Advanced multi-agent system
python advanced_agent.py

# 3. Web dashboard (in a new terminal)
pip install -r requirements.txt
python dashboard.py
# Then visit http://localhost:5000
```

---

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────────┐
│        Disaster Management Coordinator                   │
│     (Orchestrates all agents and decisions)             │
└──────────────────┬──────────────────────────────────────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
    ┌────────┐ ┌────────┐ ┌────────┐
    │ Agent  │ │ Agent  │ │ Agent  │
    │   1    │ │   2    │ │   3    │
    │Coastal │ │Mountain│ │ Valley │
    └────┬───┘ └───┬────┘ └────┬───┘
         │         │          │
         └─────────┴──────────┘
              │
        ┌─────┴─────────────────┐
        │                       │
        ▼                       ▼
   ┌─────────┐          ┌──────────────┐
   │ ML Risk │          │   Database   │
   │Assessor │          │  (SQLite)    │
   └─────────┘          └──────────────┘
        │
        └─────► Web Dashboard (Flask)
```

---

## 🧠 How Agentic AI Works

### The PERCEIVE → REASON → ACT Loop

Each agent runs this cycle autonomously:

```python
# 1. PERCEIVE: Gather Information
weather = agent.perceive()  # Get temperature, humidity, etc.

# 2. REASON: Analyze & Understand
condition, risk_score = agent.reason(weather)  # ML-based analysis

# 3. ACT: Take Action
actions = agent.decide_and_act(condition)  # Execute response plan
```

### Key Concepts

| Concept          | Meaning                   | Example                            |
| ---------------- | ------------------------- | ---------------------------------- |
| **Agent**        | Autonomous decision maker | Regional weather monitoring agent  |
| **Tool**         | Function agent can use    | WeatherSensor, DisasterAnalyzer    |
| **State**        | What the agent knows      | Last assessment, weather history   |
| **Action**       | What the agent does       | Issue alert, deploy resources      |
| **Coordination** | Agents working together   | Regional agents helping each other |

---

## 📁 Project Structure

```
weather-disaster-management-ai-agent/
├── main.py                    # Basic agent (START HERE!)
├── advanced_agent.py          # Production-grade system
├── dashboard.py               # Web UI
├── requirements.txt           # Python dependencies
├── disaster_agent.db          # SQLite database (auto-created)
├── risk_model.pkl             # ML model (auto-trained)
└── README.md                  # This file
```

---

## 🎓 What You'll Learn

### Agentic AI Concepts

- ✅ Autonomous decision making
- ✅ Multi-agent coordination
- ✅ Perception-Reasoning-Action loop
- ✅ Tool usage and integration
- ✅ State management

### Software Engineering

- ✅ Object-oriented design
- ✅ API integration (OpenWeatherMap)
- ✅ Database design (SQLite)
- ✅ Machine learning in production
- ✅ Web dashboard development
- ✅ System coordination

### AI/ML Skills

- ✅ Risk assessment algorithms
- ✅ Decision tree implementation
- ✅ Classifier training (scikit-learn)
- ✅ Model persistence

---

## 📊 Database Schema

### Tables

**weather_observations**

- Tracks all weather readings from sensors

**risk_assessments**

- Records AI predictions and confidence levels

**actions_log**

- Logs all response actions taken

**agent_communications**

- Records inter-agent messages for coordination

---

## 🔌 API Endpoints

When running the dashboard:

```
GET  /api/status              → Current system status
GET  /api/agents              → All agents and state
GET  /api/alerts              → Recent alerts
GET  /api/alerts?hours=24     → Alerts from last N hours
GET  /api/region/<name>/history → Weather history
POST /api/run-monitoring      → Trigger monitoring cycle
GET  /api/report/json         → Full system JSON export
```

---

## 🎯 Challenge Exercises

### Beginner

1. Modify `main.py` to add a new weather location
2. Change the risk thresholds in the rule-based system
3. Add a new condition type (e.g., TORNADO)

### Intermediate

4. Train the ML model with your own dataset
5. Add a new agent type (e.g., Seismic Monitoring Agent)
6. Create a new action priority level

### Advanced

7. Implement agent learning (agents improve over time)
8. Add real OpenWeatherMap API integration
9. Create a predictive model (forecast disasters)
10. Build mobile app to consume the APIs

---

## 🐛 Troubleshooting

### ImportError: No module named 'sklearn'

```bash
pip install scikit-learn
```

### No database file created

The database is created automatically on first run.

### Dashboard won't start

- Ensure port 5000 is available
- Try: `python dashboard.py --port 5001`

### ML model not training

ML features gracefully degrade to rule-based system if scikit-learn unavailable.

---

## 📚 Resources for Learning

### Agentic AI Concepts

- [Andrew Ng - Agentic AI](https://www.deeplearning.ai/resources/agentic-ai/)
- [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629)

### Implementation References

- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)

---

## 📝 License

Educational project - feel free to modify and learn!

---

## 🤝 Contributing

Have improvements? Feel free to extend:

- Add more weather conditions
- Improve ML model accuracy
- Add new agent types
- Enhance dashboard features

---

**Happy Learning! 🚀**

Questions? Start with `main.py` and work your way up!
