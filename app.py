import requests
import json


data = {
    "company_info": {
        "company_name": "Tech Innovators Inc.",
        "contact_person": "Jane Doe",
        "email": "jane.doe@techinnovators.com",
        "phone_number": "555-123-4567",
        "business_process": "Develops innovative software solutions for various industries."
    },
    "network_size": {
        "number_of_devices": "100-200",
        "expected_growth": "10 devices per year",
        "reason_for_growth": "Expansion of services",
        "key_applications": ["Email", "VoIP", "Video Conferencing"]
    },
    "bandwidth_requirements": {
        "bandwidth": {
            "email": "50 Mbps",
            "voip": "100 Mbps",
            "video_conferencing": "300 Mbps"
        },
        "latency_requirements": {
            "email": "Low",
            "voip": "Medium",
            "video_conferencing": "High"
        }
    },
    "security_compliance": {
        "security_requirements": ["Firewalls with model XYZ", "VPN (site-to-site)"],
        "compliance_standards": ["GDPR", "HIPAA"]
    },
    "ip_addressing_subnetting": {
        "ip_management": ["IPv4", "Static"],
        "subnetting_requirements": {
            "number_of_subnets": 5,
            "vlan_configurations": ["VLAN 1 for HR", "VLAN 2 for Finance"]
        }
    },
    "scalability_future_proofing": {
        "scalability_concerns": "High",
        "redundancy_failover": ["Load balancing", "Failover mechanisms"],
        "cloud_strategy": ["AWS for storage", "Azure for compute"]
    },
    "additional_requirements": {
        "vendor_preferences": ["Cisco", "Juniper"],
        "budget_constraints": "10000 USD",
        "additional_comments": "Ensure high availability",
        "future_plans": "Integration with cloud services"
    },
    "additional_considerations": {
        "budget": "Yes",
        "existing_infrastructure": "No existing infrastructure",
        "technical_expertise": "Intermediate level in network administration"
    },
    "network_diagram": "URL or attachment of the network diagram",
    "traffic_analysis": {
        "data_traffic_patterns": "High during working hours, low during off-hours",
        "volume": "500 GB per month"
    },
    "sla_requirements": {
        "uptime": "99.9%",
        "performance": "High performance",
        "security": "Top-notch security"
    }
}


url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key='


headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, json={"contents": [{"parts": [{"text": json.dumps(data)}, {"text": "Please suggest a suitable network topology based on the provided information."}]}]})


if response.status_code == 200:
    print("Topology recommendations received:")
    print(response.json())
else:
    print("Failed to get recommendations. Status code:", response.status_code)
    print("Response:", response.text)
