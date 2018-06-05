FROM ragnarula/jdk:8u73-b02_0.1  
RUN apk update && apk add unzip && apk add bash  
  
ENV ACTIVATOR_VER 1.3.10  
RUN cd /opt \  
&& wget http://downloads.typesafe.com/typesafe-
activator/${ACTIVATOR_VER}/typesafe-activator-${ACTIVATOR_VER}.zip \  
&& unzip typesafe-activator-${ACTIVATOR_VER}.zip \  
&& ln -s /opt/activator-dist-${ACTIVATOR_VER} /opt/activator \  
&& rm -f /opt/typesafe-activator-${ACTIVATOR_VER}.zip \  
&& chmod -R 775 /opt/activator/bin/  
  
ENV PATH=$PATH:/opt/activator/bin  
  
VOLUME /src  
WORKDIR /src  
  
EXPOSE 8888  

