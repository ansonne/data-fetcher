from data_fetcher import fetch_json, filter_items, extract_field

API_URL = "https://jsonplaceholder.typicode.com/users"


def main():
    data = fetch_json(API_URL)
    filtered = [
        item for item in data if item.get("address", {}).get("city") == "Aliyaview"
    ]
    names = extract_field(filtered, "name")
    print("Filtered names:", names)


if __name__ == "__main__":
    main()
