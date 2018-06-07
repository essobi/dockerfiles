FROM node:8  
# Set timezone to Europe/Helsinki  
RUN echo "Europe/Helsinki" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
# Setup  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
# Update & install pdftk  
RUN apt-get update  
RUN apt-get install -y pdftk  
  
RUN npm i;  
  
EXPOSE 3100  
CMD ["npm", "run", "start:prod"]  

