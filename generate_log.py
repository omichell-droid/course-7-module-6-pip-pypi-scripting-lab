from datetime import datetime


def generate_log(data):
    """Write each item in `data` to log_YYYYMMDD.txt and return the filename."""
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Log data must be a list.")

    # STEP 2: Build a filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write each entry on its own line
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Confirm
    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetch a sample post from a public API using the requests package."""
    import requests

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        pass
    return {}


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    post = fetch_data()
    if post:
        log_data.append(f"Fetched post: {post.get('title', 'No title found')}")
    generate_log(log_data)