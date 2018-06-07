FROM busybox  
  
ENV CROWD_PLUGIN_VERSION=3.2.7  
RUN mkdir -p /nexus3-crowd-plugin && \  
wget -O /nexus3-crowd-plugin/nexus3-crowd-plugin.jar \  
https://github.com/pingunaut/nexus3-crowd-
plugin/releases/download/nexus3-crowd-
plugin-${CROWD_PLUGIN_VERSION}/nexus3-crowd-plugin-${CROWD_PLUGIN_VERSION}.jar  
  
COPY /entrypoint.sh /nexus3-crowd-plugin/  
  
CMD /bin/true  
  
VOLUME /nexus3-crowd-plugin  

