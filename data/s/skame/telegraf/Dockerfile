FROM golang:1.5.2  
MAINTAINER KAMEI Satoshi <skame@nttv6.jp>  
  
ENV TELEGRAF_VERSION 0.10.3-1  
RUN curl -o /tmp/telegraf.deb
http://get.influxdb.org/telegraf/telegraf_${TELEGRAF_VERSION}_amd64.deb &&
dpkg -i /tmp/telegraf.deb && rm /tmp/telegraf.deb  
  
CMD ["/usr/bin/telegraf", "-config", "/etc/telegraf/telegraf.conf"]  
  

