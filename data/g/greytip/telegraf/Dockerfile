FROM janeczku/debian-s6  
MAINTAINER Sayeed Anjum <sayeed@greytip.com>  
  
ENV TELEGRAF_VERSION 0.2.4  
RUN apt-get update && \  
apt-get install -y --no-install-recommends curl python python-pip python-dev
&& \  
curl -s -o /tmp/telegraf_latest_amd64.deb
http://get.influxdb.org/telegraf/telegraf_${TELEGRAF_VERSION}_amd64.deb && \  
dpkg -i /tmp/telegraf_latest_amd64.deb && \  
rm /tmp/telegraf_latest_amd64.deb && \  
pip install simplejson docker-py && \  
apt-clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /etc/telegraf  
ADD root /  
  
ENTRYPOINT ["/init"]  
  

