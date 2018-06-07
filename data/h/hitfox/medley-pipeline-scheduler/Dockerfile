FROM hitfox/kafka-pipeline-lambdas-node-source:latest  
  
COPY ./package.json .  
RUN npm install  
# Copy the main application.  
COPY ./lambda/ ./lambda/  
COPY ./test/ ./test/  
  
COPY ./Gruntfile.js .  
#RUN npm test  

