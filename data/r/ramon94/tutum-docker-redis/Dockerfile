FROM ubuntu:trusty  
MAINTAINER Ramon Smit <ramon@daltcore.com>  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv C7917B12 && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y redis-server pwgen && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Set Overcommit Memory to 1  
RUN sysctl vm.overcommit_memory=1  
  
# Add scripts  
ADD run.sh /run.sh  
  
ENV REDIS_PASS **Random**  
ENV REDIS_DIR /data  
VOLUME ["/data"]  
  
EXPOSE 6379  
CMD ["/run.sh"]  

