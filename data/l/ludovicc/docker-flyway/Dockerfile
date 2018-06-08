FROM hbpmip/java-base:8u151-1  
MAINTAINER Ludovic Claude <ludovic.claude@chuv.ch>  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
ENV FLYWAY_VERSION=4.2.0  
RUN apk update && apk add --no-cache bash wget \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
RUN wget -O /tmp/flyway.zip
https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.zip \  
&& unzip /tmp/flyway.zip \  
&& rm /tmp/flyway.zip \  
&& mv /flyway-${FLYWAY_VERSION} /flyway \  
&& ln -s /flyway/flyway /usr/local/bin/flyway  
  
COPY docker/flyway.conf.tmpl /flyway/conf/  
COPY docker/run.sh /  
  
# A simple test  
RUN flyway 2>&1 | grep "Flyway ${FLYWAY_VERSION}"  
  
ENV PATH /flyway:$PATH  
WORKDIR /flyway  
VOLUME /flyway/jars  
VOLUME /flyway/sql  
  
# Force the use of standard DNS resolver, Go re-implementation causes
sometimes problems within Docker  
# See https://golang.org/pkg/net/#hdr-Name_Resolution  
ENV GODEBUG=netdns=cgo  
  
ENTRYPOINT ["/run.sh"]  
CMD ["--help"]  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="hbpmip/flyway" \  
org.label-schema.description="Flyway tool to manage database migrations" \  
org.label-schema.url="https://github.com/LREN-CHUV/docker-flyway" \  
org.label-schema.vcs-type="git" \  
org.label-schema.vcs-url="https://github.com/LREN-CHUV/docker-flyway.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.version="$VERSION" \  
org.label-schema.vendor="LREN CHUV" \  
org.label-schema.license="Apache2.0" \  
org.label-schema.docker.dockerfile="Dockerfile" \  
org.label-schema.schema-version="1.0"  

