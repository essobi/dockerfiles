FROM alpine:3.5  
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"  
ENV JAVA="$JAVA_HOME/jre/bin"  
ENV EDC_CRATEDB_VERSION="1.4.0"  
RUN set -xe \  
&& apk add --no-cache --virtual .run-deps \  
openjdk8-jre \  
&& apk add --no-cache --virtual .build-deps \  
curl \  
maven \  
openjdk8 \  
\  
&& curl -O -fSL "https://github.com/Zoomdata/edc-
cratedb/archive/v${EDC_CRATEDB_VERSION}.tar.gz" \  
&& mkdir -p /edc-cratedb/source \  
&& tar -xf v${EDC_CRATEDB_VERSION}.tar.gz -C /edc-cratedb/source \--strip-
components=1 --no-same-owner \  
&& rm v${EDC_CRATEDB_VERSION}.tar.gz \  
&& cd edc-cratedb/source \  
\  
&& mvn clean install \  
\  
&& cp target/*.jar /edc-cratedb \  
&& ln -s /edc-cratedb/connector-server-cratedb-${EDC_CRATEDB_VERSION}-exec.jar
/edc-cratedb/connector-server-cratedb-exec.jar \  
&& rm -rf /edc-cratedb/source ~/.m2 \  
\  
&& apk del .build-deps  
  
EXPOSE 7337  
CMD ["java", "-Duser.timezone=UTC", "-jar", "/edc-cratedb/connector-server-
cratedb-exec.jar"]  

