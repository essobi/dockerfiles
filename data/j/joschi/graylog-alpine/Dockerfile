FROM openjdk:8-jre-alpine  
MAINTAINER Jochen Schalanda <jochen+docker@schalanda.name>  
  
ENV GRAYLOG_VERSION 2.4.5  
ENV GRAYLOG_URL_BASE https://packages.graylog2.org/releases/graylog  
ENV PATH /opt/graylog/bin:$PATH  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Graylog Alpine Docker Image" \  
org.label-schema.description="Official Graylog Docker image based on Alpine
Linux" \  
org.label-schema.url="https://www.graylog.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/joschi/docker-graylog-alpine" \  
org.label-schema.vendor="Graylog, Inc." \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="MIT"  
  
# ensure "graylog" user exists  
RUN addgroup -S graylog && adduser -S -G graylog graylog  
RUN apk add --no-cache bash curl su-exec  
#RUN apk add --no-cache libcap && setcap 'cap_net_bind_service=+ep'
$JAVA_HOME/bin/java  
RUN \  
mkdir -p /opt && \  
cd /opt && \  
curl -s -S -L -O "${GRAYLOG_URL_BASE}/graylog-${GRAYLOG_VERSION}.tgz" && \  
curl -s -S -L -O
"${GRAYLOG_URL_BASE}/graylog-${GRAYLOG_VERSION}.tgz.sha256.txt" && \  
sha256sum -c "graylog-${GRAYLOG_VERSION}.tgz.sha256.txt" && \  
tar -xzf "graylog-${GRAYLOG_VERSION}.tgz" && \  
rm -f "graylog-${GRAYLOG_VERSION}.tgz"
"graylog-${GRAYLOG_VERSION}.tgz.sha256.txt" && \  
mv "graylog-${GRAYLOG_VERSION}" graylog && \  
for GRAYLOG_PATH in \  
/opt/graylog/data/journal \  
/opt/graylog/data/contentpacks \  
/opt/graylog/config \  
; do \  
mkdir -p "${GRAYLOG_PATH}"; \  
done  
  
COPY config /opt/graylog/config  
COPY graylog.sh /opt/graylog/bin/graylog  
  
VOLUME /opt/graylog/data  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 9000  
CMD ["graylog"]  

