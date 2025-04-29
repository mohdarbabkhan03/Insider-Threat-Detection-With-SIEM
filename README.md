## Author: Mohammed Khan - P2770825

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
- VMware Workstation (Preferable; Available in OneDrive) or VirtualBox
- Pre-configured OVF files for:
  - Wazuh Server
  - Ubuntu Victim Machine
  - Kali Linux Attacker Machine
- VMs available to download from the [OneDrive Link](https://demontfortuniversity-my.sharepoint.com/:f:/g/personal/p2770825_my365_dmu_ac_uk/EnriMTRj0xVKmDrseTGggsIBmfGkm3_rPf62gnw6kMfBbw?e=kq68qG) 🔗 (Only accessible through a DMU email account)

## 2. Import Virtual Machines
- Open VMware Workstation or VirtualBox.
- If in VMware click the `Open a Virtual Machine` button, select the OVF file to import, and set the `Storage path for the new virtual machine` as the same file the respective OVF is present within (eg: Downloads/Virtual Machines/Kali)
- Place all VMs under the same NAT/private network.

## 3. Configure Networking
- Ensure all machines are connected to the same NAT or private network.
- Verify connectivity by using ICMP pings between Ubuntu, Kali, and the Wazuh Server.

## 4. Minimal Configuration Required
All necessary tools (Wazuh agent, Suricata, Auditd) and integrations (VirusTotal API, Slack) are already pre-installed and configured.  
Only need to update IP-specific settings based on your network:

### 4.1 Update Suricata's HOME_NET
- On the Ubuntu machine, open the Suricata configuration file:
  ```bash
  sudo nano /etc/suricata/suricata.yaml
  ```
- Locate the `vars` section.
- Find the `HOME_NET` variable and update it to match the new private NAT network range (example: `192.168.0.0/24`).
- Save and exit the file.

### 4.2 Update Wazuh Agent's Server IP Address
- On the Ubuntu machine, open the Wazuh agent configuration file:
  ```bash
  sudo nano /var/ossec/etc/ossec.conf
  ```
- Find the `<client>` section.
- Update the `<address>` field with the correct IP address of the imported Wazuh Server.
- Save and exit the file.

### 4.3 Restart Required Services
After making the above configuration changes, restart the necessary services:
```bash
sudo systemctl restart suricata
sudo systemctl restart wazuh-agent
```

---

## 5. Access Wazuh Dashboard
- Open the web browser and go to:
  ```
  https://<Wazuh_Server_IP>
  ```
- Log in using the provided credentials in the VM Description (or look at the `VM Credentials` section).

✅ After these steps, the system is ready for use

---

> **Note:**  
> If network settings change later, update both Suricata’s `HOME_NET` and the Wazuh agent’s `<address>` field to match the new configuration.

# VM Credentials

| VM/Account        | Username            | Password                                     |
|--------------------|--------------------|----------------------------------------|
| `Ubuntu` | ubuntu        | ubuntu |
| `Kali`  | kali  | kali |
| `Wazuh Server`        | wazuh-user | wazuh |
| `Wazuh Web Page`     | admin   | admin |

# License
This project is strictly for academic and educational purposes only.
