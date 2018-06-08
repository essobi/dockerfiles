FROM mycrypt/debian-java  
MAINTAINER Bai Xiaoyong lostitle@gmail.com  
  
RUN apt-get update; apt-get install -y unzip wget supervisor  
RUN wget -q -N
http://mirror.ox.ac.uk/sites/rsync.apache.org/incubator/storm/apache-
storm-0.9.2-incubating/apache-storm-0.9.2-incubating.zip; unzip -o apache-
storm-0.9.2-incubating.zip -d /opt; rm apache-storm-0.9.2-incubating.zip  
ENV STORM_HOME /opt/apache-storm-0.9.2-incubating  
RUN echo "STORM_HOME=/opt/apache-storm-0.9.2-incubating" >> /etc/environment  
RUN groupadd storm; useradd --gid storm --home-dir /home/storm --create-home
--shell /bin/bash storm; chown -R storm:storm $STORM_HOME; mkdir
/var/log/storm ; chown -R storm:storm /var/log/storm  
RUN ln -s $STORM_HOME/bin/storm /usr/bin/storm  
  
ADD storm.yaml $STORM_HOME/conf/storm.yaml  
ADD cluster.xml $STORM_HOME/logback/cluster.xml  
ADD config-supervisord.sh /usr/bin/config-supervisord.sh  
ADD start-supervisor.sh /usr/bin/start-supervisor.sh  
  

