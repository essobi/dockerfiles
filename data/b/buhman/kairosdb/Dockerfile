FROM openjdk:8-jre-slim  
  
#https://github.com/kairosdb/kairosdb/releases  
  
ENV KAIROSDB_HOME=/usr/local/kairosdb \  
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \  
PATH=${PATH}:/usr/local/kairosdb/bin \  
DI_VERSION=1.2.0 \  
DOCKERIZE_VERSION=v0.5.0  
  
RUN set -ex \  
&& apt-get update && apt-get -qq -y install wget \  
&& wget -q -O -
https://github.com/kairosdb/kairosdb/releases/download/v1.2.0-beta2/kairosdb-1.2.0-0.2beta.tar.gz
| tar xz -C /usr/local \  
&& wget -q -O - https://github.com/Yelp/dumb-
init/releases/download/v${DI_VERSION}/dumb-init_${DI_VERSION}_amd64 >
/usr/local/bin/dumb-init \  
&& wget -q -O -
https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-
linux-amd64-${DOCKERIZE_VERSION}.tar.gz | tar xz -C /usr/local/bin \  
&& chmod +x /usr/local/bin/dockerize /usr/local/bin/dumb-init \  
&& apt-get -y purge wget \  
&& apt-get -y autoremove \  
&& apt-get clean  
  
ADD run.sh /run.sh  
ADD kairosdb.properties.tmpl $KAIROSDB_HOME/conf/kairosdb.properties.tmpl  
  
CMD ["/usr/local/bin/dumb-init", "/bin/bash", "/run.sh"]  

