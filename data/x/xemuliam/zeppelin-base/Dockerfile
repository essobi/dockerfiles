FROM alpine  
MAINTAINER Viacheslav Kalashnikov <xemuliam@gmail.com>  
ARG DIST_MIRROR=http://archive.apache.org/dist/zeppelin  
ARG VERSION=0.7.3  
ENV ZEPPELIN_HOME=/opt/zeppelin \  
JAVA_HOME=/usr/lib/jvm/java-1.7-openjdk \  
PATH=$PATH:/usr/lib/jvm/java-1.7-openjdk/jre/bin:/usr/lib/jvm/java-1.7-openjdk/bin  
RUN apk update && apk add --upgrade bash curl jq openjdk7 && \  
mkdir -p ${ZEPPELIN_HOME} && \  
curl ${DIST_MIRROR}/zeppelin-${VERSION}/zeppelin-${VERSION}-bin-all.tgz | tar
xvz -C ${ZEPPELIN_HOME} && \  
mv ${ZEPPELIN_HOME}/zeppelin-${VERSION}-bin-all/* ${ZEPPELIN_HOME} && \  
rm -rf ${ZEPPELIN_HOME}/zeppelin-${VERSION}-bin-all && \  
rm -rf *.tgz && \  
rm -rf /var/cache/apk/*  
EXPOSE 8080 8443  
VOLUME ${ZEPPELIN_HOME}/logs \  
${ZEPPELIN_HOME}/notebook  
WORKDIR ${ZEPPELIN_HOME}  
CMD ./bin/zeppelin.sh run  

