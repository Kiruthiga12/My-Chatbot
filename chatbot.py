from groq import Groq
client = Groq(api_key= "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")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ FIXED MODEL
        messages=[{"role": "user", "content": user_input}],
        stream=True,
    )

    print("Chatbot: ", end="", flush=True)
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()
