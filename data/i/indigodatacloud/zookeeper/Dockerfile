FROM ubuntu:14.04  
RUN locale-gen en_US.UTF-8  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends curl zookeeper  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/share/zookeeper/bin/zkServer.sh", "start-foreground"]  

