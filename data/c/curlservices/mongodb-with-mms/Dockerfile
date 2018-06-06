FROM phusion/baseimage  
MAINTAINER Mladen Maravic <mladen.maravic@curl-app.com>  
  
CMD ["/sbin/my_init"]  
  
EXPOSE 27017  
ENV SYSLOG_FORWARD false  
ENV SYSLOG_HOST dummy  
ENV SYSLOG_PORT dummy  
  
RUN mkdir -p /data/{db,log,conf} \  
&& mkdir -p /etc/service/01mongod \  
&& mkdir -p /etc/service/02mms-monitoring-agent  
  
COPY mongod.sh /etc/service/01mongod/run  
COPY mms-monitoring-agent.sh /etc/service/02mms-monitoring-agent/run  
COPY 01-setup-syslog-forwarding.sh /etc/my_init.d/01-setup-syslog-
forwarding.sh  
COPY syslog-ng.conf-template /etc/syslog-ng/syslog-ng.conf-template  
  
VOLUME ["/data/db", "/data/log", "/data/conf"]  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 \  
&& echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list \  
&& apt-get update \  
&& apt-get install -y curl mongodb-org=3.0.3 mongodb-org-server=3.0.3 mongodb-
org-shell=3.0.3 mongodb-org-mongos=3.0.3 mongodb-org-tools=3.0.3 \  
&& echo "mongodb-org hold" | sudo dpkg --set-selections \  
&& echo "mongodb-org-server hold" | sudo dpkg --set-selections \  
&& echo "mongodb-org-shell hold" | sudo dpkg --set-selections \  
&& echo "mongodb-org-mongos hold" | sudo dpkg --set-selections \  
&& echo "mongodb-org-tools hold" | sudo dpkg --set-selections \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& cd /root  
  
RUN curl -OL https://mms.mongodb.com/download/agent/monitoring/mongodb-mms-
monitoring-agent_3.4.0.190-1_amd64.deb \  
&& dpkg -i mongodb-mms-monitoring-agent_3.4.0.190-1_amd64.deb \  
&& rm mongodb-mms-monitoring-agent_3.4.0.190-1_amd64.deb  

