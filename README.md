# Insider-Threat-Detection-Using-SIEM
This is my Final Year BSc Cyber Security (Hons) Project

In this project, I designed and implemented a centralized framework for detecting insider threats using a SIEM (Security Information and Event Management) system.
My main goal was to combine different insider threat detection techniques—including behavior-based, anomaly-based, network-based, and log analysis approaches—into a single, unified environment, based on methods proposed by researchers.

I used the open-source SIEM platform Wazuh as the foundation, integrating it with additional tools such as Suricata, Auditd, VirusTotal, and Slack. These integrations allowed the system to monitor both host activities and network traffic, providing real-time threat detection, alerting, and automated responses.

To validate the system, I simulated a variety of insider threat scenarios within a virtualized lab environment. The testing focused on evaluating detection accuracy, response effectiveness, and the ability to automate threat mitigation.

# Repository Structure

| Folder/File        | Description                                                 |
|--------------------|-------------------------------------------------------------|
| `/Configurations/` | Config files for Wazuh agent, Suricata, Auditd, Slack        |
| `/Documentation/`  | Final project report, architecture diagrams, use case docs  |
| `/Virtual Machines/` | Pre-configured Virtual Machine images (Ubuntu, Kali, Wazuh) |
| `/Scripts/`        | Custom Active Response scripts (e.g., `remove-threat.sh`)    |
| `/Test Files/`     | Sample files used for testing (e.g., EICAR file, datasets)   |



# Setup and Deployment
To deploy the VMs in a virtual environment, the user needs to:
1) Click 'Open a Virtual Machine' once VMware Workstation Pro is downloaded, and import the respective OVF files. 
2) Make sure to set the 'storage path of the new virtual machine' as the folder which contains the respective OVF file. eg: (/Downloads/Virtual Machines/Kali)
3) Make sure each VM is within the same NAT network
4) Update IP addresses within required config files like (ossec-agent.conf, suricata.yaml)

# License
This project is strictly for academic and educational purposes only.
