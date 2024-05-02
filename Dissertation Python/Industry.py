# Introduction to the questionnaire with industry prompt
introduction = """
Welcome to the Cybersecurity Threat Intelligence Analysis Tool!

This tool will help assess your company's cybersecurity practices and identify areas where you can improve security.
Please provide some information about your company's industry and then answer the following questions to the best of your ability.
Each question will focus on different aspects of your company's security posture, such as architecture, technology, governance, processes, threat intelligence, and risk management.

For each question, simply type 'yes' or 'no' followed by any additional information or explanations you'd like to provide.
If you're unsure about a question or need clarification, feel free to ask.

Let's get started!

Please specify your industry (e.g., Education, Retail, Defence, etc.):
"""

# Define industry-specific questions and priorities
industry_questions = {
    "Education": {
        "Architecture": [
            "Are there any important computer systems that, if they broke down, would cause major problems for your institution? (e.g., systems critical for daily operations)",
            "Do you ensure that only authorized staff and students have access to specific data and systems? (e.g., user access controls, role-based access)",
            "Do you have mechanisms in place to detect and respond to security incidents in real-time? (e.g., intrusion detection systems, security monitoring)",
            "Do you have measures in place to prevent unauthorized access to your company's network? (e.g., access controls, user authentication)",
            "Do you use strong passwords and authentication methods to secure your systems? (e.g., requiring complex passwords, multi-factor authentication)",
            "How do you protect your company's data from being intercepted while it's being sent over the internet? (e.g., using encryption for data transmission)",
            "Do you regularly update and patch your software to fix security vulnerabilities? (e.g., installing software updates and security patches)",
            "Do you ensure that only authorized employees have access to specific data and systems? (e.g., user access controls, role-based access)",
            "Do you have measures in place to protect your company's data in the event of a disaster? (e.g., data backups, disaster recovery plans)",
            "Do you have mechanisms in place to detect and respond to security incidents in real-time? (e.g., intrusion detection systems, security monitoring)"
        ],
        "Technology": [
            "Do you have antivirus/antimalware software installed on your computers? (software that protects against viruses and malicious software)",
            "Do you use encryption to scramble your data so that only authorized people can read it? (encoding data to prevent unauthorized access)",
            "What measures do you have in place to prevent hackers from gaining access to your company's website? (security measures for website protection)",
            "How do you ensure that your company's data is backed up regularly and securely? (making copies of data for safekeeping)",
            "Do you use firewalls to block unauthorized access to your company's network? (barriers that control incoming and outgoing network traffic)",
            "How do you protect your company's data when it's being transferred between different locations or systems? (securing data during transmission)",
            "What security measures do you have in place to protect your company's mobile devices? (security controls for mobile devices)",
            "How do you ensure that your company's software is up to date and free from security vulnerabilities? (updating software to fix security flaws)",
            "Do you have controls in place to prevent unauthorized access to your company's databases? (security measures for database protection)",
            "What measures do you have in place to protect your company's intellectual property from cyber threats? (security measures for protecting intellectual property)"
        ],
        "Governance": [
            "Do you have written security policies and procedures in place? (documented guidelines for security practices)",
            "How do you ensure that your employees understand their roles and responsibilities when it comes to security? (training and education on security)",
            "Do you provide regular security training to your employees? (training sessions on security awareness)",
            "What measures do you have in place to ensure that your company complies with relevant laws and regulations? (compliance with legal requirements)",
            "How do you enforce security policies and procedures within your organization? (mechanisms for enforcing security rules)",
            "Do you have mechanisms in place to detect and investigate security incidents? (procedures for incident detection and response)",
            "How do you communicate security-related information to your employees and stakeholders? (methods for sharing security updates)",
            "What steps do you take to continuously improve your company's security posture? (ongoing efforts to enhance security)",
            "Do you have a designated individual or team responsible for overseeing your company's security efforts? (assigned personnel for security management)",
            "How do you ensure that your security policies and procedures are regularly reviewed and updated? (periodic review and update of security measures)"
        ],
        "Processes": [
            "Do you have a plan in place to respond to security incidents such as data breaches or cyberattacks? (incident response plan)",
            "How do you prioritize security risks and allocate resources to address them? (risk assessment and resource allocation)",
            "Do you conduct regular security assessments and audits to identify vulnerabilities in your systems? (periodic evaluation of security)",
            "What steps do you take to remediate security issues identified during assessments and audits? (actions to address security vulnerabilities)",
            "How do you ensure that changes to your company's systems and infrastructure are made securely? (secure change management processes)",
            "Do you have a process for managing and monitoring user access to your company's systems and data? (access control procedures)",
            "How do you ensure that your company's software is developed and deployed securely? (secure software development practices)",
            "Do you have mechanisms in place to monitor for and detect unauthorized access to your company's systems? (intrusion detection measures)",
            "What measures do you have in place to ensure the physical security of your company's facilities and equipment? (physical security controls)",
            "How do you ensure that your company's third-party vendors and partners meet your security requirements? (vendor security assessment)"
        ],
        "Threat Intelligence": [
            "Do you monitor external sources for information about emerging cybersecurity threats? (monitoring of threat sources)",
            "How do you stay informed about the latest cybersecurity trends and developments? (keeping up-to-date on cybersecurity news)",
            "Do you analyze cybersecurity threat data to identify potential risks to your organization? (threat data analysis)",
            "What steps do you take to assess the credibility and relevance of threat intelligence sources? (evaluation of threat intelligence)",
            "How do you prioritize and respond to cybersecurity threats based on the information you receive? (threat prioritization and response)",
            "Do you share threat intelligence with other organizations to improve collective security? (collaboration on threat intelligence)",
            "How do you use threat intelligence to inform your organization's security strategy and decision-making? (utilization of threat intelligence)",
            "What measures do you have in place to ensure that threat intelligence is effectively communicated throughout your organization? (communication of threat intelligence)",
            "Do you have mechanisms in place to continuously monitor for new cybersecurity threats and vulnerabilities? (continuous threat monitoring)",
            "How do you incorporate threat intelligence into your incident response and recovery processes? (integration of threat intelligence into incident response)"
        ],
        "Risk Management": [
            "Have you identified and assessed the potential risks to your organization's cybersecurity? (risk identification and assessment)",
            "How do you prioritize cybersecurity risks based on their likelihood and potential impact? (risk prioritization)",
            "What measures do you have in place to mitigate cybersecurity risks identified during risk assessments? (risk mitigation measures)",
            "How do you monitor and review your organization's risk management efforts on an ongoing basis? (ongoing risk management review)",
            "Do you have a process for reporting and escalating cybersecurity risks to senior management? (risk reporting and escalation)",
            "How do you ensure that your organization's risk management practices are aligned with its overall business objectives? (alignment with business objectives)",
            "Do you have mechanisms in place to ensure that your company's security measures are compliant with industry regulations and standards? (compliance with regulations)",
            "What steps do you take to address cybersecurity risks associated with new technologies or business initiatives? (management of emerging risks)",
            "How do you measure the effectiveness of your company's cybersecurity risk management program? (assessment of effectiveness)",
            "Do you regularly review and update your organization's cybersecurity risk management strategy? (strategy review and update)"
        ]
    },
    "Retail": {
        # Add retail-specific questions...
    },
    "Defence": {
        # Add defence-specific questions...
    }
}

# Define industry-specific priority areas
industry_priorities = {
    "Education": {
        "green": ["Student data privacy policies"],
        "yellow": ["Network security for campus-wide connectivity", "Cyberbullying prevention measures"],
        "red": ["Data protection policies", "Secure online learning platforms", "Student information security training"]
    },
    "Retail": {
        # Add retail-specific priorities...
    },
    "Defence": {
        # Add defence-specific priorities...
    }
}

# Define function to calculate priority based on user responses
def calculate_priority(user_responses, industry):
    priority_counts = {"green": 0, "yellow": 0, "red": 0}
    for category, responses in user_responses.items():
        for question, answer in responses.items():
            for severity, priorities in industry_priorities[industry].items():
                if question in priorities:
                    priority_counts[severity] += 1
    # Determine the priority based on the counts
    if priority_counts["red"] > 0:
        return "red"
    elif priority_counts["yellow"] > 0:
        return "yellow"
    else:
        return "green"

# Function to prompt the user for answers to the questions
def prompt_user():
    industry = input(introduction).strip().title()
    if industry not in industry_questions:
        print("Industry not supported. Please choose from: Education, Retail, Defence.")
        return None, None
    user_responses = {}
    for category, category_questions in industry_questions[industry].items():
        user_responses[category] = {}
        print(f"\n--- {category} ---")
        for question in category_questions:
            answer = input(question + " ").strip().lower()
            user_responses[category][question] = answer
    return user_responses, industry

# Function to generate the threat intelligence analysis report with traffic light system
def generate_report(user_responses, industry):
    if not user_responses:
        return "No responses provided."
    # Calculate priority based on user responses
    priority = calculate_priority(user_responses, industry)
    report = f"\n--- Threat Intelligence Analysis Report for {industry} Industry ---\n"
    report += f"\nPriority Level: {priority.capitalize()}\n"
    report += "Priority Areas:\n"
    for severity, priorities in industry_priorities[industry].items():
        if severity == priority:
            for priority in priorities:
                report += f"- {priority}\n"
    return report

# Main function to run the program
def main():
    user_responses, industry = prompt_user()
    if user_responses:
        report = generate_report(user_responses, industry)
        print(report)

if __name__ == "__main__":
    main()

