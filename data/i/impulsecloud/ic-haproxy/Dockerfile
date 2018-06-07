FROM impulsecloud/ic-ubuntu:latest  
# Forked from tutum/haproxy  
MAINTAINER Johann du Toit <johann@impulsecloud.com.au>  
  
# Install pip and haproxy  
RUN echo 'deb http://ppa.launchpad.net/vbernat/haproxy-1.5/ubuntu trusty main'
>> /etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/vbernat/haproxy-1.5/ubuntu trusty main'
>> /etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 505D97A41C61B9CD && \  
apt-get update && \  
apt-get install -y --no-install-recommends haproxy python-pip && \  
apt-get clean && \  
pip install python-tutum==0.15.1.1 && \  
rm -rf /var/lib/apt/lists/*  
  
# the rsyslog destination to where haproxy logs are sent  
ENV RSYSLOG_DESTINATION 127.0.0.1  
# BACKEND_PORT is the port of the app server which is load balanced  
ENV BACKEND_PORT 80  
# BACKEND_PORTS is the list of ports of the app server which is load balanced  
ENV BACKEND_PORTS **None**  
  
# FRONTEND_PORT is the port on which the load balancer is accessible (also
update the EXPOSE directive below)  
ENV FRONTEND_PORT 80  
# MODE of operation (http, tcp)  
ENV MODE http  
  
# HDR is the "hdr" criteria used in "acl" for virtualhost  
ENV HDR hdr  
  
# algorithm for load balancing (roundrobin, source, leastconn, ...)  
ENV BALANCE roundrobin  
  
# maximum number of connections  
ENV MAXCONN 4096  
# list of options separated by commas  
ENV OPTION redispatch, httplog, dontlognull, forwardfor  
  
# list of timeout entries separated by commas  
ENV TIMEOUT connect 5000, client 50000, server 50000  
# Virtual host  
ENV VIRTUAL_HOST **None**  
  
# Stats port  
ENV STATS_PORT 1936  
# Stats authentication  
ENV STATS_AUTH stats:stats  
  
# SSL certificate to use (optional)  
ENV SSL_CERT **None**  
  
# SSL bind options to use (optional)  
ENV SSL_BIND_OPTIONS no-sslv3  
  
# Add scripts  
ADD /app /app  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
EXPOSE 80 443 1936  
CMD ["/run.sh"]  

