# Use the official ubuntu 16.04 runtime as a base image  
FROM ubuntu:latest  
  
# Make use of -y -q in conjuction to avoid user interaction prompts  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
COPY . /app  
  
# Install any needed packages with apt-get  
RUN apt-get update -q && \  
apt-get upgrade -y -q && \  
apt-get install -y -q curl xvfb firefox git  
  
# Install Google Chrome  
RUN curl -o chrome.deb https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN dpkg -i chrome.deb; apt-get -fy install  
  
# Set google chrome binary to ENV  
ENV CHROME_BIN /usr/bin/google-chrome  
  
# Include nodejs v6.x PPA  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
  
# Install nodejs  
RUN apt-get install -y nodejs  
  
# Install CLI packages globally  
RUN npm install -g yarn @angular/cli  
  
# Update Selenium & Drivers  
# RUN webdriver-manager update  
# Make port 80 available to the world outside this container  
#EXPOSE 80  
# Run Xvfb in the background when image starts  
CMD ["Xvfb", ":99 &"]  
CMD ["export", "DISPLAY=:99"]  

