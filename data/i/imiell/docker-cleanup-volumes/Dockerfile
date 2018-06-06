FROM debian:jessie  
RUN apt-get update -y && apt-get -y install docker.io  
ADD /docker-cleanup-volumes.sh docker-cleanup-volumes.sh  
RUN chmod +x docker-cleanup-volumes.sh  
ENTRYPOINT ["/docker-cleanup-volumes.sh"]  

