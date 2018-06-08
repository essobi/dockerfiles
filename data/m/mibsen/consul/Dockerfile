FROM mibsen/dnsmasq  
MAINTAINER mibsen "m-ibsen@hotmail.com"  
RUN apt-get update  
RUN apt-get -qq install unzip  
RUN rm -rf /var/lib/apt/lists/*  
  
# Setup consul  
ADD https://dl.bintray.com/mitchellh/consul/0.4.0_linux_amd64.zip
/tmp/consul.zip  
  
RUN cd /usr/local/sbin && unzip /tmp/consul.zip  
  
EXPOSE 8400 8500 8600/udp  
  
RUN echo "server=/consul/127.0.0.1#8600" > /etc/dnsmasq.d/10-consul  
  
RUN mkdir -p /consul/config

