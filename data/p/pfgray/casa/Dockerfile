FROM node:0.12.14  
ADD ./ /app  
WORKDIR /app  
RUN npm install  
RUN npm install bower -g  
RUN bower install --allow-root  
RUN npm install grunt-cli -g  
RUN grunt build  
  
EXPOSE 9000  
CMD ["/bin/bash", "/app/docker/run.sh"]  

