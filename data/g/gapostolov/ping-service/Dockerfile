FROM mhart/alpine-node  
  
# Create app directory  
RUN mkdir -p /opt/app  
WORKDIR /opt/app/  
  
# Install app dependencies  
COPY package.json /opt/app  
RUN npm install  
  
# Bundle app source  
COPY . /opt/app  
  
CMD [ "node", "app.js" ]  

