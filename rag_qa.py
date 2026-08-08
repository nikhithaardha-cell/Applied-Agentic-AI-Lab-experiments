
# ============================================
# LAB 2: RAG-BASED QUESTION ANSWERING SYSTEM
# ============================================

# --------------------------------------------
# STEP 1: KNOWLEDGE BASE
# --------------------------------------------

documents = [

    "Artificial Intelligence is a branch of computer science that develops systems capable of performing tasks that normally require human intelligence.",

    "Large Language Models are artificial intelligence models trained on large amounts of text data. They can understand and generate human-like language.",

    "Agentic AI refers to AI systems that can plan tasks, make decisions, use tools and work toward specific goals.",

    "Retrieval-Augmented Generation, also known as RAG, combines information retrieval with answer generation. It retrieves relevant information from an external knowledge source before producing an answer.",

    "Embeddings are numerical representations of text. They represent the meaning of words, sentences, or documents.",

    "A vector database stores numerical representations called embeddings and allows similar information to be retrieved efficiently.",

    "Prompt engineering is the process of designing effective instructions for an AI model to obtain useful and relevant responses.",

    "RAG systems generally contain document loading, document processing, indexing, retrieval, and response generation.",

    "Cybersecurity is the practice of protecting computers, networks, applications, systems, and data from unauthorized access, attacks, damage, and cyber threats.",

    "Common cybersecurity threats include phishing, malware, ransomware, password attacks, denial-of-service attacks, and social engineering.",

    "Cybersecurity helps protect the confidentiality, integrity, and availability of information and computer systems."
]


# --------------------------------------------
# STEP 2: CREATE DOCUMENT INDEX
# --------------------------------------------

print("============================================")
print("       RAG QUESTION ANSWERING SYSTEM")
print("============================================")

print("\nCreating document index...")

index = {}

for document_number, document in enumerate(documents):

    # Convert document to lowercase
    words = (
        document.lower()
        .replace(",", "")
        .replace(".", "")
        .replace("(", "")
        .replace(")", "")
        .split()
    )

    # Store each word in the index
    for word in words:

        if word not in index:
            index[word] = []

        if document_number not in index[word]:
            index[word].append(document_number)


print("Document indexing completed.")


# --------------------------------------------
# STEP 3: RETRIEVE RELEVANT DOCUMENTS
# --------------------------------------------

def retrieve_documents(question):

    question_words = (
        question.lower()
        .replace("?", "")
        .replace(",", "")
        .replace(".", "")
        .split()
    )

    # Common words that are not useful for retrieval
    stop_words = {
        "what",
        "is",
        "are",
        "the",
        "a",
        "an",
        "of",
        "and",
        "to",
        "in",
        "for",
        "on",
        "how",
        "does",
        "do",
        "can",
        "tell",
        "me",
        "about"
    }

    # Remove common words
    question_words = [
        word for word in question_words
        if word not in stop_words
    ]

    scores = {}

    # Search the index
    for word in question_words:

        if word in index:

            for document_number in index[word]:

                if document_number not in scores:
                    scores[document_number] = 0

                scores[document_number] += 1


    # If no matching words are found
    if not scores:
        return []


    # Sort documents based on relevance
    ranked_documents = sorted(
        scores,
        key=scores.get,
        reverse=True
    )


    # Only return documents with the highest relevance
    best_score = scores[ranked_documents[0]]

    relevant_documents = []

    for document_number in ranked_documents:

        if scores[document_number] == best_score:

            relevant_documents.append(document_number)


    return relevant_documents[:2]


# --------------------------------------------
# STEP 4: RESPONSE GENERATION
# --------------------------------------------

def generate_answer(question, retrieved_documents):

    if not retrieved_documents:

        return (
            "Sorry, I could not find relevant information "
            "in the knowledge base."
        )


    answer = ""

    for document_number in retrieved_documents:

        answer += documents[document_number] + "\n"


    return answer.strip()


# --------------------------------------------
# STEP 5: GET USER QUESTION
# --------------------------------------------

question = input("\nEnter your question: ")


# --------------------------------------------
# STEP 6: RETRIEVE INFORMATION
# --------------------------------------------

retrieved_documents = retrieve_documents(question)


# --------------------------------------------
# STEP 7: DISPLAY RETRIEVED INFORMATION
# --------------------------------------------

print("\n--------------------------------------------")
print("RETRIEVED INFORMATION")
print("--------------------------------------------")


if retrieved_documents:

    for number, document_number in enumerate(
        retrieved_documents,
        start=1
    ):

        print("\nDocument", number)
        print(documents[document_number])

else:

    print(
        "No relevant information found "
        "in the knowledge base."
    )


# --------------------------------------------
# STEP 8: GENERATE ANSWER
# --------------------------------------------

answer = generate_answer(
    question,
    retrieved_documents
)


# --------------------------------------------
# STEP 9: DISPLAY FINAL ANSWER
# --------------------------------------------

print("\n--------------------------------------------")
print("GENERATED ANSWER")
print("--------------------------------------------")

print(answer)


# --------------------------------------------
# END OF PROGRAM
# --------------------------------------------
