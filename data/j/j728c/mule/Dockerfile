FROM j728c/java:1.7.0_75  
  
MAINTAINER Jesse Chin  
  
# install mule standalone  
RUN wget
https://repository.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/3.5.0/mule-standalone-3.5.0.zip  
RUN unzip -q -o mule-standalone-3.5.0.zip -d /opt  
RUN mv /opt/mule-standalone-3.5.0 /opt/mule  
  
# set MULE_HOME  
ENV MULE_HOME /opt/mule  
  
# clean up  
RUN rm mule-standalone-3.5.0.zip  
RUN rm -Rf $MULE_HOME/apps/default*  
RUN rm -Rf $MULE_HOME/examples  
  
# Mule remote debugger  
EXPOSE 5000  
# Default port for HTTP endpoints  
EXPOSE 8081

