import requests
import socket

CONSUL_HOST = 'localhost'
CONSUL_PORT = 8500


def register_service(service_name, service_port):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    registration_data = {
        "Name": service_name,
        "Address": ip_address,
        "Port": service_port,
        "Check": {
            "HTTP": f"http://{ip_address}:{service_port}/health/",
            "Interval": "10s"
        }
    }

    response = requests.put(
        f"http://{CONSUL_HOST}:{CONSUL_PORT}/v1/agent/service/register",
        json=registration_data
    )

    if response.status_code == 200:
        print(f"Service {service_name} registered successfully.")
    else:
        print(f"Failed to register service {service_name}: {response.text}")


# Call the function when your service starts
register_service("student_service", 8000)
