"""
Web Dashboard for Weather Disaster Management Agent
====================================================

A Flask-based web interface to monitor the multi-agent system in real-time.

Run: python dashboard.py
Then visit: http://localhost:5000
"""

from flask import Flask, render_template_string, jsonify, request
from flask_cors import CORS
import json
import sqlite3
from datetime import datetime, timedelta
from advanced_agent import (
    DatabaseManager, MLRiskAssessor, RealWeatherAPI, 
    RegionalDisasterAgent, DisasterManagementCoordinator, APIServer
)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize system components (shared across requests)
db = DatabaseManager()
ml_assessor = MLRiskAssessor()
weather_api = RealWeatherAPI()
coordinator = DisasterManagementCoordinator(db)
api_server = APIServer(coordinator, db)

# Setup agents
regions = ["coastal_city", "mountain_region", "inland_valley"]
for i, region in enumerate(regions, 1):
    agent = RegionalDisasterAgent(
        agent_id=f"AGENT_{i}_{region.upper()}",
        region=region,
        db=db,
        ml_assessor=ml_assessor,
        weather_api=weather_api
    )
    coordinator.register_agent(agent)


# ============================================================================
# HTML Dashboard Template
# ============================================================================

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Disaster Management - AI Agent Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.1em;
            opacity: 0.9;
        }
        
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .card {
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            animation: slideIn 0.3s ease-out;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .card h2 {
            color: #333;
            margin-bottom: 15px;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }
        
        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }
        
        .status-good { background-color: #4CAF50; }
        .status-warning { background-color: #ff9800; }
        .status-critical { background-color: #f44336; }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        .agent-box {
            background: #f5f5f5;
            border-left: 4px solid #667eea;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        
        .agent-box.critical {
            border-left-color: #f44336;
            background: #ffebee;
        }
        
        .agent-box.warning {
            border-left-color: #ff9800;
            background: #fff3e0;
        }
        
        .agent-info {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 8px 0;
        }
        
        .agent-info label {
            font-weight: bold;
            color: #555;
        }
        
        .agent-info span {
            color: #666;
        }
        
        .risk-meter {
            width: 100%;
            height: 20px;
            background: #ddd;
            border-radius: 10px;
            overflow: hidden;
            margin: 10px 0;
        }
        
        .risk-fill {
            height: 100%;
            background: linear-gradient(to right, #4CAF50, #ff9800, #f44336);
            transition: width 0.3s ease;
        }
        
        .actions-list {
            background: #f9f9f9;
            border-radius: 5px;
            padding: 10px;
            margin-top: 10px;
            max-height: 300px;
            overflow-y: auto;
        }
        
        .action-item {
            padding: 8px;
            margin: 5px 0;
            border-left: 3px solid #667eea;
            background: white;
            font-size: 0.9em;
        }
        
        .action-item.critical {
            border-left-color: #f44336;
            background: #ffebee;
        }
        
        .action-item.high {
            border-left-color: #ff9800;
            background: #fff3e0;
        }
        
        .button {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            margin-top: 10px;
            transition: background 0.3s;
        }
        
        .button:hover {
            background: #764ba2;
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
            margin-top: 15px;
        }
        
        .stat {
            background: #f0f0f0;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
        }
        
        .stat-value {
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }
        
        .stat-label {
            color: #666;
            margin-top: 5px;
        }
        
        .alert-item {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 10px;
            margin: 8px 0;
            border-radius: 3px;
            font-size: 0.9em;
        }
        
        .alert-item.critical {
            background: #f8d7da;
            border-left-color: #f44336;
        }
        
        .refresh-time {
            text-align: right;
            color: #999;
            font-size: 0.85em;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌍 Weather Disaster Management AI Agent</h1>
            <p>Multi-Agent System for Real-Time Disaster Response</p>
        </div>
        
        <!-- System Overview -->
        <div class="card">
            <h2>📊 System Overview</h2>
            <div class="stats">
                <div class="stat">
                    <div class="stat-value" id="total-agents">0</div>
                    <div class="stat-label">Active Agents</div>
                </div>
                <div class="stat">
                    <div class="stat-value" id="high-risk">0</div>
                    <div class="stat-label">High-Risk Regions</div>
                </div>
                <div class="stat">
                    <div class="stat-value" id="active-alerts">0</div>
                    <div class="stat-label">Active Alerts</div>
                </div>
                <div class="stat">
                    <div class="stat-value" id="responses">0</div>
                    <div class="stat-label">Response Actions</div>
                </div>
            </div>
            <button class="button" onclick="runMonitoring()">▶️ Run System Monitoring</button>
            <div class="refresh-time">Last update: <span id="last-update">Never</span></div>
        </div>
        
        <!-- Regional Agents -->
        <div class="grid" id="agents-container">
            <div class="card">
                <h2>🤖 Regional Agents</h2>
                <p>Loading agent data...</p>
            </div>
        </div>
        
        <!-- Recent Alerts -->
        <div class="card">
            <h2>⚠️ Recent Alerts & Actions</h2>
            <div id="alerts-container">
                <p>No recent alerts</p>
            </div>
            <div class="refresh-time">Updates auto-refresh every 10 seconds</div>
        </div>
    </div>
    
    <script>
        // Auto-update dashboard
        function updateDashboard() {
            Promise.all([
                fetch('/api/status').then(r => r.json()),
                fetch('/api/agents').then(r => r.json()),
                fetch('/api/alerts').then(r => r.json())
            ]).then(([status, agents, alerts]) => {
                updateStatus(status);
                updateAgents(agents);
                updateAlerts(alerts);
                document.getElementById('last-update').textContent = 
                    new Date().toLocaleTimeString();
            });
        }
        
        function updateStatus(status) {
            document.getElementById('total-agents').textContent = status.total_agents || 0;
            document.getElementById('high-risk').textContent = 
                status.global_status?.high_risk_regions?.length || 0;
            document.getElementById('active-alerts').textContent = 
                status.global_status?.active_alerts?.length || 0;
        }
        
        function updateAgents(agents) {
            const container = document.getElementById('agents-container');
            if (!agents.agents || agents.agents.length === 0) {
                container.innerHTML = '<div class="card"><p>No agents available</p></div>';
                return;
            }
            
            container.innerHTML = agents.agents.map(agent => `
                <div class="card">
                    <h2>
                        <span class="status-indicator status-good"></span>
                        ${agent.region}
                    </h2>
                    <div class="agent-box">
                        <div class="agent-info">
                            <label>Agent ID:</label>
                            <span>${agent.id}</span>
                        </div>
                        ${agent.last_assessment ? `
                            <div class="agent-info">
                                <label>Condition:</label>
                                <span>${agent.last_assessment.condition}</span>
                            </div>
                            <div class="agent-info">
                                <label>Risk Score:</label>
                                <span>${agent.last_assessment.risk_score}/10</span>
                            </div>
                            <div class="risk-meter">
                                <div class="risk-fill" style="width: ${agent.last_assessment.risk_score * 10}%"></div>
                            </div>
                            <div class="agent-info">
                                <label>Confidence:</label>
                                <span>${(agent.last_assessment.confidence * 100).toFixed(1)}%</span>
                            </div>
                        ` : '<p>No assessment yet</p>'}
                    </div>
                </div>
            `).join('');
        }
        
        function updateAlerts(data) {
            const container = document.getElementById('alerts-container');
            if (!data.alerts || data.alerts.length === 0) {
                container.innerHTML = '<p>No recent alerts</p>';
                return;
            }
            
            container.innerHTML = `
                <p><strong>${data.total_alerts}</strong> alerts in last 24 hours</p>
                ${data.alerts.slice(0, 10).map(alert => `
                    <div class="alert-item ${alert.priority.toLowerCase() === 'critical' ? 'critical' : ''}">
                        <strong>[${alert.priority}]</strong> ${alert.action}
                        <br><small>${alert.agent} @ ${new Date(alert.timestamp).toLocaleString()}</small>
                    </div>
                `).join('')}
            `;
        }
        
        function runMonitoring() {
            const btn = event.target;
            btn.disabled = true;
            btn.textContent = '⏳ Running...';
            
            fetch('/api/run-monitoring', {method: 'POST'})
                .then(r => r.json())
                .then(data => {
                    updateDashboard();
                    alert('✅ Monitoring cycle complete!');
                })
                .finally(() => {
                    btn.disabled = false;
                    btn.textContent = '▶️ Run System Monitoring';
                });
        }
        
        // Initial load and auto-refresh
        updateDashboard();
        setInterval(updateDashboard, 10000);
    </script>
</body>
</html>
"""


# ============================================================================
# API Routes
# ============================================================================

@app.route('/')
def dashboard():
    """Serve the main dashboard"""
    return render_template_string(DASHBOARD_HTML)


@app.route('/api/status')
def get_status():
    """Get current system status"""
    return jsonify({
        'total_agents': len(coordinator.agents),
        'global_status': coordinator.global_status,
        'timestamp': datetime.now().isoformat()
    })


@app.route('/api/agents')
def get_agents():
    """Get all agents and their current state"""
    agents_data = []
    
    for agent in coordinator.agents.values():
        agents_data.append({
            'id': agent.agent_id,
            'region': agent.region,
            'capabilities': agent.capabilities,
            'last_assessment': agent.last_assessment
        })
    
    return jsonify({
        'agents': agents_data,
        'total': len(agents_data)
    })


@app.route('/api/alerts')
def get_alerts():
    """Get recent alerts"""
    hours = request.args.get('hours', 24, type=int)
    alerts = api_server.get_alerts(hours)
    return jsonify(alerts)


@app.route('/api/region/<region>/history')
def get_region_history(region):
    """Get weather history for a specific region"""
    hours = request.args.get('hours', 24, type=int)
    history = api_server.get_region_history(region, hours)
    return jsonify(history)


@app.route('/api/run-monitoring', methods=['POST'])
def run_monitoring():
    """Trigger a full monitoring cycle"""
    results = coordinator.coordinate_agents()
    return jsonify(results)


@app.route('/api/report/json')
def get_json_report():
    """Export system state as JSON"""
    report = api_server.export_json_report()
    return app.response_class(
        response=report,
        status=200,
        mimetype='application/json'
    )


# ============================================================================
# Run Application
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🌐 STARTING WEB DASHBOARD")
    print("="*70)
    print("\n📊 Dashboard available at: http://localhost:5000")
    print("\n🤖 Agents registered:")
    for agent in coordinator.agents.values():
        print(f"   - {agent.agent_id} ({agent.region})")
    print("\n" + "="*70)
    
    app.run(debug=True, host='localhost', port=5000)
