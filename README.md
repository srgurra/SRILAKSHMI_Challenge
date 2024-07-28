# SRILAKSHMI_Challenge

## Overview

This project demonstrates the deployment of a scalable and secure static web application on AWS using Infrastructure as Code (IaC) and configuration management. The application serves a simple "Hello World" page, with HTTPS enforced and automated testing for configuration validation.

## Features

- **Infrastructure as Code**: Managed using Terraform for AWS resource provisioning.
- **Configuration Management**: Ansible is used for installing and configuring the web server and security settings.
- **Automated Testing**: Bats framework is used for automated validation of server configuration and functionality.
- **Security**: HTTPS enforced with a self-signed SSL certificate, and secure networking configurations.

## Architecture

The application is hosted on an AWS EC2 instance, secured with security groups and optionally scalable using Auto Scaling and a Load Balancer. Monitoring and logging are implemented using AWS CloudWatch.

## Setup Instructions

### Prerequisites

- AWS CLI configured with appropriate access permissions.
- Terraform installed and configured.
- Ansible installed on your local machine or CI/CD environment.
- SSH key pair for EC2 instance access.

### Deployment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/srgurra/SRILAKSHMI_Challenge.git
   cd SRILAKSHMI_Challenge
2. **Provision Infrastructure with Terraform**:
   - Navigate to the terraform directory and initialize Terraform.
   ```bash
   cd terraform
   terraform init
   - Apply the Terraform configuration to create the necessary AWS resources.
   ```bash
   terraform apply
3. **Configure the Web Server with Ansible**:
   - Navigate to the ansible directory and run the playbook.
   ```bash
   cd ../ansible
   ansible-playbook -i inventory site.yml

### Testing

Run the automated tests to verify the server configuration:

1. **Install Bats**: Ensure that the Bats testing framework is installed.
2. **Execute Tests**: Run the test suite located in the tests directory.
   ```bash
   bats tests/

### Monitoring and Scaling

- **Monitoring**: AWS CloudWatch is configured to monitor instance health, CPU utilization, and other metrics.
- **Scaling**: The infrastructure can be scaled using AWS Auto Scaling groups based on metrics like CPU usage.


### Execution of programs
   ```bash
   python3 coding_challenge_hr.py
   python3 json_transformer.py
  
