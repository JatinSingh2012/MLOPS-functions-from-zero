from wikibot import get_wikipedia_summary

def test_valid_topic():
    summary = get_wikipedia_summary("Python (programming language)", sentences=1)
    assert isinstance(summary, str)
    assert "Python" in summary or "programming" in summary

def test_disambiguation():
    result = get_wikipedia_summary("Mercury")
    assert "Disambiguation error" in result or "Options" in result

def test_page_not_found():
    result = get_wikipedia_summary("asdkfjhasdkjfhakjsdhf")
    assert result == "Page not found."

def test_invalid_input():
    result = get_wikipedia_summary("")
    assert isinstance(result, str)
