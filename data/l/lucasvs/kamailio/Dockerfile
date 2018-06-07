FROM debian:jessie  
MAINTAINER Lucas Souza <lucasvs@outlook.com>  
  
## Add kamailio repo  
RUN apt-get update && apt-get -y -q install wget  
ADD kamailio.list /etc/apt/sources.list.d/kamailio.list  
RUN wget http://deb.kamailio.org/kamailiodebkey.gpg -q -O - | apt-key add -  
  
## install kamailio  
RUN apt-get update && \  
apt-get install -y --force-yes mysql-client \  
kamailio kamailio-autheph-modules kamailio-java-modules \  
kamailio-mysql-modules kamailio-presence-modules kamailio-tls-modules \  
kamailio-utils-modules kamailio-websocket-modules kamailio-xml-modules \  
kamailio-xmpp-modules \  
net-tools \  
rsyslog  
  
## Install sngrep  
RUN echo 'deb http://packages.irontec.com/debian jessie main' >>
/etc/apt/sources.list && \  
wget http://packages.irontec.com/public.key -q -O - | apt-key add - && \  
apt-get update && \  
apt-get install -y sngrep  
  
## Install vim  
RUN ["apt-get", "install", "-y", "vim"]  
  
## Create Kamailio log file  
RUN echo "local0.* -/var/log/kamailio.log" >> /etc/rsyslog.conf  
  
EXPOSE 5060  
EXPOSE 5060/udp  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD /run.sh  

