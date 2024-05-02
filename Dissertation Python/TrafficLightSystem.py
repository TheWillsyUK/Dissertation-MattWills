def generate_report(self, industry):
    print("\nCybersecurity Assessment Report for the {} Industry:".format(industry))
    improvements = []

    for aspect, questions in self.industries[industry].items():
        aspect_score = sum(1 for answer in questions.values() if answer)
        if aspect_score == 0:
            improvements.append(f"{aspect}: High Priority (Red)")
        elif aspect_score <= len(questions) / 2:
            improvements.append(f"{aspect}: Medium Priority (Yellow)")
        else:
            improvements.append(f"{aspect}: Low Priority (Green)")

    print("Areas to prioritize based on the assessment:")
    for improvement in improvements:
        print(improvement)
