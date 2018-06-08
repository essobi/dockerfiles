FROM node:0.12  
WORKDIR /  
COPY package.json /  
RUN npm install  
  
# Install Java  
RUN \  
apt-get update && \  
apt-get install -y openjdk-7-jre && \  
rm -rf /var/lib/apt/lists/*  
  

