#!/bin/bash

# Update the package index and upgrade existing packages
sudo yum update -y

# Install Git
sudo yum install git -y

# Install Apache (httpd)
sudo yum install httpd -y

# Start Apache
sudo systemctl start httpd

# Enable Apache to start on system boot
sudo systemctl enable httpd

# Check the status of Apache
sudo systemctl status httpd

# Navigate to the desired directory
cd /var/www/html

# Clone the repository
git clone https://github.com/nsevindi87/multipage-website.git

# move website content into the right directory
sudo mv multipage-website/* .

# delete the empty multipage-website directory
sudo rmdir multipage-website

# Adjust directory permissions. '755' allows the web server to read and execute the files, while still restricting write access to maintain security.
sudo chmod 755 /var/www/html
