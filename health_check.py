import sys
import yaml
import requests
import time
from collections import defaultdict
from urllib.parse import urlparse

def load_yaml(file_path):
    """Load YAML configuration from the file."""
    with open(file_path, "r") as file:
        yaml_data = yaml.safe_load(file)
        return yaml_data
    
def check_health(endpoint):
    """Check health  of a given endpoint."""
    url = endpoint.get("url")
    method = endpoint.get("method", "GET").upper()
    headers = endpoint.get("headers", {})
    body = endpoint.get("body", None)
    
    # Returns current epoch time in seconds.
    start = time.time()
    try:
        response = requests.request(method, url, headers=headers, json=body, timeout=5)
        
        # To milliseconds
        latency = (time.time() - start) * 1000
        
        # Endpoint is Up and Healthy
        if 200 <= response.status_code < 300 and latency < 500:
            return True  
        
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed for {url}: {e}")
    
    # Endpoint is Unhealthy
    return False
    

def check_endpoints(file_path):
    """Monitor the endpoints based on the YAML configuration."""
    domain_stats = defaultdict(lambda: {"total": 0, "up": 0})
    endpoints = load_yaml(file_path)
    try:
        while True:
            for endpoint in endpoints:
                url = endpoint.get("url")
                
                # Extract the domain name of the endpoint.
                domain = urlparse(url).netloc
                
                is_healthy = check_health(endpoint)
                domain_stats[domain]["total"] += 1
                if is_healthy:
                    domain_stats[domain]["up"] += 1
                # print(domain_stats.items())
                
            # Print Availability Percentages.
            for domain, stats in domain_stats.items():
                uptime = round((stats["up"] / stats["total"]) * 100)
                print(f"{domain} has {uptime}% availability percentage")
            print("\n")
            
            # Wait for 15 Seconds.
            time.sleep(15)
            
    except KeyboardInterrupt:
        print("\nMonitoring interrupted by user\nExiting...")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please pass the YAML file path!!")
        sys.exit(1)
        
    file_path = sys.argv[1]
    check_endpoints(file_path)