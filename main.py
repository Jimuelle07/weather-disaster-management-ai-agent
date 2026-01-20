"""
Weather Disaster Management AI Agent
====================================

This is an agentic AI system that monitors weather conditions and takes 
autonomous actions to manage disaster risks.

Key Concepts:
- Agent: An autonomous system that perceives, reasons, and acts
- Tools: Functions the agent can use to gather data and take actions
- State: Information about the current situation
- Decision Making: Logic to determine what action to take
"""

import json
import sys
import os
from datetime import datetime
from enum import Enum
from dataclasses import dataclass

# Fix encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# ============================================================================
# PART 1: Define the Agent's Tools (Perception Layer)
# ============================================================================

class WeatherCondition(Enum):
    """Different weather states the agent can identify"""
    NORMAL = "normal"
    RAINY = "rainy"
    STORMY = "stormy"
    HURRICANE = "hurricane"
    FLOOD_RISK = "flood_risk"


@dataclass
class WeatherData:
    """Data structure for weather information"""
    temperature: float      # Celsius
    humidity: float         # Percentage
    wind_speed: float       # km/h
    rainfall: float         # mm
    location: str
    timestamp: datetime


class WeatherSensor:
    """Tool 1: Simulates real weather data collection"""
    
    def get_weather_data(self, location: str) -> WeatherData:
        """
        In a real system, this would fetch from weather APIs.
        For now, we simulate weather data.
        """
        # Simulate different weather conditions for demonstration
        weather_scenarios = {
            "coastal_city": {
                "temperature": 28,
                "humidity": 85,
                "wind_speed": 65,  # High wind = potential hurricane
                "rainfall": 50,
            },
            "inland_valley": {
                "temperature": 25,
                "humidity": 60,
                "wind_speed": 15,
                "rainfall": 5,
            },
            "mountain_region": {
                "temperature": 15,
                "humidity": 70,
                "wind_speed": 45,
                "rainfall": 100,  # Heavy rain = flood risk
            }
        }
        
        data = weather_scenarios.get(location, weather_scenarios["inland_valley"])
        
        return WeatherData(
            temperature=data["temperature"],
            humidity=data["humidity"],
            wind_speed=data["wind_speed"],
            rainfall=data["rainfall"],
            location=location,
            timestamp=datetime.now()
        )


class DisasterAnalyzer:
    """Tool 2: Analyzes weather data to assess disaster risk"""
    
    def assess_risk(self, weather: WeatherData) -> WeatherCondition:
        """
        The agent uses this tool to understand the situation (REASONING).
        
        Rules-based decision making:
        - Wind speed > 150 km/h = Hurricane danger
        - Rainfall > 75mm in short period = Flood risk
        - Wind > 60 km/h with high humidity = Storm risk
        """
        
        if weather.wind_speed > 150:
            return WeatherCondition.HURRICANE
        
        if weather.rainfall > 75:
            return WeatherCondition.FLOOD_RISK
        
        if weather.wind_speed > 60 and weather.humidity > 80:
            return WeatherCondition.STORMY
        
        if weather.rainfall > 20:
            return WeatherCondition.RAINY
        
        return WeatherCondition.NORMAL
    
    def get_risk_score(self, condition: WeatherCondition) -> int:
        """Quantifies the risk level"""
        risk_levels = {
            WeatherCondition.NORMAL: 0,
            WeatherCondition.RAINY: 2,
            WeatherCondition.STORMY: 5,
            WeatherCondition.FLOOD_RISK: 7,
            WeatherCondition.HURRICANE: 10,
        }
        return risk_levels[condition]


class ResponsePlanner:
    """Tool 3: Plans response actions based on risk assessment"""
    
    def get_recommended_actions(self, condition: WeatherCondition) -> list[str]:
        """
        The agent uses this to DECIDE what actions to take.
        
        Different risk levels trigger different response protocols.
        """
        actions = {
            WeatherCondition.NORMAL: [
                "Continue normal operations",
                "Maintain routine monitoring",
            ],
            WeatherCondition.RAINY: [
                "Issue rain advisory",
                "Advise residents to stay indoors",
                "Prepare drainage systems",
            ],
            WeatherCondition.STORMY: [
                "Issue storm warning",
                "Activate emergency shelters",
                "Deploy emergency response teams",
                "Issue evacuation advisory for exposed areas",
            ],
            WeatherCondition.FLOOD_RISK: [
                "Activate flood warning system",
                "Close vulnerable roads",
                "Pre-position rescue equipment",
                "Implement evacuation plan",
            ],
            WeatherCondition.HURRICANE: [
                "Activate all emergency protocols",
                "Mandatory evacuation for coastal areas",
                "Deploy all emergency services",
                "Set up emergency command center",
                "Activate disaster relief coordination",
            ],
        }
        return actions.get(condition, [])


# ============================================================================
# PART 2: The Agent (Decision Making & Action Layer)
# ============================================================================

class DisasterManagementAgent:
    """
    The main AGENT that brings everything together.
    
    It has:
    - Tools: sensor, analyzer, planner
    - Memory: tracks what it knows
    - Decision logic: determines what to do
    - Action execution: carries out decisions
    """
    
    def __init__(self):
        # Initialize tools
        self.weather_sensor = WeatherSensor()
        self.risk_analyzer = DisasterAnalyzer()
        self.response_planner = ResponsePlanner()
        
        # Memory: track state and history
        self.current_observations = {}
        self.action_history = []
    
    def perceive(self, location: str) -> WeatherData:
        """
        STEP 1: PERCEIVE - Agent gathers data from its environment
        Using Tool 1: WeatherSensor
        """
        print(f"\n📡 [PERCEIVE] Agent is gathering weather data for {location}...")
        weather = self.weather_sensor.get_weather_data(location)
        
        self.current_observations[location] = weather
        print(f"   Temperature: {weather.temperature}°C")
        print(f"   Humidity: {weather.humidity}%")
        print(f"   Wind Speed: {weather.wind_speed} km/h")
        print(f"   Rainfall: {weather.rainfall} mm")
        
        return weather
    
    def reason(self, weather: WeatherData) -> tuple[WeatherCondition, int]:
        """
        STEP 2: REASON - Agent analyzes the situation
        Using Tool 2: DisasterAnalyzer
        
        This is where the "intelligence" happens - the agent interprets
        raw data and draws conclusions.
        """
        print(f"\n🧠 [REASON] Agent is analyzing the situation...")
        
        condition = self.risk_analyzer.assess_risk(weather)
        risk_score = self.risk_analyzer.get_risk_score(condition)
        
        print(f"   Assessed Condition: {condition.value.upper()}")
        print(f"   Risk Score: {risk_score}/10")
        
        return condition, risk_score
    
    def decide_and_act(self, condition: WeatherCondition, location: str):
        """
        STEP 3: DECIDE & ACT - Agent takes action based on reasoning
        Using Tool 3: ResponsePlanner
        
        The agent doesn't just report - it TAKES ACTION autonomously.
        """
        print(f"\n⚡ [DECIDE & ACT] Agent is executing response plan...")
        
        actions = self.response_planner.get_recommended_actions(condition)
        
        print(f"   Recommended Actions:")
        for i, action in enumerate(actions, 1):
            print(f"   {i}. {action}")
        
        # Record in memory
        self.action_history.append({
            "timestamp": datetime.now(),
            "location": location,
            "condition": condition.value,
            "actions": actions
        })
        
        return actions
    
    def monitor_and_respond(self, location: str):
        """
        Main agent loop: PERCEIVE → REASON → ACT
        
        This is the core agent behavior. It runs autonomously without
        waiting for human commands for every decision.
        """
        print(f"\n{'='*60}")
        print(f"🤖 WEATHER DISASTER MANAGEMENT AGENT - MONITORING {location.upper()}")
        print(f"{'='*60}")
        
        # PERCEIVE: Gather information
        weather = self.perceive(location)
        
        # REASON: Analyze and understand
        condition, risk_score = self.reason(weather)
        
        # DECIDE & ACT: Take action
        actions = self.decide_and_act(condition, location)
        
        return {
            "location": location,
            "condition": condition.value,
            "risk_score": risk_score,
            "actions_taken": actions
        }
    
    def generate_report(self) -> str:
        """Generate a summary report of all agent activities"""
        report = "\n" + "="*60 + "\n"
        report += "📊 AGENT ACTIVITY REPORT\n"
        report += "="*60 + "\n"
        
        for entry in self.action_history:
            report += f"\nTime: {entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}\n"
            report += f"Location: {entry['location']}\n"
            report += f"Condition: {entry['condition'].upper()}\n"
            report += f"Actions: {len(entry['actions'])} taken\n"
        
        return report


# ============================================================================
# PART 3: Run the Agent
# ============================================================================

def main():
    """
    Demonstrate the agentic AI in action!
    """
    
    # Create an agent
    agent = DisasterManagementAgent()
    
    # The agent monitors multiple locations autonomously
    locations = ["coastal_city", "mountain_region", "inland_valley"]
    
    for location in locations:
        result = agent.monitor_and_respond(location)
    
    # Print activity report
    print(agent.generate_report())
    
    print("\n" + "="*60)
    print("✅ Agent monitoring complete")
    print("="*60)


if __name__ == "__main__":
    main()
