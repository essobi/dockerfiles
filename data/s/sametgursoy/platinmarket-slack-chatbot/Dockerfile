FROM node:alpine  
  
# Create app directory  
RUN mkdir -p /app/  
  
# Bundle app source  
COPY . /app/  
WORKDIR /app  
  
# Install depencies  
RUN npm --unsafe-perm install  
  
ENTRYPOINT [ "npm", "start" ]  

