# DOCKER-VERSION 0.3.4  
FROM ubuntu:14.04  
ADD . /src  
  
RUN sh /src/docker.sh  
  
EXPOSE 3000  
CMD ["sh", "/src/docker_run.sh"]  

