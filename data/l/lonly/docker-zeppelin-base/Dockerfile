FROM alpine:3.6  
  
ARG DIST_MIRROR=http://archive.apache.org/dist/zeppelin  
ARG VERSION=0.7.3  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL \  
maintainer="lonly197@qq.com" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="Apache License 2.0" \  
org.label-schema.name="lonly/docker-zeppelin-base" \  
org.label-schema.url="https://github.com/lonly197" \  
org.label-schema.description="This is a basic docker image for building
docker-zeppelin and building docker-zeppelin-cn." \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/lonly197/docker-zeppelin-base" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vendor="lonly197@qq.com" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
ENV ZEPPELIN_HOME=/opt/zeppelin \  
JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk \  
PATH=$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
RUN set -x \  
## fix 'ERROR: http://dl-cdn.alpinelinux.org/alpine/v3.6/main: BAD archive'  
&& echo http://mirrors.aliyun.com/alpine/v3.6/main/ >> /etc/apk/repositories \  
&& echo http://mirrors.aliyun.com/alpine/v3.6/community/>>
/etc/apk/repositories \  
## update apk package  
&& apk update \  
## add base package  
&& apk add --no-cache --upgrade bash curl ca-certificates openssl wget rsync
jq openjdk8 \  
&& update-ca-certificates \  
## mkidr work dir  
&& mkdir -p ${ZEPPELIN_HOME} \  
## download zeppelin package  
&& curl ${DIST_MIRROR}/zeppelin-${VERSION}/zeppelin-${VERSION}-bin-all.tgz |
tar xvz -C ${ZEPPELIN_HOME} \  
&& mv ${ZEPPELIN_HOME}/zeppelin-${VERSION}-bin-all/* ${ZEPPELIN_HOME} \  
## cleanup  
&& rm -rf ${ZEPPELIN_HOME}/zeppelin-${VERSION}-bin-all \  
&& rm -rf *.tgz \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/nativelib  
  
EXPOSE 8080 8443  
  
VOLUME ${ZEPPELIN_HOME}/conf \  
${ZEPPELIN_HOME}/logs \  
${ZEPPELIN_HOME}/notebook \  
${ZEPPELIN_HOME}/local-repo \  
${ZEPPELIN_HOME}/helium  
  
WORKDIR ${ZEPPELIN_HOME}

