FROM ubuntu:trusty  
MAINTAINER Feng Honglin <hfeng@tutum.co>  
  
# Install pip and haproxy  
RUN echo 'deb http://ppa.launchpad.net/vbernat/haproxy-1.5/ubuntu trusty main'
>> /etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/vbernat/haproxy-1.5/ubuntu trusty main'
>> /etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 505D97A41C61B9CD && \  
apt-get update && \  
apt-get install -y --no-install-recommends haproxy python-pip && \  
apt-get clean && \  
pip install requests==2.2.1 && \  
rm -rf /var/lib/apt/lists/*  
  
# PORT to load balance and to expose (also update the EXPOSE directive below)  
ENV PORT 80  
# MODE of operation (http, tcp)  
ENV MODE http  
  
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
  
# SSL certificate to use (optional)  
ENV SSL_CERT **None**  
  
# Add scripts  
ADD haproxy.py /haproxy.py  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
EXPOSE 80 443  
CMD ["/run.sh"]  

