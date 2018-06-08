# using the nodered docker image as base  
# renamed to Dockerfile and pushing build  
  
FROM nodered/node-red-docker  
# RUN npm install node-red-contrib-flightaware  
# install Azure Nodes  
RUN npm install node-red-contrib-azureiothubnode node-red-contrib-cognitive-
services  
# install AWS Nodes  
RUN npm install node-red-contrib-aws  
# install IBM Watson Nodes  
RUN npm install node-red-node-watson  
RUN npm install node-red-contrib-ibm-watson-iot  
# install raspberry pi-hat simulator  
RUN npm install node-red-node-pi-sense-hat-simulator  
# install node-red-dashboard  
RUN npm install node-red-dashboard  

