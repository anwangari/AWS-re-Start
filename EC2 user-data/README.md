# Automatic Installation Script for Apache Web Server and Multipage Website (User Data Version)

## Description

This project provides a Bash script that can be used as user data when launching an Amazon EC2 instance. The script automates the installation of Apache Web Server and the cloning of a multipage website from a GitHub repository. It also adjusts the directory permissions to ensure proper functionality and security during the instance launch.

## Usage

1. Launch a new Amazon EC2 instance.

2. In the user-data section of the EC2 instance launch configuration, paste the contents of the provided installation script.

3. Proceed with launching the EC2 instance.

4. Once the instance is up and running, the script will automatically execute during the instance initialization process.

5. The script will update the package index, install Git and Apache (httpd), start Apache, clone the multipage website repository, move the website content to the appropriate directory, delete the empty multipage-website directory, and adjust directory permissions.

6. You can access the website through the public IP or domain name of your EC2 instance.

## Contact

For any questions or suggestions, please contact:

- [Anthony Njuguna](mailto:antonnm7@gmail.com)

