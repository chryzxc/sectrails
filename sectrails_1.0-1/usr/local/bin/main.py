# filepath: sectrails/main.py
import requests
import json
from tabulate import tabulate
from datetime import datetime
import argparse

def fetch_data(api_key, target):
    url = f"https://api.securitytrails.com/v1/history/{target}/dns/a"
    headers = {
        "APIKEY": api_key
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def calculate_duration(first_seen, last_seen):
    first_date = datetime.strptime(first_seen, "%Y-%m-%d")
    last_date = datetime.strptime(last_seen, "%Y-%m-%d")
    duration = last_date - first_date
    return duration.days

def display_data(data):
    table = []
    for record in data['records']:
        ip = record['values'][0]['ip']
        organization = record['organizations'][0]
        first_seen = record['first_seen']
        last_seen = record['last_seen']
        duration_seen = calculate_duration(first_seen, last_seen)
        table.append([ip, organization, first_seen, last_seen, duration_seen])
    
    headers = ["IP Address", "Organization", "First Seen", "Last Seen", "Duration Seen (days)"]
    print(tabulate(table, headers, tablefmt="grid"))

def main():
    parser = argparse.ArgumentParser(description="Fetch DNS history from SecurityTrails")
    parser.add_argument("-target", required=True, help="Target domain")
    parser.add_argument("-apikey", required=True, help="API key for SecurityTrails")
    args = parser.parse_args()

    data = fetch_data(args.apikey, args.target)
    display_data(data)

if __name__ == "__main__":
    main()