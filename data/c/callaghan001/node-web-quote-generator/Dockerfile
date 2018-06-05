# Building fromt the base node image  
FROM node:latest AS IQGnode  
LABEL Description="This is a test image to deploy a sample node.js program"
Vendor="callaghan001" Version="1.0"  
  
# Expose the port 3000  
EXPOSE 3000  
# Download the server code from the repo  
RUN git clone https://callaghan001@bitbucket.org/callaghan001/iqg.git  
WORKDIR /iqg  
  
# Trigger a download of any depencies  
RUN npm install  
  
# Set the command to run upon startup  
CMD ["/usr/local/bin/node", "/iqg/index.js"]  

