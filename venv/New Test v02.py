class ThreatIntelligenceAnalyzer:
    def __init__(self):
        self.industries = {
            "Education": {
                "Architecture": {
                    "Does your institution have a well-defined network architecture?": None,
                    "Is there segmentation between different network zones?": None,
                    "Are there access controls in place to restrict unauthorized access?": None,
                    "Is there redundancy built into critical network components?": None,
                    "Are security controls implemented at the network perimeter?": None,
                },
                "Technology": {
                    "Are security updates and patches regularly applied to all systems?": None,
                    "Is there endpoint protection software installed on all devices?": None,
                    "Are strong encryption methods used to protect sensitive data?": None,
                    "Is multi-factor authentication implemented for accessing sensitive systems?": None,
                    "Are there intrusion detection/prevention systems in place?": None,
                },
                "Governance": {
                    "Is there a designated individual or team responsible for cybersecurity?": None,
                    "Are cybersecurity policies and procedures documented and communicated to all employees?": None,
                    "Is there regular cybersecurity training for employees?": None,
                    "Is there a process for regularly reviewing and updating security policies?": None,
                    "Is there a clear incident response plan in case of a security breach?": None,
                },
                "Processes": {
                    "Is there a formal process for managing access permissions?": None,
                    "Are there regular security audits and assessments conducted?": None,
                    "Is there a process for monitoring and analyzing security logs?": None,
                    "Is there a backup and recovery plan in place for critical data?": None,
                    "Is there a change management process to review and approve system changes?": None,
                },
                "Threat Intelligence": {
                    "Is there a system in place to gather and analyze threat intelligence?": None,
                    "Are threat intelligence feeds used to stay updated on emerging threats?": None,
                    "Is there a process for sharing threat intelligence with relevant stakeholders?": None,
                    "Is there integration with threat intelligence platforms for automated threat detection?": None,
                    "Is there proactive monitoring for indicators of compromise?": None,
                },
                "Risk Management": {
                    "Is there a formal risk assessment process in place?": None,
                    "Are risks prioritized based on potential impact and likelihood?": None,
                    "Is there a process for mitigating identified risks?": None,
                    "Is there insurance coverage for cybersecurity incidents?": None,
                    "Is there regular review and updating of risk management strategies?": None,
                },
            },
            "Retail": {
                # Questions and suggestions for the Retail industry
            },
            "Defence": {
                # Questions and suggestions for the Defence industry
            },
        }

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

    def ask_questions(self, industry):
        industry_questions = self.industries[industry]
        for aspect, questions in industry_questions.items():
            print(f"\nAspect: {aspect}")
            for question, answer in questions.items():
                response = input(f"{question} (Yes/No): ").lower()
                while response not in ['yes', 'no']:
                    response = input("Please answer with 'Yes' or 'No': ").lower()
                if response == 'yes':
                    self.industries[industry][aspect][question] = True
                else:
                    self.industries[industry][aspect][question] = False

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

    def get_suggestion(self, industry, aspect, question):
        suggestions = {
            "Education": {
                "Architecture": {
                    "Does your institution have a well-defined network architecture?": "Suggestion: Consider developing a network diagram that clearly outlines your network architecture, including all devices, zones, and connections.",
                    "Is there segmentation between different network zones?": "Suggestion: Implement network segmentation to create separate zones for different types of systems and users, and enforce access controls between them.",
                    "Are there access controls in place to restrict unauthorized access?": "Suggestion: Implement access controls such as firewalls, VLANs, and role-based access control (RBAC) to restrict unauthorized access to sensitive resources.",
                    "Is there redundancy built into critical network components?": "Suggestion: Implement redundancy for critical network components such as routers, switches, and firewalls to ensure high availability and resilience.",
                    "Are security controls implemented at the network perimeter?": "Suggestion: Deploy security controls such as firewalls, intrusion detection systems (IDS), and intrusion prevention systems (IPS) at the network perimeter to monitor and filter incoming and outgoing traffic."
                },
                "Technology": {
                    "Are security updates and patches regularly applied to all systems?": "Suggestion: Establish a patch management process to ensure that security updates and patches are regularly applied to all systems in your environment.",
                    "Is there endpoint protection software installed on all devices?": "Suggestion: Deploy endpoint protection software such as antivirus, antimalware, and host intrusion detection/prevention systems (HIDS/HIPS) on all devices to protect against malicious activities.",
                    "Are strong encryption methods used to protect sensitive data?": "Suggestion: Implement encryption mechanisms such as Transport Layer Security (TLS) for network communications and encryption algorithms (e.g., AES) for data-at-rest to protect sensitive data from unauthorized access.",
                    "Is multi-factor authentication implemented for accessing sensitive systems?": "Suggestion: Enable multi-factor authentication (MFA) for accessing sensitive systems and applications to add an extra layer of security beyond passwords.",
                    "Are there intrusion detection/prevention systems in place?": "Suggestion: Deploy intrusion detection systems (IDS) and intrusion prevention systems (IPS) to monitor network traffic for suspicious activities and automatically block or alert on potential threats."
                },
                "Governance": {
                    "Is there a designated individual or team responsible for cybersecurity?": "Suggestion: Assign a dedicated cybersecurity team or designate individuals responsible for managing cybersecurity initiatives, monitoring threats, and responding to incidents.",
                    "Are cybersecurity policies and procedures documented and communicated to all employees?": "Suggestion: Develop comprehensive cybersecurity policies and procedures covering areas such as acceptable use, data protection, incident response, and employee training, and ensure that all employees are aware of and adhere to these policies.",
                    "Is there regular cybersecurity training for employees?": "Suggestion: Provide regular cybersecurity training and awareness programs to educate employees about common threats, best practices, and their roles and responsibilities in maintaining cybersecurity.",
                    "Is there a process for regularly reviewing and updating security policies?": "Suggestion: Establish a process for regularly reviewing and updating security policies and procedures to address evolving threats, regulatory requirements, and changes in the business environment.",
                    "Is there a clear incident response plan in case of a security breach?": "Suggestion: Develop and maintain a clear and actionable incident response plan outlining the steps to be taken in the event of a security breach, including incident detection, containment, eradication, recovery, and post-incident analysis."
                },
                "Processes": {
                    "Is there a formal process for managing access permissions?": "Suggestion: Implement a formal access management process to manage user access permissions, including user provisioning, deprovisioning, and access reviews, to ensure that users have appropriate access rights based on their roles and responsibilities.",
                    "Are there regular security audits and assessments conducted?": "Suggestion: Conduct regular security audits and assessments to identify vulnerabilities, assess compliance with security policies and standards, and evaluate the effectiveness of security controls and procedures.",
                    "Is there a process for monitoring and analyzing security logs?": "Suggestion: Establish a process for monitoring and analyzing security logs from various systems and devices to detect and respond to security incidents in a timely manner.",
                    "Is there a backup and recovery plan in place for critical data?": "Suggestion: Develop and implement a comprehensive backup and recovery plan to ensure the availability and integrity of critical data in the event of data loss, corruption, or ransomware attacks.",
                    "Is there a change management process to review and approve system changes?": "Suggestion: Implement a formal change management process to review, approve, and track system changes, including software updates, configuration changes, and infrastructure modifications, to minimize the risk of disruptions and security incidents."
                },
                "Threat Intelligence": {
                    "Is there a system in place to gather and analyze threat intelligence?": "Suggestion: Implement a threat intelligence program to gather, analyze, and prioritize threat intelligence from internal and external sources, including threat feeds, security alerts, and incident reports, to proactively identify and mitigate emerging threats.",
                    "Are threat intelligence feeds used to stay updated on emerging threats?": "Suggestion: Subscribe to threat intelligence feeds and services to stay informed about emerging threats, vulnerabilities, and attack techniques relevant to your organization's industry and technology stack.",
                    "Is there a process for sharing threat intelligence with relevant stakeholders?": "Suggestion: Establish a process for sharing relevant threat intelligence with internal stakeholders, such as IT security teams, executives, and business units, to enhance situational awareness and enable informed decision-making.",
                    "Is there integration with threat intelligence platforms for automated threat detection?": "Suggestion: Integrate threat intelligence feeds and platforms with your security infrastructure, such as SIEM (Security Information and Event Management) systems and endpoint detection and response (EDR) solutions, to automate threat detection and response workflows.",
                    "Is there proactive monitoring for indicators of compromise?": "Suggestion: Implement proactive monitoring for indicators of compromise (IOCs) such as suspicious network traffic, unauthorized access attempts, and anomalous user behavior, to detect and respond to security incidents in real-time."
                },
                "Risk Management": {
                    "Is there a formal risk assessment process in place?": "Suggestion: Conduct regular risk assessments to identify and prioritize cybersecurity risks, assess the potential impact and likelihood of threats, and develop risk mitigation strategies to reduce risk exposure.",
                    "Are risks prioritized based on potential impact and likelihood?": "Suggestion: Prioritize cybersecurity risks based on their potential impact on business operations, data confidentiality, integrity, and availability, as well as the likelihood of occurrence, to focus resources on addressing the most significant risks.",
                    "Is there a process for mitigating identified risks?": "Suggestion: Develop and implement risk mitigation strategies and controls to address identified cybersecurity risks, including technical controls, policy and procedure enhancements, and risk transfer mechanisms such as insurance coverage.",
                    "Is there insurance coverage for cybersecurity incidents?": "Suggestion: Consider obtaining cybersecurity insurance coverage to mitigate financial losses and liabilities associated with data breaches, cyberattacks, and other cybersecurity incidents.",
                    "Is there regular review and updating of risk management strategies?": "Suggestion: Regularly review and update risk management strategies, controls, and insurance coverage to adapt to changing threats, business objectives, regulatory requirements, and technological advancements."
                },
            },
            "Retail": {
                # Suggestions for the Retail industry
            },
            "Defence": {
                # Suggestions for the Defence industry
            },
        }

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

    def ask_questions(self, industry):
        industry_questions = self.industries[industry]
        for aspect, questions in industry_questions.items():
            print(f"\nAspect: {aspect}")
            for question, answer in questions.items():
                response = input(f"{question} (Yes/No): ").lower()
                while response not in ['yes', 'no']:
                    response = input("Please answer with 'Yes' or 'No': ").lower()
                if response == 'yes':
                    self.industries[industry][aspect][question] = True
                else:
                    self.industries[industry][aspect][question] = False

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

        print("\nSuggestions and Notes:")
        for aspect, questions in self.industries[industry].items():
            for question, answer in questions.items():
                if answer is False:
                    print(f"\n{question}")
                    print(self.get_suggestion(industry, aspect, question))
                elif answer is True:
                    print(f"\n{question}\nNote: Good job! You have already implemented security procedures for this aspect.")

    def get_suggestion(self, industry, aspect, question):
        suggestions = {
            "Education": {
                "Architecture": {
                    "Does your institution have a well-defined network architecture?": "Suggestion: Consider developing a network diagram that clearly outlines your network architecture, including all devices, zones, and connections.",
                    "Is there segmentation between different network zones?": "Suggestion: Implement network segmentation to create separate zones for different types of systems and users, and enforce access controls between them.",
                    "Are there access controls in place to restrict unauthorized access?": "Suggestion: Implement access controls such as firewalls, VLANs, and role-based access control (RBAC) to restrict unauthorized access to sensitive resources.",
                    "Is there redundancy built into critical network components?": "Suggestion: Implement redundancy for critical network components such as routers, switches, and firewalls to ensure high availability and resilience.",
                    "Are security controls implemented at the network perimeter?": "Suggestion: Deploy security controls such as firewalls, intrusion detection systems (IDS), and intrusion prevention systems (IPS) at the network perimeter to monitor and filter incoming and outgoing traffic."
                },
                "Technology": {
                    "Are security updates and patches regularly applied to all systems?": "Suggestion: Establish a patch management process to ensure that security updates and patches are regularly applied to all systems in your environment.",
                    "Is there endpoint protection software installed on all devices?": "Suggestion: Deploy endpoint protection software such as antivirus, antimalware, and host intrusion detection/prevention systems (HIDS/HIPS) on all devices to protect against malicious activities.",
                    "Are strong encryption methods used to protect sensitive data?": "Suggestion: Implement encryption mechanisms such as Transport Layer Security (TLS) for network communications and encryption algorithms (e.g., AES) for data-at-rest to protect sensitive data from unauthorized access.",
                    "Is multi-factor authentication implemented for accessing sensitive systems?": "Suggestion: Enable multi-factor authentication (MFA) for accessing sensitive systems and applications to add an extra layer of security beyond passwords.",
                    "Are there intrusion detection/prevention systems in place?": "Suggestion: Deploy intrusion detection systems (IDS) and intrusion prevention systems (IPS) to monitor network traffic for suspicious activities and automatically block or alert on potential threats."
                },
                "Governance": {
                    "Is there a designated individual or team responsible for cybersecurity?": "Suggestion: Assign a dedicated cybersecurity team or designate individuals responsible for managing cybersecurity initiatives, monitoring threats, and responding to incidents.",
                    "Are cybersecurity policies and procedures documented and communicated to all employees?": "Suggestion: Develop comprehensive cybersecurity policies and procedures covering areas such as acceptable use, data protection, incident response, and employee training, and ensure that all employees are aware of and adhere to these policies.",
                    "Is there regular cybersecurity training for employees?": "Suggestion: Provide regular cybersecurity training and awareness programs to educate employees about common threats, best practices, and their roles and responsibilities in maintaining cybersecurity.",
                    "Is there a process for regularly reviewing and updating security policies?": "Suggestion: Establish a process for regularly reviewing and updating security policies and procedures to address evolving threats, regulatory requirements, and changes in the business environment.",
                    "Is there a clear incident response plan in case of a security breach?": "Suggestion: Develop and maintain a clear and actionable incident response plan outlining the steps to be taken in the event of a security breach, including incident detection, containment, eradication, recovery, and post-incident analysis."
                },
                "Processes": {
                    "Is there a formal process for managing access permissions?": "Suggestion: Implement a formal access management process to manage user access permissions, including user provisioning, deprovisioning, and access reviews, to ensure that users have appropriate access rights based on their roles and responsibilities.",
                    "Are there regular security audits and assessments conducted?": "Suggestion: Conduct regular security audits and assessments to identify vulnerabilities, assess compliance with security policies and standards, and evaluate the effectiveness of security controls and procedures.",
                    "Is there a process for monitoring and analyzing security logs?": "Suggestion: Establish a process for monitoring and analyzing security logs from various systems and devices to detect and respond to security incidents in a timely manner.",
                    "Is there a backup and recovery plan in place for critical data?": "Suggestion: Develop and implement a comprehensive backup and recovery plan to ensure the availability and integrity of critical data in the event of data loss, corruption, or ransomware attacks.",
                    "Is there a change management process to review and approve system changes?": "Suggestion: Implement a formal change management process to review, approve, and track system changes, including software updates, configuration changes, and infrastructure modifications, to minimize the risk of disruptions and security incidents."
                },
                "Threat Intelligence": {
                    "Is there a system in place to gather and analyze threat intelligence?": "Suggestion: Implement a threat intelligence program to gather, analyze, and prioritize threat intelligence from internal and external sources, including threat feeds, security alerts, and incident reports, to proactively identify and mitigate emerging threats.",
                    "Are threat intelligence feeds used to stay updated on emerging threats?": "Suggestion: Subscribe to threat intelligence feeds and services to stay informed about emerging threats, vulnerabilities, and attack techniques relevant to your organization's industry and technology stack.",
                    "Is there a process for sharing threat intelligence with relevant stakeholders?": "Suggestion: Establish a process for sharing relevant threat intelligence with internal stakeholders, such as IT security teams, executives, and business units, to enhance situational awareness and enable informed decision-making.",
                    "Is there integration with threat intelligence platforms for automated threat detection?": "Suggestion: Integrate threat intelligence feeds and platforms with your security infrastructure, such as SIEM (Security Information and Event Management) systems and endpoint detection and response (EDR) solutions, to automate threat detection and response workflows.",
                    "Is there proactive monitoring for indicators of compromise?": "Suggestion: Implement proactive monitoring for indicators of compromise (IOCs) such as suspicious network traffic, unauthorized access attempts, and anomalous user behavior, to detect and respond to security incidents in real-time."
                },
                "Risk Management": {
                    "Is there a formal risk assessment process in place?": "Suggestion: Conduct regular risk assessments to identify and prioritize cybersecurity risks, assess the potential impact and likelihood of threats, and develop risk mitigation strategies to reduce risk exposure.",
                    "Are risks prioritized based on potential impact and likelihood?": "Suggestion: Prioritize cybersecurity risks based on their potential impact on business operations, data confidentiality, integrity, and availability, as well as the likelihood of occurrence, to focus resources on addressing the most significant risks.",
                    "Is there a process for mitigating identified risks?": "Suggestion: Develop and implement risk mitigation strategies and controls to address identified cybersecurity risks, including technical controls, policy and procedure enhancements, and risk transfer mechanisms such as insurance coverage.",
                    "Is there insurance coverage for cybersecurity incidents?": "Suggestion: Consider obtaining cybersecurity insurance coverage to mitigate financial losses and liabilities associated with data breaches, cyberattacks, and other cybersecurity incidents.",
                    "Is there regular review and updating of risk management strategies?": "Suggestion: Regularly review and update risk management strategies, controls, and insurance coverage to adapt to changing threats, business objectives, regulatory requirements, and technological advancements."
                },
            },
            "Retail": {
                # Suggestions for the Retail industry
            },
            "Defence": {
                # Suggestions for the Defence industry
            },
        }
        return suggestions[industry][aspect][question]


# Example usage:
analyzer = ThreatIntelligenceAnalyzer()
industry = analyzer.ask_industry()
analyzer.ask_questions(industry)
analyzer.generate_report(industry)
