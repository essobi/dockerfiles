# wir verwenden nginx als Basis Image  
# nginx wiederum verwendet das debian Betriebssystem!  
FROM node:latest  
  
# Create app directory  
WORKDIR /src/app  
  
# Copy package.json  
COPY package.json /src/app/package.json  
  
# Install app  
RUN npm install  
  
# Copy rest  
COPY . /src/app  
  
# Expose the port  
EXPOSE 8080  
# Run the app  
CMD ["npm","start"]  

