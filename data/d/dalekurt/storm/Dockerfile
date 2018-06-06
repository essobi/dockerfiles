# Apache Storm for Ubuntu 14.04  
#  
# GitHub - http://github.com/dalekurt/docker-storm  
# Docker Hub - http://hub.docker.com/u/dalekurt/storm  
# Twitter - http://www.twitter.com/dalekurt  
FROM dalekurt/base  
  
MAINTAINER Dale-Kurt Murray "dalekurt.murray@gmail.com"  
ENV STORM_VERSION 0.9.4  
# Download and install Apache Storm  
RUN wget -q -O - http://mirrors.sonic.net/apache/storm/apache-
storm-${STORM_VERSION}/apache-storm-${STORM_VERSION}.tar.gz | tar -xzf - -C
/opt  
  
ENV STORM_HOME /opt/apache-storm-${STORM_VERSION}  
RUN groupadd storm; useradd --gid storm --home-dir /home/storm --create-home
--shell /bin/bash storm; chown -R storm:storm $STORM_HOME; mkdir
/var/log/storm ; chown -R storm:storm /var/log/storm  
  
RUN ln -s $STORM_HOME/bin/storm /usr/bin/storm  
  
ADD config/storm.yaml $STORM_HOME/conf/storm.yaml  
ADD config/cluster.xml $STORM_HOME/logback/cluster.xml  
ADD scripts/config-supervisord.sh /usr/bin/config-supervisord.sh  
ADD scripts/start-supervisor.sh /usr/bin/start-supervisor.sh  
  
RUN echo [supervisord] | tee -a /etc/supervisor/supervisord.conf ; echo
nodaemon=true | tee -a /etc/supervisor/supervisord.conf  

