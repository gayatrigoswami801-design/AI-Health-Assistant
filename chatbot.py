def chatbot():

    print("\n===== AI CHATBOT =====")

    question = input("Ask health question: ")

    if "fever" in question.lower():

        print("Drink water and take proper rest.")

    elif "cold" in question.lower():

        print("Avoid cold drinks and stay warm.")

    else:

        print("Consult doctor for proper guidance.")