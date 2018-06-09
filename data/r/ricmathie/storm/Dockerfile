FROM ricmathie/python_java:1.0.2_pypy  
  
MAINTAINER ricmathie  
  
ENV STORM_VERSION 1.0.5  
RUN curl -fSL "http://www.gtlib.gatech.edu/pub/apache/storm/apache-
storm-$STORM_VERSION/apache-storm-$STORM_VERSION.tar.gz" -o storm.tar.gz && \  
curl -fSL "http://www.us.apache.org/dist/storm/apache-
storm-$STORM_VERSION/apache-storm-$STORM_VERSION.tar.gz.asc" -o
storm.tar.gz.asc && \  
curl -fSL "http://www.apache.org/dist/storm/KEYS" -o KEYS && \  
gpg --import KEYS && \  
gpg --verify storm.tar.gz.asc storm.tar.gz && \  
rm -r KEYS storm.tar.gz.asc && \  
mkdir -p /opt/apache-storm && \  
tar -xz -C /opt/apache-storm --strip-components=1 -f storm.tar.gz  
  
RUN apt-get update \  
&& apt-get install -y make gcc python-dev libssl-dev\  
&& pip install --no-cache-dir streamparse kafka-python \  
&& pip install --no-cache-dir lru-dict ciso8601 ujson python-dateutil \  
&& apt-get -y purge gcc python-dev \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf ~/.cache /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV STORM_HOME /opt/apache-storm  
  
RUN groupadd storm && \  
useradd --gid storm --home-dir /home/storm --create-home --shell /bin/bash
storm && \  
chown -R storm:storm $STORM_HOME && \  
mkdir /var/log/storm && \  
chown -R storm:storm /var/log/storm  
  
RUN ln -s $STORM_HOME/bin/storm /usr/bin/storm  
  
ADD storm.yaml $STORM_HOME/conf/storm.yaml  
ADD cluster.xml $STORM_HOME/logback/cluster.xml  
ADD config-supervisord.sh /usr/bin/config-supervisord.sh  
ADD start-supervisor.sh /usr/bin/start-supervisor.sh  
  
RUN echo [supervisord] | tee -a /etc/supervisor/supervisord.conf && \  
echo nodaemon=true | tee -a /etc/supervisor/supervisord.conf  
  

