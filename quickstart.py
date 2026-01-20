#!/usr/bin/env python3
"""
QUICK START GUIDE - Weather Disaster Management AI Agent
=========================================================

Run this script to see a complete walkthrough of the system!
"""

import subprocess
import sys
import os
import json
from pathlib import Path

def print_section(title):
    """Print a formatted section title"""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")

def main():
    os.chdir(Path(__file__).parent)
    
    print("\n")
    print("█████████████████████████████████████████████████████████████████████")
    print("█                                                                   █")
    print("█  🌍 WEATHER DISASTER MANAGEMENT AI AGENT SYSTEM                  █")
    print("█     Quick Start Guide                                            █")
    print("█                                                                   █")
    print("█████████████████████████████████████████████████████████████████████")
    
    # Step 1: Show what's installed
    print_section("Step 1: Verifying Installation")
    
    files = {
        'main.py': 'Basic agent (learning reference)',
        'advanced_agent.py': 'Production system with ML, DB, and multi-agent',
        'dashboard.py': 'Web-based real-time monitoring UI',
        'requirements.txt': 'Python dependencies',
        'README.md': 'Full documentation',
    }
    
    missing = []
    for filename, description in files.items():
        if Path(filename).exists():
            print(f"  ✅ {filename:<25} - {description}")
        else:
            print(f"  ❌ {filename:<25} - {description}")
            missing.append(filename)
    
    if missing:
        print(f"\n⚠️  Missing files: {', '.join(missing)}")
        return
    
    print("\n✅ All files present!")
    
    # Step 2: Explain the system
    print_section("Step 2: System Overview")
    
    overview = """
    This system has 3 learning levels:
    
    LEVEL 1: main.py
    ├─ Learn: Basic agent architecture
    ├─ Demonstrates: Perceive → Reason → Act loop
    ├─ Features: Rule-based risk assessment, simple tools
    └─ Run: python main.py
    
    LEVEL 2: advanced_agent.py
    ├─ Learn: Production-grade agentic AI
    ├─ Demonstrates: Multi-agent coordination, ML models, database
    ├─ Features: Database, ML risk assessment, API integration
    └─ Run: python advanced_agent.py
    
    LEVEL 3: dashboard.py
    ├─ Learn: Full system visualization
    ├─ Demonstrates: Web UI, real-time monitoring, API endpoints
    ├─ Features: Interactive dashboard, auto-refresh, alerts
    └─ Run: python dashboard.py (then visit http://localhost:5000)
    
    Each level builds on the previous one!
    """
    
    print(overview)
    
    # Step 3: Show database structure
    print_section("Step 3: What Gets Stored")
    
    if Path('disaster_agent.db').exists():
        print("✅ Database exists with the following tables:\n")
        import sqlite3
        conn = sqlite3.connect('disaster_agent.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
            count = cursor.fetchone()[0]
            print(f"   📊 {table[0]:<30} ({count} records)")
        
        conn.close()
    else:
        print("📝 Database will be created automatically on first run")
    
    print("\nEach agent run saves:")
    print("   ├─ Weather observations (raw sensor data)")
    print("   ├─ Risk assessments (AI predictions)")
    print("   ├─ Actions log (decisions made)")
    print("   └─ Agent communications (inter-agent messages)")
    
    # Step 4: Show next steps
    print_section("Step 4: Next Steps")
    
    steps = """
    Choose your learning path:
    
    🎯 Quick Demo (5 minutes)
       python main.py              # See basic agent in action
    
    🔍 Full System Demo (2 minutes)
       python advanced_agent.py    # See multi-agent + ML + DB
    
    🌐 Interactive Dashboard (ongoing)
       pip install -r requirements.txt
       python dashboard.py         # Open http://localhost:5000
    
    📚 Deep Learning (ongoing)
       1. Read the code comments in main.py
       2. Trace through the Perceive → Reason → Act loop
       3. Try modifying thresholds in DisasterAnalyzer
       4. Add a new weather location to RealWeatherAPI
       5. Train your own ML model with different data
    
    🚀 Challenge: Build Your Own
       1. Add a new agent type (e.g., SeismicAgent)
       2. Create a new tool (e.g., PopulationDensityAnalyzer)
       3. Implement learning (agents improve over time)
       4. Add real OpenWeatherMap API integration
    """
    
    print(steps)
    
    # Step 5: Show key learning concepts
    print_section("Step 5: Key Concepts to Master")
    
    concepts = {
        "Agent": "Autonomous system that perceives, reasons, and acts",
        "Tool": "Function/service an agent can use (sensors, analyzers)",
        "State": "What the agent knows (observations, assessments)",
        "Action": "What the agent does (decisions, orders)",
        "Coordination": "Multiple agents working together to solve problems",
        "PERCEIVE": "Gather data from environment using tools",
        "REASON": "Analyze data and make sense of situation",
        "ACT": "Execute decisions autonomously without human input",
        "ML Integration": "Use machine learning for decision making",
        "Database": "Persistent storage of all observations and actions",
    }
    
    for concept, definition in concepts.items():
        print(f"  • {concept:<20} - {definition}")
    
    print_section("Ready to Start?")
    
    print("""
    Run your first agent:
    
        python main.py
    
    Then explore the code and modify it to learn!
    
    Questions? Check:
    - README.md for full documentation
    - Code comments throughout the files
    - Challenge exercises in README.md
    
    Good luck! 🚀
    """)

if __name__ == "__main__":
    main()
