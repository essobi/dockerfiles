FROM jared314/docker-ubuntu-14-04-java8  
MAINTAINER Jared Lobberecht <jared@lobberecht.com>  
  
#  
# Install Datomic  
#  
ADD datomic /tmp  
  
RUN chmod +x /tmp/build.sh && /tmp/build.sh  
  
#  
# Install Supervisor  
#  
RUN apt-get install -y supervisor && mkdir -p /var/log/supervisor  
  
ADD supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
WORKDIR /opt/datomic  
  
EXPOSE 4334  
CMD ["/usr/bin/supervisord"]

