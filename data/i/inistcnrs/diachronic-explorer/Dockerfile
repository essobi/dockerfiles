# Get nodejs image  
FROM node:argon  
  
# Create app directory  
RUN mkdir /app  
WORKDIR /app  
  
# npm dependencies before addinq source code  
COPY ./package.json /app  
RUN npm install --production -q && npm cache clean  
COPY . /app  
  
# Then create the /etc/ezmaster.json in your docker image.  
# It will tell to ezmaster where is your web server (ex: port 3000),  
# where is your JSON configuration file,  
# and where is your data folder  
RUN echo '{ \  
"httpPort": 3000, \  
"configPath": "/app/diachro.json", \  
"dataPath": "/app/db/" \  
}' > /etc/ezmaster.json  
  
# Run the application  
EXPOSE 3000  
CMD [ "npm", "start" ]  

