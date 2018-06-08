FROM openjdk:8  
MAINTAINER Tobias Raatiniemi <raatiniemi@gmail.com>  
  
ENV GRADLE_VERSION 4.4  
ENV GRADLE_HOME /opt/gradle-${GRADLE_VERSION}  
ENV GRADLE_BIN_ZIP gradle-${GRADLE_VERSION}-bin.zip  
ENV GRADLE_USER_HOME /cache  
ENV BUILD_HOME /build  
  
RUN set -x \  
&& curl -L http://downloads.gradle.org/distributions/${GRADLE_BIN_ZIP} -o
/tmp/${GRADLE_BIN_ZIP} \  
&& unzip /tmp/${GRADLE_BIN_ZIP} -d /opt/ \  
&& rm /tmp/${GRADLE_BIN_ZIP}  
  
WORKDIR $BUILD_HOME  
VOLUME $GRADLE_USER_HOME  
  
ENV PATH $PATH:${GRADLE_HOME}/bin  

