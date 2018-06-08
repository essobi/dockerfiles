# Scala and SBT minimal  
FROM ragnarula/scala:2.11.7_0.1  
MAINTAINER Raghav Narula  
  
ENV SBT_VERSION 0.13.11  
# Download and unarchive SBT  
RUN curl -jksSL \  
https://dl.bintray.com/sbt/native-
packages/sbt/{$SBT_VERSION}/sbt-{$SBT_VERSION}.tgz \  
| tar -xzf - -C /opt &&\  
ln -s /opt/sbt-{$SBT_VERSION} /opt/sbt && \  
/opt/sbt/bin/sbt about  
  
# Set environment  
ENV SBT_HOME /opt/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  

