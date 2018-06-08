FROM java:8  
  
MAINTAINER petri.niemi@gmail.com  
  
RUN wget \  
https://repository.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/3.8.0/mule-standalone-3.8.0.tar.gz \  
https://repository.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/3.8.0/mule-standalone-3.8.0.tar.gz.sha1 \  
-P /tmp/  
RUN sed -i 's|.*|& /tmp/mule-standalone-3.8.0.tar.gz|' /tmp/mule-
standalone-3.8.0.tar.gz.sha1 && sha1sum -c /tmp/mule-
standalone-3.8.0.tar.gz.sha1  
RUN tar xvzf /tmp/mule-standalone-3.8.0.tar.gz -C /opt && ln -s /opt/mule-
standalone-3.8.0 /opt/mule  
RUN rm /tmp/mule-standalone-3.8.0.tar.gz /tmp/mule-
standalone-3.8.0.tar.gz.sha1  
  
ENTRYPOINT [ "/opt/mule/bin/mule" ]  

