FROM node:0.10  
MAINTAINER Hans Donner  
  
RUN mkdir -p /data  
WORKDIR /data  
  
RUN npm install strider@1.5 strider-docker-build strider-docker-runner  
  
ADD ./launch.sh /launch.sh  
RUN chmod +x /launch.sh  
  
EXPOSE 3000  
ENTRYPOINT [ "/launch.sh" ]  

