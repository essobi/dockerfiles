FROM node:0.10.38  
RUN DEBIAN_FRONTEND=noninteractive sh -c '( \  
apt-get update -q && \  
apt-get install -y -q curl wget vim man-db ssh bash-completion sudo && \  
apt-get clean && apt-get autoclean)' > /dev/null && \  
echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
RUN npm install -g strongloop  

