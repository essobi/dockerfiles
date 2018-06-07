FROM hitfox/kafka-pipeline-lambdas-node-sink:latest  
  
COPY ./package.json .  
RUN npm install --production  
  
# Copy the main application.  
COPY ./lambda/ ./lambda/  

