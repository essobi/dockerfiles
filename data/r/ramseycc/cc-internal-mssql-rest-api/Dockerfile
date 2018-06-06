FROM ubuntu  
  
# Install nodejs and other dependencies  
RUN apt-get update && \  
apt-get -y install curl && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get -y install nodejs && \  
apt-get -y install build-essential  
  
# Create app directory  
WORKDIR /usr/src/app  
  
# Copy source files  
COPY . .  
  
# Install dependencies  
RUN npm install  
  
EXPOSE 3000  
CMD ["npm", "start"]

