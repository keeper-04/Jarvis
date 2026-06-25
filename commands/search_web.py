import webbrowser

def run(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching Google for: {query}"

#if __name__ == "__main__":
#    run("marvel movies")