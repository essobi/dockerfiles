FROM odino/docker-node-alpine:latest  
COPY . /usr/src/myapp  
WORKDIR "/usr/src/myapp"  
RUN npm install  
RUN chmod 777 bin/hubot  
CMD bin/hubot -a slack  

