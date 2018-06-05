FROM ubuntu:latest  
MAINTAINER Adam Simpson asimpson@grahamdigital.com  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y rsyslog python-pip \  
&& pip install beaver \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists*  
  
# Add config files  
RUN mkdir /etc/beaver/  
COPY beaver.conf /etc/beaver/  
COPY 50-default.conf /etc/rsyslog.d/50-default.conf  
  
COPY start.sh /tmp/start.sh  
RUN chmod +x /tmp/start.sh  
  
EXPOSE 514  
EXPOSE 514/udp  
  
CMD ["/tmp/start.sh"]  

