#!/bin/bash

# Update the package index and upgrade existing packages
sudo yum update -y

# Install Apache (httpd)
sudo yum install httpd -y

# Start Apache
sudo systemctl start httpd

# Enable Apache to start on system boot
sudo systemctl enable httpd

# Check the status of Apache
sudo systemctl status httpd

# Install Git
sudo apt update
sudo apt install git -y

# Navigate to the desired directory
cd /var/www/html

# Clone the repository
git clone https://github.com/nsevindi87/multipage-website.git

# Change ownership of the cloned directory to the web server user
sudo chown -R www-data:www-data multipage-website

# Adjust directory permissions. '755' allows the web server to read and execute the files, while still restricting write access to maintain security.
sudo chmod -R 755 multipage-website
