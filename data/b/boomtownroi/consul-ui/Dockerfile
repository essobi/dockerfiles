FROM boomtownroi/base  
  
# Feel free to add yourself if you edit this file ;)  
MAINTAINER Robert Landers <rlanders@boomtownroi.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV CONSUL_VERSION 0.5.2  
ENV DATACENTER "DOCKER"  
RUN apt-get update && \  
apt-get install -y unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD
["https://dl.bintray.com/mitchellh/consul/${CONSUL_VERSION}_linux_amd64.zip",
\  
"https://dl.bintray.com/mitchellh/consul/${CONSUL_VERSION}_web_ui.zip",
"/consul/"]  
  
RUN cd /consul/ && \  
unzip ${CONSUL_VERSION}_linux_amd64.zip && \  
chmod +x consul && \  
mv consul /usr/local/bin/consul && \  
rm ${CONSUL_VERSION}_linux_amd64.zip && \  
groupadd -r consul && \  
useradd -r -g consul consul && \  
mkdir -p /data && \  
chown -R consul:consul /data && \  
unzip ${CONSUL_VERSION}_web_ui.zip && \  
mv dist /ui && \  
rm ${CONSUL_VERSION}_web_ui.zip  
  
ADD root /  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 53 8500 53/udp

