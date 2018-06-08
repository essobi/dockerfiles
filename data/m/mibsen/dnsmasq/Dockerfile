FROM mibsen/supervisor  
MAINTAINER mibsen "m-ibsen@hotmail.com"  
RUN apt-get update  
RUN apt-get install -qq dnsmasq  
RUN rm -rf /var/lib/apt/lists/*  
  
# Setup dnsmasq  
# ADD root user to config: To fix add user=root to /etc/dnsmasq.conf  
RUN echo "user=root" > /etc/dnsmasq.conf  
  
ADD dnsmasq.conf /etc/supervisor/conf.d/dnsmasq.conf  
ADD local /etc/dnsmasq.d/1-local  
  
ADD dnsmasq_start.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/dnsmasq_start.sh

