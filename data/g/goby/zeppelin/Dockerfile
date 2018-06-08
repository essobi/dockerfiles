FROM openjdk:8-alpine  
  
ENV ZEPPELIN_VERSION 0.7.1  
ENV ZEPPELIN_HOME /zeppelin  
  
RUN apk add --update curl bash tar \  
&& mkdir -p ${ZEPPELIN_HOME} \  
&& curl -L
http://ftp.jaist.ac.jp/pub/apache/zeppelin/zeppelin-$ZEPPELIN_VERSION/zeppelin-$ZEPPELIN_VERSION-
bin-all.tgz \  
| tar -xz --strip=1 -C ${ZEPPELIN_HOME} \  
&& rm -fr /var/cache/apk/*  
  
ADD log4j.properties ${ZEPPELIN_HOME}/conf/  
  
WORKDIR ${ZEPPELIN_HOME}  
VOLUME ${ZEPPELIN_HOME}/local-repo  
EXPOSE 8080  
CMD ["bin/zeppelin.sh"]  

