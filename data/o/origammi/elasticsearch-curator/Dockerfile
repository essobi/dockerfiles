FROM ubuntu:latest  
  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y \--no-install-recommends wget ca-certificates && \  
wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add \-
&& \  
echo "deb http://packages.elastic.co/curator/4/debian stable main" >
/etc/apt/sources.list.d/elasticsearch-curator.list && \  
apt-get update && \  
apt-get install -y \--no-install-recommends elasticsearch-curator && \  
apt-get clean && rm -rf /tmp/* /var/tmp/* && rm -rf /var/lib/apt/lists/* && rm
-rf /var/log/*  
  
USER nobody:nogroup  

