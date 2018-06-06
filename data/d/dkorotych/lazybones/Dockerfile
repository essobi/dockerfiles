FROM openjdk:8-jre-alpine  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VCS_URL  
ARG VERSION  
  
MAINTAINER Dmitry Korotych, dkorotych at gmail dot com  
  
LABEL \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.vendor="Dmitry Korotych, dkorotych at gmail dot com" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
ENV LAZYBONES_VERSION 0.8.3  
ENV APPLICATION_DIR /app  
ENV LAZYBONES_DIR ${USER_HOME}/.lazybones  
  
RUN apk add --no-cache openssl bash \  
&& cd /usr/local \  
&& wget https://dl.bintray.com/pledbrook/lazybones-
templates/lazybones-${LAZYBONES_VERSION}.zip \  
&& unzip lazybones-${LAZYBONES_VERSION}.zip \  
&& ln -s lazybones-${LAZYBONES_VERSION} lazybones \  
&& rm lazybones-${LAZYBONES_VERSION}.zip \  
&& apk del openssl  
  
ENV PATH /usr/local/lazybones/bin:${PATH}  
  
WORKDIR ${APPLICATION_DIR}  
VOLUME ${APPLICATION_DIR}  
  
ENTRYPOINT ["/usr/local/lazybones/bin/lazybones"]  
CMD ["help"]

