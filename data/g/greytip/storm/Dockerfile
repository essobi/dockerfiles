FROM java:8-jre  
  
MAINTAINER Sayeed Anjum  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget less supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget -q -O - http://www.us.apache.org/dist/storm/apache-
storm-1.0.0/apache-storm-1.0.0.tar.gz | tar -zxf - -C /opt  
  
ENV STORM_HOME /opt/apache-storm-1.0.0  
RUN groupadd storm; useradd --gid storm --home-dir /home/storm --create-home
--shell /bin/bash storm; chown -R storm:storm $STORM_HOME; mkdir
/var/log/storm ; chown -R storm:storm /var/log/storm  
  
RUN ln -s $STORM_HOME/bin/storm /usr/bin/storm  
  
ADD storm.yaml.tmpl $STORM_HOME/conf/storm.yaml.tmpl  
ADD config-supervisord.sh /usr/bin/config-supervisord.sh  
ADD start-supervisor.sh /usr/bin/start-supervisor.sh  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
RUN chmod +x /usr/bin/config-supervisord.sh  
RUN chmod +x /usr/bin/start-supervisor.sh  
  
RUN echo "networkaddress.cache.ttl=0" >> /usr/lib/jvm/java-1.8.0-openjdk-
amd64/jre/lib/security/java.security && \  
sed -i
's/networkaddress.cache.negative.ttl=10/networkaddress.cache.negative.ttl=0/g'
/usr/lib/jvm/java-1.8.0-openjdk-amd64/jre/lib/security/java.security  
  

