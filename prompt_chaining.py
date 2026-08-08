
# ============================================
# LAB 3: PROMPT CHAINING FOR SUMMARIZATION
# ============================================

print("============================================")
print("       PROMPT CHAINING SUMMARIZATION")
print("============================================")


# --------------------------------------------
# STEP 1: GET INPUT TEXT
# --------------------------------------------

text = input("\nEnter the text to summarize:\n")


# --------------------------------------------
# CHAIN 1: EXTRACT KEY POINTS
# --------------------------------------------

def extract_key_points(text):

    sentences = text.split(".")

    key_points = []

    for sentence in sentences:

        sentence = sentence.strip()

        if sentence:
            key_points.append(sentence)

    return key_points


# --------------------------------------------
# CHAIN 2: ORGANIZE KEY POINTS
# --------------------------------------------

def organize_key_points(key_points):

    organized_points = []

    for point in key_points:

        point = point.strip()

        if point:
            organized_points.append(point)

    return organized_points


# --------------------------------------------
# CHAIN 3: GENERATE FINAL SUMMARY
# --------------------------------------------

def generate_summary(organized_points):

    if not organized_points:
        return "No information available."

    # Select important points
    important_points = organized_points[:3]

    summary = ". ".join(important_points)

    return summary + "."


# --------------------------------------------
# EXECUTE PROMPT CHAIN
# --------------------------------------------

# Chain 1
key_points = extract_key_points(text)


print("\n--------------------------------------------")
print("STEP 1: EXTRACTED KEY POINTS")
print("--------------------------------------------")

for number, point in enumerate(key_points, start=1):

    print(str(number) + ". " + point)


# Chain 2
organized_points = organize_key_points(key_points)


print("\n--------------------------------------------")
print("STEP 2: ORGANIZED KEY POINTS")
print("--------------------------------------------")

for number, point in enumerate(
    organized_points,
    start=1
):

    print(str(number) + ". " + point)


# Chain 3
final_summary = generate_summary(organized_points)


print("\n--------------------------------------------")
print("STEP 3: FINAL SUMMARY")
print("--------------------------------------------")

print(final_summary)


# --------------------------------------------
# COMPLETION
# --------------------------------------------

print("\n============================================")
print("Prompt chaining completed successfully.")
print("============================================")

