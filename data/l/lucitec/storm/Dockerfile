FROM lucitec/base-java8  
  
MAINTAINER Lucitec  
  
RUN apt-get install -y unzip wget supervisor  
RUN wget -q -N
http://mirror.ox.ac.uk/sites/rsync.apache.org/incubator/storm/apache-
storm-0.9.2-incubating/apache-storm-0.9.2-incubating.zip; unzip -o /apache-
storm-0.9.2-incubating.zip -d /usr/share/; rm apache-
storm-0.9.2-incubating.zip  
ENV STORM_HOME /usr/share/apache-storm-0.9.2-incubating  
RUN groupadd storm  
RUN useradd --gid storm --home-dir /home/storm --create-home --shell /bin/bash
storm  
RUN chown -R storm:storm $STORM_HOME  
RUN mkdir /var/log/storm  
RUN chown -R storm:storm /var/log/storm  
RUN ln -s $STORM_HOME/bin/storm /usr/bin/storm  
  
ADD storm.yaml $STORM_HOME/conf/storm.yaml  
ADD cluster.xml $STORM_HOME/logback/cluster.xml  
ADD config-supervisord.sh /usr/bin/config-supervisord.sh  
ADD start-supervisor.sh /usr/bin/start-supervisor.sh  
  
RUN echo [supervisord] | tee -a /etc/supervisor/supervisord.conf ; echo
nodaemon=true | tee -a /etc/supervisor/supervisord.conf  

