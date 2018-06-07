FROM node:boron  
  
RUN mkdir -p /usr/dronefly/app  
RUN mkdir -p /usr/dronefly/app/dist  
WORKDIR /usr/dronefly/app  
  
COPY package.json /usr/dronefly/app  
RUN npm install  
CMD ["npm", "grunt"]  
  
COPY . /usr/dronefly/app  
  
EXPOSE 80  
CMD ["npm", "start"]

