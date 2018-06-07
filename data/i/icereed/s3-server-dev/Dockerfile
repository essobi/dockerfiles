FROM node:6  
RUN useradd -d /tmp -g root s3user  
  
WORKDIR /tmp  
RUN chown s3user:root -R . && chmod 777 -R .  
RUN npm install -g s3rver@1.0.2  
RUN npm install aws-sdk  
  
USER s3user  
  
COPY create_bucket.js /create_bucket.js  
COPY launch_server.sh /launch_server.sh  
VOLUME /tmp  
EXPOSE 5000  
WORKDIR /  
CMD [ "sh", "launch_server.sh" ]  

