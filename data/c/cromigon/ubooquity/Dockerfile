FROM alpine:3.5  
MAINTAINER Niclas Björner <niclas@cromigon.se>  
  
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk/bin/java" APP_VERSION="1.10.1"  
RUN apk --no-cache add openjdk8-jre-base openjdk8-jre-lib curl unzip && \  
mkdir -p /opt/ubooquity/fonts && \  
mkdir -p /opt/ubooquity-data && \  
mkdir -p /opt/data && \  
curl -Ss http://vaemendis.net/ubooquity/downloads/Ubooquity-${APP_VERSION}.zip
-o /tmp/${APP_VERSION}.zip && \  
unzip /tmp/${APP_VERSION}.zip -d /opt/ubooquity && \  
rm /tmp/${APP_VERSION}.zip  
  
RUN wget http://vaemendis.net/ubooquity/downloads/themes/modern-1.7.0.zip -O
/tmp/modern.zip && \  
unzip /tmp/modern.zip -d /opt/ubooquity-data/themes && \  
rm /tmp/modern.zip  
  
WORKDIR /opt/ubooquity  
EXPOSE 2202  
VOLUME /opt/ubooquity-data /opt/data  
  
ENTRYPOINT ["java", "-jar", "Ubooquity.jar", "-workdir", "/opt/ubooquity-
data", "-headless"]  
  

