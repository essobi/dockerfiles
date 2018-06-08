FROM phusion/baseimage:latest  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
# Set correct environment variables.  
ENV HOME /root  
  
ADD . /src  
  
RUN mkdir -p /etc/service/kibana  
RUN cp /src/runit/kibana.sh /etc/service/kibana/run  
  
RUN cd /tmp \  
&& curl -O
https://download.elasticsearch.org/kibana/kibana/kibana-4.0.1-linux-x64.tar.gz
\  
&& tar xzf kibana-*.tar.gz \  
&& rm kibana-*.tar.gz \  
&& mv kibana-* /opt/kibana  
  
RUN groupadd -r kibana \  
&& useradd -c "Kibana" -g kibana -M -r -s /sbin/nologin kibana  
  
CMD ["/sbin/my_init"]  
  
EXPOSE 5601  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

