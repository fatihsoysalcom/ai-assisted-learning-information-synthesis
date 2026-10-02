import re
from collections import Counter

def traditional_learning_approach(text, keywords):
    """
    Simulates a traditional learning approach: finding and counting keywords.
    Focuses on information retrieval and memorization.
    """
    print("--- Traditional Learning Approach (Keyword Spotting & Memorization) ---")
    found_keywords = {}
    for keyword in keywords:
        # Case-insensitive search for whole words
        matches = re.findall(r'\b' + re.escape(keyword) + r'\b', text, re.IGNORECASE)
        found_keywords[keyword] = len(matches)
        if matches:
            print(f"Keyword '{keyword}': Found {len(matches)} times.")
    print("\nKeywords found and their counts:", found_keywords)
    # Illustrates the article's point about traditional learning focusing on facts
    print("This approach focuses on identifying specific facts and their occurrences.")

def ai_assisted_learning_approach(text):
    """
    Simulates an AI-assisted learning approach: focusing on understanding,
    synthesis, and extracting key themes beyond simple keyword matching.
    (Simplified simulation using standard library text processing).
    """
    print("\n--- AI-Assisted Learning Approach (Understanding & Synthesis) ---")

    # 1. Sentence Tokenization
    # Splits text into sentences, a fundamental step for understanding context.
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    print(f"Total sentences identified: {len(sentences)}")

    # 2. Identify common multi-word phrases (simulating theme/concept extraction)
    # This goes beyond single keywords to find recurring ideas, representing synthesis.
    words = re.findall(r'\b\w+\b', text.lower())
    # Generate bigrams (two-word phrases)
    bigrams = [' '.join(words[i:i+2]) for i in range(len(words) - 1)]
    # Count frequency of bigrams
    bigram_counts = Counter(bigrams)

    # Filter out very common, less meaningful bigrams and get top 5
    filtered_bigrams = {phrase: count for phrase, count in bigram_counts.items()
                        if count > 1 and len(phrase.split()) > 1 and len(phrase) > 5}
    top_phrases = sorted(filtered_bigrams.items(), key=lambda item: item[1], reverse=True)[:5]

    print("\nTop 5 Common Multi-Word Phrases (simulating theme extraction/synthesis):")
    for phrase, count in top_phrases:
        print(f"- '{phrase}' (occurs {count} times)")
    # Illustrates the article's point about AI helping with synthesis and understanding themes

    # 3. Basic Extractive Summary (simulating identifying core arguments)
    # Prioritize sentences that contain any of the identified top phrases to form a summary.
    summary_sentences = []
    phrase_texts = [p for p, c in top_phrases]

    for sentence in sentences:
        if len(sentence.split()) < 8: # Skip very short sentences
            continue
        # Check if the sentence contains any of the top phrases (case-insensitive)
        if any(re.search(r'\b' + re.escape(phrase) + r'\b', sentence, re.IGNORECASE) for phrase in phrase_texts):
            summary_sentences.append(sentence.strip())
            if len(summary_sentences) >= 3: # Limit summary to 3 sentences
                break

    print("\nExtractive Summary of Key Points (simulating understanding core arguments):")
    if not summary_sentences:
        # Fallback: just pick the first few longer sentences if no phrases matched
        summary_sentences = [s.strip() for s in sentences if len(s.split()) > 8][:3]
    for s in summary_sentences:
        print(f"- {s}")
    # Illustrates the article's point about AI assisting in understanding and creating summaries

    print("\nThis approach aims to identify patterns, synthesize core ideas, and provide a more nuanced understanding, moving beyond mere fact retrieval.")

# --- Main part of the script ---
if __name__ == "__main__":
    # Sample text representing a body of information to be learned
    # This text is adapted from the article context itself, translated to English
    article_text = """
    As artificial intelligence (AI) permeates every aspect of our lives, our traditional learning methods are becoming insufficient. The ease of access to information and the opportunities offered by AI tools, how should they transform our learning process? This article will delve into the effects of AI on learning, question existing approaches, and together design future learning models. Learning is no longer about memorizing, but about the ability to understand, synthesize, and create.

    Artificial Intelligence and the Evolution of Learning: Why Now?

    Just a few decades ago, access to information was limited to dusty library shelves or expensive encyclopedias. Today, with a smartphone, we can access a large part of the planet's information in seconds. Alongside this information explosion, the breathtaking advancements in artificial intelligence technologies offer the potential to radically change our way of learning. What used to take hours of research can now be completed in minutes with AI-powered tools. This situation shifts the focus of the learning process from gathering and memorizing information to the skills of understanding, questioning, synthesizing, and creatively using information. This change deeply affects not only educational institutions but also individuals' lifelong learning strategies.
    """

    # --- Demonstrate Traditional Learning ---
    # Keywords a student might look for, representing a focus on facts.
    keywords_to_find = ["artificial intelligence", "AI", "learning methods", "information", "memorizing"]
    traditional_learning_approach(article_text, keywords_to_find)

    print("\n" + "="*80 + "\n")

    # --- Demonstrate AI-Assisted Learning ---
    ai_assisted_learning_approach(article_text)
