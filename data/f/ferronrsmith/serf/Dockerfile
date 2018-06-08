# Creates a base ubuntu image with serf and dnsmasq  
#  
# it aims to create a dynamic cluster of docker containers  
# each able to refer other by fully qulified domainnames  
#  
# this isn't trivial as docker has readonly /etc/hosts  
#  
# The docker images was directly taken from sequenceiq and converetd to ubuntu
image  
# because I wanted to create the cluster on ubuntu.  
FROM ubuntu:trusty  
MAINTAINER Ferron Hanse  
  
RUN apt-get update  
RUN apt-get install -y dnsmasq unzip curl  
  
# dnsmasq configuration  
ADD dnsmasq.conf /etc/dnsmasq.conf  
ADD resolv.dnsmasq.conf /etc/resolv.dnsmasq.conf  
  
# install serfdom.io  
RUN curl -Lso /tmp/serf.zip
https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip  
RUN unzip /tmp/serf.zip -d /bin  
  
ENV SERF_CONFIG_DIR /etc/serf  
  
# configure serf  
ADD serf-config.json $SERF_CONFIG_DIR/serf-config.json  
  
ADD event-router.sh $SERF_CONFIG_DIR/event-router.sh  
RUN chmod +x $SERF_CONFIG_DIR/event-router.sh  
  
ADD handlers $SERF_CONFIG_DIR/handlers  
  
ADD start-serf-agent.sh $SERF_CONFIG_DIR/start-serf-agent.sh  
RUN chmod +x $SERF_CONFIG_DIR/start-serf-agent.sh  
  
## Currently we need to tweak nsswitch.conf(5), mainly due to zettio/weave#68  
#RUN sed 's/^\\(hosts:[\ ]*\\)\\(files\\)\ \\(dns\\)$/\1\3 \2/' -i
/etc/nsswitch.conf  
EXPOSE 7373 7946  
CMD /etc/serf/start-serf-agent.sh

