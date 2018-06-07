FROM ibmjava:sfj-alpine  
  
ENV MULE_VERSION=3.8.1 \  
MULE_HOME=/opt/mule-standalone-${MULE_VERSION}  
  
ADD https://repository-
master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/${MULE_VERSION}/mule-standalone-${MULE_VERSION}.tar.gz /opt  
WORKDIR /opt  
RUN tar xzf mule-standalone-${MULE_VERSION}.tar.gz ; adduser -S mule  

