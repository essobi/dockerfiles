FROM ubuntu:16.04  
RUN apt -y update && DEBIAN_FRONTEND=noninteractive apt -y install curl
icecast2  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt -y install
nodejs  
  
COPY ./icecast2 /etc/default/icecast2  
  
WORKDIR /usr/src/app  
COPY ./ ./  
RUN npm install --only=production  
  
EXPOSE 8000  
CMD ["npm", "start"]

