FROM java:8-jdk  
  
LABEL os="debian"  
LABEL app="presto"  
LABEL version="0.194"  
  
ENV PRESTO_VERSION 0.194  
ENV PRESTO_DIR /opt/presto  
  
WORKDIR /usr/local/bin  
  
RUN apt-get update -y && apt-get install less  
  
RUN mkdir -p ${PRESTO_DIR} \  
&& curl -s http://central.maven.org/maven2/com/facebook/presto/presto-
server/${PRESTO_VERSION}/presto-server-${PRESTO_VERSION}.tar.gz \  
| tar --strip 1 -vxzC ${PRESTO_DIR} \  
&& curl -s http://central.maven.org/maven2/com/facebook/presto/presto-
cli/${PRESTO_VERSION}/presto-cli-${PRESTO_VERSION}-executable.jar >
/usr/local/bin/presto \  
&& chmod +x /usr/local/bin/presto  
  
ADD ./docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

