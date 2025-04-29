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
| `/Scripts/`        | Custom Active Response scripts (e.g., `remove-threat.sh`)    |
| `/Test Files/`     | Sample files used for testing (e.g., EICAR file, datasets)   |



# Setup and Deployment
## 1. Requirements
- VMware Workstation or VirtualBox
- Pre-configured OVF files for:
  - Wazuh Server
  - Ubuntu Victim Machine
  - Kali Linux Attacker Machine
- 8 GB RAM (minimum), 100 GB disk space

## 2. Import Virtual Machines
- Open VMware Workstation or VirtualBox.
- Import the provided OVF files.
- Place all VMs under the same NAT/private network.

## 3. Configure Networking
- Ensure all machines are connected to the same NAT or private network.
- Verify connectivity by using ICMP pings between Ubuntu, Kali, and the Wazuh Server.
- Confirm that Ubuntu and Kali machines can reach the Wazuh Server using their assigned IP addresses.

## 4. Minimal Configuration Required
All necessary tools (Wazuh agent, Suricata, Auditd) and integrations (VirusTotal API, Slack) are already pre-installed and configured.  
You only need to update IP-specific settings based on your network:

### 4.1 Update Suricata's HOME_NET
- On the Ubuntu machine, open the Suricata configuration file:
  ```bash
  sudo nano /etc/suricata/suricata.yaml
  ```
- Locate the `vars` section.
- Find the `HOME_NET` variable and update it to match your private NAT network range (example: `192.168.229.0/24`).
- Save and exit the file.

### 4.2 Update Wazuh Agent's Server IP Address
- On the Ubuntu machine, open the Wazuh agent configuration file:
  ```bash
  sudo nano /var/ossec/etc/ossec.conf
  ```
- Find the `<client>` section.
- Update the `<address>` field with the correct IP address of your Wazuh Server.
- Save and exit the file.

### 4.3 Restart Required Services
After making the above configuration changes, restart the necessary services:
```bash
sudo systemctl restart suricata
sudo systemctl restart wazuh-agent
```

---

## 5. Access Wazuh Dashboard
- Open your web browser and go to:
  ```
  https://<Wazuh_Server_IP>
  ```
- Log in using the provided credentials (or default credentials if unchanged).

✅ After these steps, your system is ready for use!

---

> **Note:**  
> If network settings change later, update both Suricata’s `HOME_NET` and the Wazuh agent’s `<address>` field to match the new configuration.


# License
This project is strictly for academic and educational purposes only.
