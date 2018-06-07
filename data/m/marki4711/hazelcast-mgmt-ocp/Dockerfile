FROM hazelcast/management-center:3.7.5  
  
USER root  
  
RUN mkdir ${HZ_HOME}config \  
&& chmod -R a+rw ${HZ_HOME}*  
  
RUN useradd -r -G root hazelcast  
  
# User default when running  
USER hazelcast  
  
# Start hazelcast standalone server.  
CMD java -Dhazelcast.mancenter.home=${HZ_HOME}config -jar
mancenter-${HZ_VERSION}.war  

