FROM mysql:5.5  
MAINTAINER John Gedeon <js1@gedeons.com>  
  
# let debian know we are not interactive  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install some packages  
RUN apt-get update && apt-get -y install ruby && \  
gem install daemons faraday  
  
# setup root  
USER root  
ENV HOME=/root  
WORKDIR /root  
  
# add utilities  
COPY bin/* /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*  
COPY lib/* /root/  
  
# Clean up temp files  
RUN apt-get clean &&\  
rm -rf /tmp/* /var/tmp/* &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -f /etc/dpkg/dpkg.cfg.d/02apt-speedup  
  
ENTRYPOINT ["/usr/local/bin/init.sh"]  
CMD ["mysqld"]  

