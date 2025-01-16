import requests

CONSUL_HOST = 'localhost'
CONSUL_PORT = 8500


def discover_service(service_name):
    response = requests.get(f"http://{CONSUL_HOST}:{CONSUL_PORT}/v1/agent/services")
    services = response.json()

    for service_id, service in services.items():
        if service['Service'] == service_name:
            return f"{service['Address']}:{service['Port']}"

    return None
