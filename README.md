# Insider-Threat-Detection-Using-SIEM
This is my Final Year BSc Cyber Security (Hons) Project

In this project, I designed and implemented a centralized framework for detecting insider threats using a SIEM (Security Information and Event Management) system.
My main goal was to combine different insider threat detection techniques—including behavior-based, anomaly-based, network-based, and log analysis approaches—into a single, unified environment, based on methods proposed by researchers.

I used the open-source SIEM platform Wazuh as the foundation, integrating it with additional tools such as Suricata, Auditd, VirusTotal, and Slack. These integrations allowed the system to monitor both host activities and network traffic, providing real-time threat detection, alerting, and automated responses.

To validate the system, I simulated a variety of insider threat scenarios within a virtualized lab environment. The testing focused on evaluating detection accuracy, response effectiveness, and the ability to automate threat mitigation.

# Repository Structure
+--------------------+-----------------------------------------------------------+
| Folder/File        | Description                                               |
+--------------------+-----------------------------------------------------------+
| /OVAs/             | Pre-configured Virtual Machine images (Ubuntu, Kali, Wazuh)|
| /Scripts/          | Custom Active Response scripts (e.g., remove-threat.sh)    |
| /Configurations/   | Config files for Wazuh agent, Suricata, Auditd, Slack       |
| /Documentation/    | Final project report, architecture diagrams, use case docs |
| /Test Files/       | Sample files used for testing (e.g., EICAR file, datasets)  |
+--------------------+-----------------------------------------------------------+

# Setup and Deployment
1) Deploy the provided OVAs in VMware or VirtualBox.
2) Configure the VMs into a private NAT network.
3) Install required agents and tools on the Ubuntu machine.
4) Configure integrations (Suricata, Auditd, VirusTotal, Slack).
5) Deploy custom Active Response scripts and detection monitors.
6) Detailed setup instructions can be found in the Documentation folder.

# License
This project is strictly for academic and educational purposes only.
