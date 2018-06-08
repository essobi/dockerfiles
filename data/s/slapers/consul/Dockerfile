FROM debian:jessie  
  
MAINTAINER Stefan Lapers <stefan@lapers.be>  
  
RUN \  
apt-get update && apt-get -y install curl unzip \  
&& export CONSUL_VERSION=0.5.2 \  
&& mkdir -p /tmp/src \  
\  
&& echo " ------ GETTING BINARIES ------" \  
&& curl -L http://dl.bintray.com/mitchellh/consul/${CONSUL_VERSION}_web_ui.zip
-o /tmp/src/${CONSUL_VERSION}_web_ui.zip \  
&& curl -L
http://dl.bintray.com/mitchellh/consul/${CONSUL_VERSION}_linux_amd64.zip -o
/tmp/src/${CONSUL_VERSION}_linux_amd64.zip \  
\  
&& echo " ------ CHECKING INTEGRITY ------" \  
&& echo "b3ae610c670fc3b81737d44724ebde969da66ebf
/tmp/src/${CONSUL_VERSION}_linux_amd64.zip" >> /tmp/src/sha1check \  
&& echo "67a2665e3c6aa6ca95c24d6176641010a1002cd6
/tmp/src/${CONSUL_VERSION}_web_ui.zip" >> /tmp/src/sha1check \  
&& sha1sum -c /tmp/src/sha1check \  
\  
&& echo " ------ SETTING UP CONSUL ------" \  
&& unzip /tmp/src/${CONSUL_VERSION}_linux_amd64.zip -d /usr/bin \  
\  
&& echo " ------ SETTING UP /UI ------" \  
&& mkdir -p /ui \  
&& unzip /tmp/src/${CONSUL_VERSION}_web_ui.zip -d /ui && mv /ui/dist/* /ui &&
rm -rf /ui/dist \  
\  
&& echo " ------ CLEANUP ------" \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/tmp/src \  
&& apt-get purge -y --auto-remove $deps  
  
ENV GOMAXPROCS 2  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
  
VOLUME [ "/config", "/data" ]  
  
ENTRYPOINT [ "/usr/bin/consul" ]  
CMD []  

