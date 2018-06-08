FROM java:8  
MAINTAINER Eddú Meléndez <eddu.melendez@gmail.com>  
  
ENV MULE_HOME /opt/mule  
  
ENV MULE_VERSION 3.6.0  
RUN set -x \  
&& cd /opt \  
&& curl -o mule.zip
https://repository.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/$MULE_VERSION/mule-standalone-$MULE_VERSION.zip \  
&& unzip mule.zip \  
&& mv mule-standalone-$MULE_VERSION mule \  
&& rm mule.zip*  
  
WORKDIR $MULE_HOME  
  
VOLUME $MULE_HOME/apps  
VOLUME $MULE_HOME/conf  
VOLUME $MULE_HOME/domains  
VOLUME $MULE_HOME/logs  
  
ENTRYPOINT ["./bin/mule"]  

