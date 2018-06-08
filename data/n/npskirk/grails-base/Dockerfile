FROM anapsix/alpine-java:8_jdk  
MAINTAINER Kirk Stork <kirk.stork@zenuevo.com>  
  
ENV GRADLE_VERSION 3.2  
ENV GRAILS_VERSION 3.2.9  
WORKDIR /opt  
  
RUN apk add --update unzip && \  
apk add --update openssl && \  
apk add --update bash && \  
wget https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip
&& \  
unzip gradle-$GRADLE_VERSION-bin.zip && \  
rm -rf gradle-$GRADLE_VERSION-bin.zip && \  
ln -s gradle-$GRADLE_VERSION gradle && \  
wget https://github.com/grails/grails-
core/releases/download/v$GRAILS_VERSION/grails-3.2.9.zip && \  
unzip grails-$GRAILS_VERSION.zip && \  
rm -rf grails-$GRAILS_VERSION.zip && \  
ln -s grails-$GRAILS_VERSION grails  
  
ENV GRADLE_HOME /opt/gradle  
ENV PATH $GRADLE_HOME/bin:$PATH  
ENV GRAILS_HOME /opt/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
  
# Populate local maven repo with common dependencies  
COPY build.gradle /opt/ghost/build.gradle  
COPY gradle.properties /opt/ghost/gradle.properties  
WORKDIR /opt/ghost  
RUN gradle buildNeeded  
WORKDIR /opt  
RUN rm -Rf ghost  
  

