FROM lonly/docker-zeppelin:0.7.3  
  
ARG VERSION=0.7.3-special-cn  
ARG VCS_REF  
ARG BUILD_DATE  
  
LABEL \  
maintainer="lonly197@qq.com" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="Apache License 2.0" \  
org.label-schema.name="lonly/docker-zeppelin" \  
org.label-schema.url="https://github.com/lonly197" \  
org.label-schema.description="This is a full Docker image for Apache Zeppelin,
based on Official image." \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/lonly197/docker-zeppelin" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vendor="lonly197@qq.com" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
# Install package  
RUN set -x \  
## Define var  
&& ZEPPELIN_VERSION=0.7.3 \  
## Chinesize zeppelin web  
### Enter work dir  
&& cd ${ZEPPELIN_HOME} \  
## Unzip zeppelin web war  
&& mkdir -p webapp \  
&& unzip -oq zeppelin-web-${ZEPPELIN_VERSION}.war -d webapp \  
## Remove old war  
&& rm -rf zeppelin-web-${ZEPPELIN_VERSION}.war \  
## Enter webapp dir  
&& cd ./webapp/ \  
## Download Chinesization zeppelin web tar  
&& wget -q -c https://github.com/lonly197/zeppelin-
web/archive/${VERSION}.tar.gz -O ${VERSION}.tar.gz \  
&& tar xvf ${VERSION}.tar.gz --strip 1 \  
&& rm -rf ${VERSION}.tar.gz \  
## Zip Chinesization war  
&& jar -cvfM0 zeppelin-web-${ZEPPELIN_VERSION}.war ./* \  
&& mv zeppelin-web-${ZEPPELIN_VERSION}.war ${ZEPPELIN_HOME}/ \  
&& cd ../ \  
&& rm -rf webapp \  
## Cleanup  
&& rm -rf *.tgz *.zip *.tar \  
&& rm -rf /tmp/*  
  
# Start Zeppelin Server  
CMD ${ZEPPELIN_HOME}/bin/zeppelin.sh run

