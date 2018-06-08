FROM java:8u92-jdk-alpine  
MAINTAINER Slawomir Messner "slawomir.messner@gmx.de"  
#Prepare libs  
ENV GRADLE_VERSION 2.14.1  
WORKDIR /opt  
#Download gradle, unzip and cleanup  
RUN apk update && apk add bash curl libstdc++ && curl -sLO
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip &&
\  
unzip gradle-${GRADLE_VERSION}-bin.zip && \  
rm gradle-${GRADLE_VERSION}-bin.zip && \  
apk del curl && \  
rm -rf /var/cache/apk/*  
#Set environmentvariables  
ENV GRADLE_HOME /opt/gradle-$GRADLE_VERSION  
ENV PATH $PATH:$GRADLE_HOME/bin  
#Standard ENTRYPOINT  
ENTRYPOINT ["gradle"]  
#Parameter ENTRYPOINT  
CMD ["clean", "build"]

