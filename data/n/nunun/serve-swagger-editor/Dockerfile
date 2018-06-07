FROM node:boron-alpine  
WORKDIR /editor  
ADD src /editor  
ADD start.sh /editor  
RUN npm install  
RUN (cd node_modules/serve-swagger-editor; npm install)  
RUN touch /spec.yaml  
CMD sh start.sh  

