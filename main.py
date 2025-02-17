import sys
import os
from har_parser import parse_har, generate_wiremock_json


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <har_file> <file_prefix>")
        sys.exit(1)

    har_file_path = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) >= 3 else "wiremock_mappings"

    xhr_requests = parse_har(har_file_path)

    mappings_dir = os.path.join(os.path.expanduser("~"), "Desktop", "mappings")
    os.makedirs(mappings_dir, exist_ok=True)

    for i, request in enumerate(xhr_requests):
        single_wiremock_data = generate_wiremock_json([request])
        output_file = os.path.join(mappings_dir, f"{prefix}_{i}.json")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(single_wiremock_data)
        print(f"Creato file: {output_file}")


if __name__ == "__main__":
    main()
