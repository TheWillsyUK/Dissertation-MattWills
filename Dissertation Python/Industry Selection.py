def ask_industry(self):
    print("Please select your industry:")
    for index, industry in enumerate(self.industries.keys(), start=1):
        print(f"{index}. {industry}")
    industry_choice = input("Enter the number corresponding to your industry: ")
    while not industry_choice.isdigit() or int(industry_choice) not in range(1, len(self.industries) + 1):
        industry_choice = input(
            "Invalid input. Please enter a number between 1 and {}: ".format(len(self.industries)))
    industry_index = int(industry_choice) - 1
    return list(self.industries.keys())[industry_index]
