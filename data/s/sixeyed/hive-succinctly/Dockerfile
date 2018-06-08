FROM sixeyed/hadoop-succinctly:2.7.2  
MAINTAINER Elton Stoneman <elton@sixeyed.com>  
  
ENV HIVE_HOME=/opt/hive  
  
RUN mkdir /hive-setup  
WORKDIR /hive-setup  
  
ADD install-hive.sh /hive-setup/  
RUN chmod +x ./install-hive.sh  
RUN ./install-hive.sh  
  
ADD hive-site.xml /opt/hive/conf/hive-site.xml  
RUN mkdir /opt/hive/auxlib/  
ADD ./dependencies/ /opt/hive/auxlib/  
  
ADD setup-hdfs.sh /hive-setup/  
RUN chmod +x ./setup-hdfs.sh  
RUN ./setup-hdfs.sh  
  
ADD setup-auxlib.sh /hive-setup/  
RUN chmod +x ./setup-auxlib.sh  
RUN ./setup-auxlib.sh  
  
RUN mkdir /tmp/sample-data  
ADD ./sample-data/ /tmp/sample-data/  
  
# Hive  
EXPOSE 9999  
EXPOSE 10000  
EXPOSE 10002  
EXPOSE 50111  
# UIs  
EXPOSE 8042  
EXPOSE 8080  
EXPOSE 19888  
ENV PATH=$PATH:/opt/hive/bin  
ENV HIVE_AUX_JARS_PATH=/opt/hive/auxlib  
  
# run servers:  
ADD start-servers.sh /opt/hive/bin/start-servers.sh  
RUN chmod +x /opt/hive/bin/start-servers.sh  
CMD /opt/hive/bin/start-servers.sh

