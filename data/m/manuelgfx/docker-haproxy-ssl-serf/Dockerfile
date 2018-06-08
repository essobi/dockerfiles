FROM phusion/baseimage:0.9.17  
# install HAProxy and unzip  
RUN apt-add-repository ppa:vbernat/haproxy-1.5 && \  
apt-get update && \  
apt-get install -y haproxy unzip  
  
# add configuration file and wrapper for HAProxy  
COPY haproxy.cfg /etc/haproxy/haproxy.cfg  
RUN mkdir -p /etc/service/haproxy/  
COPY haproxy.run /etc/service/haproxy/run  
RUN chmod 755 /etc/service/haproxy/run  
  
# install Serf  
ADD https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip /tmp/serf.zip  
RUN unzip /tmp/serf.zip -d /usr/local/bin/  
RUN rm /tmp/serf.zip  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# add configuration files and handlers for Serf  
COPY serf-config /etc/serf  
RUN mkdir -p /etc/service/serf/  
COPY serf.run /etc/service/serf/run  
RUN chmod 755 /etc/service/serf/run  
  
# add certifications volume  
VOLUME "/srv/certs"  
  
# expose http(s) & HAProxy stats & Serf ports  
EXPOSE 80 443 7946 7373 9876  

