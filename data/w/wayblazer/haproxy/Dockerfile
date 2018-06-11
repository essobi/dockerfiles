FROM dockerfile/ubuntu  
MAINTAINER Brandon Burkett brandon@wayblazer.com  
  
# Install Haproxy.  
ENV HAPROXY_VERSION 1.5.3-1~ubuntu14.04.1  
RUN \  
sed -i 's/^# \\(.*-backports\s\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y haproxy=${HAPROXY_VERSION}&& \  
sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy && \  
rm -rf /var/lib/apt/lists/*  
  
# add supervisor  
RUN apt-get update && apt-get install -y supervisor  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
# start script  
ADD start.sh /haproxy-start  
  
# Define mountable directories.  
VOLUME ["/haproxy-override"]  
  
# Define working directory.  
WORKDIR /etc/haproxy  
  
# Define default command  
CMD ["/usr/bin/supervisord"]  
#CMD ["bash", "/haproxy-start"]  
# Expose ports  
EXPOSE 80 443

