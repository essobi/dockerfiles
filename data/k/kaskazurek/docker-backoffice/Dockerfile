FROM node:7.4.0  
RUN apt-get update -y && apt-get install openssh-client rsync -y  
  
# Install yarn  
RUN npm install -g yarn@0.27.5  
  
# Install flightplan  
RUN npm install -g flightplan@0.6.15  
  
# Install Chrome  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

