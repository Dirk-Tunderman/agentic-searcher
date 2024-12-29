from typing import Text

class TextSummarizer:
    def __init__(self, config):
        self.config = config

    def summarize(self, text: Text) -> Text:
        """Generate a summary of the input text"""
        pass

    def calculate_relevance(self, text: Text, query: Text) -> float:
        """Calculate relevance score between text and query"""
        pass