FROM anapsix/alpine-java:8_server-jre  
  
RUN mkdir -p /app  
  
RUN apk update && apk upgrade \  
&& apk --no-cache add --virtual build-dependencies unzip \  
&& apk --no-cache add curl python  
  
ENV PLAY_VERSION 1.4.2  
RUN curl --location -s
https://downloads.typesafe.com/play/$PLAY_VERSION/play-$PLAY_VERSION.zip >
/tmp/play-$PLAY_VERSION.zip \  
&& unzip -q /tmp/play-$PLAY_VERSION.zip -d /opt \  
&& rm -rf /tmp/play-$PLAY_VERSION.zip \  
/opt/play-$PLAY_VERSION/COPYING \  
/opt/play-$PLAY_VERSION/documentation \  
/opt/play-$PLAY_VERSION/framework/test-src \  
/opt/play-$PLAY_VERSION/play.bat \  
/opt/play-$PLAY_VERSION/python/*.dll \  
/opt/play-$PLAY_VERSION/python/python.* \  
/opt/play-$PLAY_VERSION/README.textile \  
/opt/play-$PLAY_VERSION/samples-and-tests \  
/opt/play-$PLAY_VERSION/support  
  
RUN apk del --purge build-dependencies \  
&& rm -fr /var/cache/apk/*  
  
ENV PATH /opt/play-$PLAY_VERSION:$PATH  
  
WORKDIR /app  
  
EXPOSE 9000  
CMD ["play", "version"]  
  
#FROM socialmetrix/play:1.4.2-alpine  
MAINTAINER http://sinfonier-project.net  
  
RUN apk add --no-cache bash git openssl  
  
ENV JAVA_CACERTS $JAVA_HOME/jre/lib/security/cacerts  
ADD ca.pem /etc/ssl/certs/  
RUN keytool -noprompt -storepass changeit -keystore ${JAVA_CACERTS} -import
-file /etc/ssl/certs/ca.pem -alias ELEVENPATH_CA  
  
ARG SOURCE_BRANCH=master  
  
RUN git clone https://github.com/telefonicaid/fiware-sinfonier.git /app && cd
/app && git checkout $SOURCE_BRANCH  
RUN git status  
RUN echo $VERSION  
RUN echo $DOCKER_TAG  
RUN echo $SOURCE_BRANCH  
RUN echo $IMAGE_NAME  
  
WORKDIR /app/sinfonier-web  
  
RUN play dependencies --verbose  
  
CMD ["play", "run", "--%docker"]  
  

