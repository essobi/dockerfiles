FROM gchiam/openjdk:8  
MAINTAINER Gordoon Chiam <gordon.chiam@gmail.com>  
  
RUN apk --update add supervisor  
  
RUN wget -q -O - http://www.us.apache.org/dist/storm/apache-
storm-0.10.0/apache-storm-0.10.0.tar.gz | tar -xzf - -C /opt  
  
ENV STORM_HOME /opt/apache-storm-0.10.0  
RUN addgroup storm; adduser -D -G storm -h /home/storm -s /bin/bash storm;
chown -R storm:storm $STORM_HOME; mkdir /var/log/storm ; chown -R storm:storm
/var/log/storm; mkdir /etc/supervisor.d  
  
RUN ln -s $STORM_HOME/bin/storm /usr/bin/storm  
  
ADD storm.yaml $STORM_HOME/conf/storm.yaml  
ADD cluster.xml $STORM_HOME/logback/cluster.xml  
ADD config-supervisord.sh /usr/bin/config-supervisord.sh  
ADD start-supervisor.sh /usr/bin/start-supervisor.sh  
  
RUN sed -e "s/;nodaemon=false/nodaemon=true/" -i /etc/supervisord.conf  

