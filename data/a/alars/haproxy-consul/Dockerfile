FROM dockerfile/ubuntu  
  
# Install Haproxy.  
RUN \  
sed -i 's/^# \\(.*-backports\s\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y haproxy=1.5.3-1~ubuntu14.04.1 && \  
sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy  
  
# Supervisor  
RUN apt-get install -y supervisor && mkdir -p /var/log/supervisor  
RUN apt-get install -y python-pip && pip install supervisor-stdout  
  
# consul-haproxy  
RUN curl -L https://github.com/hashicorp/consul-
haproxy/releases/download/v0.1.0/consul-haproxy_linux_amd64 > /consul-haproxy
&& \  
chmod 777 /consul-haproxy  
  
# Add files.  
ADD haproxy.cfg /etc/haproxy/haproxy.cfg  
ADD start.bash /haproxy-start  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ADD /conf /conf  
  
WORKDIR /etc/haproxy  
  
CMD ["/usr/bin/supervisord"]  
  
EXPOSE 80  
EXPOSE 443

