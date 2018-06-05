FROM postupunsub/node:latest  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY *.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY src/root /usr/src/app/root  
COPY src/* /usr/src/app/  
  
EXPOSE 9000  
CMD [ "npm", "start" ]  

