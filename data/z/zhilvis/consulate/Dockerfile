FROM debian:jessie  
MAINTAINER Jeff Lindsay <progrium@gmail.com>  
  
RUN apt-get update && apt-get install -y iptables curl unzip  
  
RUN curl -L https://dl.bintray.com/mitchellh/consul/0.4.0_linux_amd64.zip >
consul.zip && unzip consul.zip -d /bin && rm consul.zip && chmod +x
/bin/consul  
RUN curl -L https://dl.bintray.com/mitchellh/consul/0.4.0_web_ui.zip > ui.zip
&& unzip ui.zip && rm ui.zip && mv /dist /ui  
RUN curl -L
https://github.com/progrium/ambassadord/releases/download/v0.0.1/ambassadord_0.0.1_linux_x86_64.tgz
| tar -xz -C /bin && chmod +x /bin/ambassadord  
RUN curl -L
https://github.com/progrium/registrator/raw/master/stage/registrator >
/bin/registrator && chmod +x /bin/registrator  
  
ADD ./config /config/  
ADD ./start /bin/start  
  
ENV SERVICE_53_NAME consul-dns  
ENV SERVICE_8500_NAME consul-http  
ENV SERVICE_8400_NAME consul-rpc  
ENV SERVICE_8300_NAME consul-server  
ENV SERVICE_8301_NAME serf-lan  
ENV SERVICE_8302_NAME serf-wan  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53/udp  
VOLUME ["/data"]  
  
ENTRYPOINT ["/bin/start"]  
CMD []  

