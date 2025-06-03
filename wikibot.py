import wikipedia

def get_wikipedia_summary(topic, sentences=2):
    """
    Fetches a summary from Wikipedia for the given topic.

    Args:
        topic (str): The topic to search for.
        sentences (int): Number of sentences to return in the summary.

    Returns:
        str: The summary text.
    """
    try:
        summary = wikipedia.summary(topic, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error. Options: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    while True:
        topic = input("Enter a Wikipedia topic (or type 'exit' to quit): ")
        if topic.lower() == 'exit':
            print("Exiting.")
            break
        print(get_wikipedia_summary(topic))
        print("-" * 60)