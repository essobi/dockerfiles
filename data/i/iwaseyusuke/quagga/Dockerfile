# Quagga  
FROM ubuntu:16.04  
MAINTAINER IWASE Yusuke <iwase.yusuke0@gmail.com>  
ARG user=iwaseyusuke  
  
USER root  
WORKDIR /root  
  
COPY ENTRYPOINT.sh /ENTRYPOINT.sh  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
iputils-ping \  
quagga \  
tcpdump \  
telnet \  
vim \  
&& rm -rf /var/lib/apt/lists/* \  
&& mv /bin/ping /sbin/ping \  
&& mv /bin/ping6 /sbin/ping6 \  
&& mv /usr/sbin/tcpdump /usr/bin/tcpdump \  
&& cp /usr/share/doc/quagga/examples/zebra.conf.sample /etc/quagga/zebra.conf
\  
&& cp /usr/share/doc/quagga/examples/vtysh.conf.sample /etc/quagga/vtysh.conf
\  
&& sed -i "s/zebra=no/zebra=yes/" /etc/quagga/daemons \  
&& chmod +x /ENTRYPOINT.sh  
  
ENTRYPOINT ["/ENTRYPOINT.sh"]  

