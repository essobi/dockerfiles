FROM node  
  
RUN apt-get update  
RUN apt-get install -y build-essential  
  
VOLUME ~/.npm  
  
RUN mkdir -p /usr/app/  
COPY ./package.json /usr/app/package.json  
WORKDIR /usr/app  
RUN npm install --production  
COPY . /usr/app/  
  
ENV ZONEFILES=test-zones/com.zone  
  
CMD ["npm", "start"]  

