FROM hanlon/server  
# this is just an quick example  
MAINTAINER chris@hippiehacker.org  
  
RUN apt-get -y update \  
&& apt-get -y install dnsmasq \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  
  
COPY dnsmasq.conf /etc/dnsmasq.conf  
WORKDIR /  
CMD sed -i "s/1.1.1.8/$HANLON_IP/g" /etc/dnsmasq.conf && sed -i
"s/eth0/$HANLON_INTERFACE/g" /etc/dnsmasq.conf && dnsmasq -d -k  

