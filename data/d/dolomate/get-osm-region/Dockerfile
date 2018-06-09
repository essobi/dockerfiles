FROM openjdk:jdk-alpine  
  
RUN apk update && \  
apk upgrade && \  
apk add --update autoconf gcc git curl bash libstdc++ wget && rm -rf
/var/cache/apk/*  
  
RUN mkdir /usr/lib/gradle /app  
  
ENV GRADLE_VERSION 3.5  
ENV GRADLE_HOME /usr/lib/gradle/gradle-${GRADLE_VERSION}  
ENV PATH ${PATH}:${GRADLE_HOME}/bin  
  
WORKDIR /usr/lib/gradle  
RUN set -x \  
&& wget
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip gradle-${GRADLE_VERSION}-bin.zip \  
&& rm gradle-${GRADLE_VERSION}-bin.zip  
  
RUN mkdir ~/src && \  
cd ~/src && \  
git clone git://github.com/openstreetmap/osmosis.git && \  
cd osmosis && \  
./gradlew assemble  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
  
CMD ["./xml-to-pbf.sh"]  

