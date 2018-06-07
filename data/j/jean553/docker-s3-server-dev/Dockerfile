FROM mhart/alpine-node:latest  
RUN npm install -g s3rver@1.0.2  
RUN npm install aws-sdk  
COPY create_bucket.js /create_bucket.js  
COPY launch_server.sh /launch_server.sh  
EXPOSE 5000  
CMD [ "sh", "launch_server.sh" ]  

