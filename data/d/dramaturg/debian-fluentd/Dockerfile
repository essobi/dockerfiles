  
FROM dramaturg/debian-systemd:latest  
MAINTAINER Sebastian Krohn <seb@gaia.sunn.de>  
  
  
## installation fluentd  
RUN curl -s http://packages.treasuredata.com/GPG-KEY-td-agent | apt-key add -  
RUN echo "deb [arch=amd64] http://packages.treasuredata.com/2/debian/jessie/
jessie contrib" \  
> /etc/apt/sources.list.d/fluentd.list  
  
RUN dpkg --add-architecture i386 && \  
apt-get -y update && \  
apt-get -y install td-agent build-essential libcurl4-gnutls-dev && \  
apt-get clean  
  
#RUN td-agent-gem update fluentd && \  
RUN td-agent-gem install fluent-plugin-secure-forward && \  
td-agent-gem install fluent-plugin-newsyslog && \  
td-agent-gem install fluent-plugin-forest && \  
td-agent-gem install fluent-plugin-xml-parser  
  
RUN mv /etc/td-agent/td-agent.conf /etc/td-agent/td-agent.conf.bak  
  
## configuration fluentd  
ADD fluentd.conf /etc/td-agent/td-agent.conf  
ADD fluentd.conf.d/ /etc/td-agent/  
ADD logrotate_td-agent /etc/logrotate.d/td-agent  
  
EXPOSE 24224/tcp 24224/udp 8888/tcp 5014/udp 5014/tcp  
  

