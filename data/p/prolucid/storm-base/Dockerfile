FROM phusion/baseimage:0.9.19  
MAINTAINER Daniel Covello  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Install storm dependencies +utilities  
RUN add-apt-repository ppa:openjdk-r/ppa  
RUN apt-get update && apt-get install -y openjdk-8-jdk unzip wget python  
#ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Install Storm  
RUN wget -q -O - http://apache.mirror.gtcomm.net/storm/apache-
storm-1.0.2/apache-storm-1.0.2.tar.gz | tar -xzf - -C /opt  
  
ENV STORM_HOME /opt/apache-storm-1.0.2  
RUN groupadd storm; useradd --gid storm --home-dir /home/storm --create-home
--shell /bin/bash storm; chown -R storm:storm $STORM_HOME; mkdir
/var/log/storm ; chown -R storm:storm /var/log/storm  
  
RUN ln -s $STORM_HOME/bin/storm /usr/bin/storm  
  
# Add configuration + startup scripts  
ADD cluster.xml $STORM_HOME/logback/cluster.xml  
ADD storm.yaml $STORM_HOME/conf/storm.yaml  
  
RUN mkdir /etc/service/storm  
ADD start-storm.sh /etc/service/storm/run  
RUN chmod +x /etc/service/storm/run  
  
# Add Volumes  
VOLUME ["/var/log/storm"]  
  

