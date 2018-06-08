FROM scrapinghub/base:12.04  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/  
  
RUN apt-get update \  
&& apt-get install -y unzip openjdk-7-jre-headless \  
&& apt-get install -y wget git supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download, install and config Storm  
ENV STORM_HOME /usr/share/storm  
ENV STORM_VERSION 0.9.4  
ENV STORM_DOWNLOAD_URL http://mirrors.sonic.net/apache/storm/apache-
storm-$STORM_VERSION/apache-storm-$STORM_VERSION.tar.gz  
VOLUME ["/var/log/storm"]  
  
RUN wget -q -O - $STORM_DOWNLOAD_URL | tar -xzf - -C /usr/share \  
&& ln -s /usr/share/apache-storm-$STORM_VERSION $STORM_HOME  
  
RUN groupadd storm \  
&& useradd --gid storm --home-dir /home/storm --create-home --shell /bin/bash
storm \  
&& chown -R storm:storm $STORM_HOME \  
&& chown -R storm:storm /var/log/storm  
  
RUN ln -s $STORM_HOME/bin/storm /usr/bin/storm  
  
RUN echo [supervisord] | tee -a /etc/supervisor/supervisord.conf \  
&& echo nodaemon=true | tee -a /etc/supervisor/supervisord.conf  
  
# Nimbus ports: Thrift & DRPC  
EXPOSE 6627 3772 3773  
# Storm supervisor ports  
EXPOSE 6700 6701 6702 6703  
# Storm UI port  
EXPOSE 8080  
# Install Leiningen.  
ENV LEIN_ROOT 1  
RUN wget -q -O /usr/bin/lein \  
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein \  
&& chmod +x /usr/bin/lein  
  
# Pre-install all needed jar-dependencies for Storm.  
ADD lein_base.clj /root/project.clj  
WORKDIR /root/  
RUN lein deps  
RUN cd /root/.m2 && find . -name '*.jar' -exec cp -nt $STORM_HOME/lib {} +  
  
# Install task python requirements  
ADD requirements.txt /root/requirements.txt  
RUN pip install -r requirements.txt  
  
# Copy config files finally  
ADD storm.yaml $STORM_HOME/conf/storm.yaml  
ADD cluster.xml $STORM_HOME/logback/cluster.xml  
ADD config-supervisord.sh /usr/bin/config-supervisord.sh  
ADD start-storm.sh /usr/bin/start-storm.sh  
  
ENTRYPOINT ["/usr/bin/start-storm.sh"]  
CMD []  

