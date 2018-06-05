FROM mattjtodd/alpine-base:3.5  
WORKDIR /activemq  
  
ARG ACTIVEMQ_VERSION=5.14.3  
ENV
ACTIVEMQ_URL=https://www.apache.org/dist/activemq/$ACTIVEMQ_VERSION/apache-
activemq-$ACTIVEMQ_VERSION-bin.tar.gz  
  
ENV DUMB_INIT_VERSION=1.2.0  
ENV JAVA8_VERSION=8.121.13-r0  
  
# su-exec user  
RUN addgroup activemq && \  
adduser -S -G activemq activemq  
  
RUN set -ex && \  
# update and install packages  
apk update && \  
apk add \--no-cache --update --repository
http://dl-3.alpinelinux.org/alpine/edge/community/ \  
curl \  
gnupg \  
openjdk8-jre-base=${JAVA8_VERSION} \  
tar && \  
\  
# install activemq  
curl --progress-bar $ACTIVEMQ_URL -o activemq.tar.gz && \  
curl --progress-bar $ACTIVEMQ_URL.asc -o activemq.tar.gz.asc && \  
curl --progress-bar https://www.apache.org/dist/activemq/KEYS | gpg --import
&& \  
gpg --verify activemq.tar.gz.asc && \  
tar xzf activemq.tar.gz --strip-components=1 && \  
rm activemq.tar.gz* && \  
apk del curl gnupg && \  
rm -rf /var/cache/apk/* && \  
chown activemq:activemq . -R  
  
EXPOSE 1883 5672 8161 61613 61614 61616  
ENTRYPOINT ["dumb-init", "--", "su-exec", "activemq", "bin/activemq"]  
  
CMD ["console"]  

