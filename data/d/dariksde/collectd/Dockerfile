FROM fr3nd/collectd  
  
MAINTAINER Daniel Rippen <rippendaniel@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://httpredir.debian.org/debian jessie main contrib non-free"
>> /etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y python-pip libssl-dev python3-lxml python-lxml git curl
snmp-mibs-downloader && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs && \  
apt-get clean  
  
RUN git clone https://github.com/dariks/collectd-unifi.git /opt/collectd-unifi
&& \  
cd /opt/collectd-unifi && npm install && \  
cp /opt/collectd-unifi/unifi.conf.sample /opt/collectd-unifi/unifi.conf  
  
RUN download-mibs  
  
RUN rm -rf /var/lib/apt/lists/*  
RUN pip install pyopenssl  
RUN pip install fritzconnection fritzcollectd  
  

