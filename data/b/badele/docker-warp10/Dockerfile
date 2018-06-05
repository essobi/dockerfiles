FROM lwieske/java-8:jdk-8u66-slim  
MAINTAINER Tabmo <devs@tabmo.io>  
  
ENV WARP10_VERSION=1.2.15  
# Updating  
RUN apk update  
  
# Installing packages & build-dependencies  
RUN apk add bash curl python  
RUN apk add --virtual=build-dependencies ca-certificates wget  
  
# Getting warp10  
RUN mkdir /opt \  
&& cd /opt \  
&& wget
https://dl.bintray.com/cityzendata/generic/io/warp10/warp10/$WARP10_VERSION/warp10-$WARP10_VERSION.tar.gz  
  
# Unpack  
RUN cd /opt \  
&& tar xzf warp10-*.tar.gz \  
&& rm warp10-*.tar.gz \  
&& ln -s /opt/warp10-* /opt/warp10  
  
WORKDIR /opt/warp10  
  
ENV QUANTUM_VERSION=3.0.3  
ENV HASH_CLASS="@key:128:warp.hash.class@"  
ENV HASH_LABELS="@key:128:warp.hash.labels@"  
ENV HASH_INDEX="@key:128:warp.hash.index@"  
ENV HASH_TOKEN="@key:128:warp.hash.token@"  
ENV HASH_APP="@key:128:warp.hash.app@"  
ENV AES_TOKEN="@key:256:warp.aes.token@"  
ENV AES_SCRIPTS="@key:256:warp.aes.scripts@"  
ENV AES_METASETS="@key:256:warp.aes.metasets@"  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 8080/tcp  
EXPOSE 8090/tcp  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

