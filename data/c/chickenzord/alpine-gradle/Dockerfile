FROM anapsix/alpine-java:jdk8  
  
MAINTAINER Akhyar Amarullah <akhyrul@gmail.com>  
  
ENV IVY_HOME /cache  
ENV GRADLE_VERSION 2.6  
ENV GRADLE_HOME /usr/local/gradle  
ENV PATH ${PATH}:${GRADLE_HOME}/bin  
ENV GRADLE_USER_HOME /gradle  
  
# Install gradle  
WORKDIR /usr/local  
RUN wget https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-
bin.zip && \  
unzip gradle-$GRADLE_VERSION-bin.zip && \  
rm -f gradle-$GRADLE_VERSION-bin.zip && \  
ln -s gradle-$GRADLE_VERSION gradle && \  
echo -ne "- with Gradle $GRADLE_VERSION\n" >> /root/.built  
  
RUN apk update && apk add libstdc++ && rm -rf /var/cache/apk/*  
  
RUN mkdir -p /gradle && mkdir -p /app  
VOLUME /gradle /app  
  
WORKDIR /app  
ENTRYPOINT gradle  

