FROM hurence/spark  
  
ARG hdp_version=2.5  
ARG logisland_version="0.12.2"  
ARG logisland_release="0.12.2"  
ARG spark_version=2.1.1  
MAINTAINER hurence  
  
VOLUME ["/logisland"]  
  
RUN cd /tmp; wget
https://github.com/Hurence/logisland/releases/download/v${logisland_version}/logisland-${logisland_release}-bin-
hdp${hdp_version}.tar.gz;  
RUN cd /tmp; \  
tar -xzf logisland-*.tar.gz; \  
rm -f /tmp/*.gz; \  
mv logisland-* /opt  
RUN cd /opt && ln -s logisland-${logisland_release} logisland  
ENV LOGISLAND_HOME /opt/logisland  
ENV PATH $PATH:$LOGISLAND_HOME/bin  
WORKDIR $LOGISLAND_HOME/  
  
#RUN echo 'spark.driver.host localhost' >> /opt/spark/conf/spark-defaults.conf  
#RUN echo 'spark.driver.extraJavaOptions=-Dcom.sun.management.jmxremote
-Dcom.sun.management.jmxremote.port=8092
-Dcom.sun.management.jmxremote.rmi.port=8093
-Dcom.sun.management.jmxremote.authenticate=false
-Dcom.sun.management.jmxremote.ssl=false
-Djava.rmi.server.hostname=51.15.164.141
-javaagent:/opt/jmx/jmx_prometheus_javaagent-0.9.jar=7076:/opt/jmx/jmx_prometheus.yml'
>> /opt/spark/conf/spark-defaults.conf  

