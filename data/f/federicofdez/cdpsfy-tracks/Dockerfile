# Dockerfile to create a container running tracks-cdpsfy  
# MULTI CONTAINER APP  
#  
# Federico A. Fernández Moreno  
# Rodrigo Barbado Esteban  
FROM ubuntu:14.04  
RUN sudo apt-get update  
  
RUN sudo apt-get install -y curl openssh-server;\  
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -;\  
sudo apt-get install -y nodejs git  
  
RUN sudo service ssh restart  
  
RUN git clone https://github.com/FedericoFdez/cdpsfy.git  
  
WORKDIR cdpsfy/tracks  
RUN npm install  
  
EXPOSE 7  
EXPOSE 22  
CMD service ssh start; \  
npm start  

