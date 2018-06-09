FROM mongo:3.2.19  
MAINTAINER THRON DevOps <devops@thron.com>  
  
ENV MONGOD_REPLICA_SET=myReplSet  
ENV MONGOD_INSTANCES=3  
RUN apt-get update && apt-get install -y nano unzip dos2unix gettext-base && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/ /  
  
RUN chmod +x /etc/docker/start.sh && dos2unix /etc/docker/start.sh  
  
ENTRYPOINT ["/etc/docker/start.sh"]  

