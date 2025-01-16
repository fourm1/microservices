from http.client import responses

import requests
from django.http import JsonResponse
from django.views import View
from .consul_client import discover_service

urls_services = {
    'students': 'student_service',
    'schools': 'school_service',
}


class ProxyView(View):

    def get(self, request, *args, **kwargs):
        path = kwargs.get('path', '')

        service_url = None

        # Discover the service using Consul
        for service in urls_services:
            print(service)
            if service in path:
                service_url = discover_service(service)
                print(service_url)
            if not service_url:
                return JsonResponse({"error": "Service not found"}, status=404)
            if service_url:
                responses = requests.get(service)

        # Forward the request to the appropriate service
        try:
            response = requests.get(f"http://{service_url}/{path}", params=request.GET)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": f"Failed to reach service: {str(e)}"}, status=500)
