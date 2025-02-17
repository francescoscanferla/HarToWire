import json


def parse_har(har_path):
    with open(har_path, "r", encoding="utf-8") as f:
        har_data = json.load(f)

    xhr_requests = []
    for entry in har_data["log"]["entries"]:
        request = entry["request"]
        _type = entry.get("_resourceType", "")
        if _type == "xhr":
            xhr_requests.append(entry)
    return xhr_requests


def generate_wiremock_json(xhr_entries):
    for entry in xhr_entries:
        request = entry["request"]
        response = entry["response"]
        body_text = response["content"].get("text", "")

        try:
            json_body = json.loads(body_text)
        except (json.JSONDecodeError, TypeError):
            json_body = {}

        full_url = request["url"]
        api_index = full_url.find("/api/")
        if api_index != -1:
            final_url = "/" + full_url[api_index + 5 :]
        else:
            final_url = full_url

        stub = {
            "request": {"method": request["method"], "urlPathPattern": final_url},
            "response": {
                "status": response["status"],
                "headers": {"Content-type": "application/json;charset=UTF-8"},
                "jsonBody": json_body,
            },
        }

    return json.dumps(stub, indent=2)
