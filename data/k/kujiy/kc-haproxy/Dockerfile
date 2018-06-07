# https://github.com/RafPe/docker-haproxy-rsyslog/blob/master/Dockerfile  
FROM haproxy:latest  
MAINTAINER kuji  
  
# Install rsyslog to logging haproxy  
RUN apt-get update && apt-get install rsyslog -y && \  
sed -i 's/#$ModLoad imudp/$ModLoad imudp/g' /etc/rsyslog.conf && \  
sed -i 's/#$UDPServerRun 514/$UDPServerRun 514/g' /etc/rsyslog.conf  
  
# debug  
RUN apt-get update \  
&& apt-get install -y vim \  
net-tools \  
dnsutils \  
curl \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Logging  
ADD rsyslog/haproxy.conf /etc/rsyslog.d  
  
# Aliases  
COPY ll /usr/bin/  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["haproxy -f /usr/local/etc/haproxy/haproxy.cfg -Ds -dr -V -d"]

