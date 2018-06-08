FROM stakater/java8-alpine:1.8.0_121  
MAINTAINER Muhammad Hamza Zaib <hamza@aurorasolutions.io>  
  
# Set customizable env vars defaults.  
ENV GRAILS_VERSION 3.2.2  
ENV GRADLE_VERSION 3.1  
ENV JAVA_OPTS -Xms256m -Xmx512m  
ENV GRAILS_DEPENDENCY_CACHE_DIR /app/.m2/repository  
  
# Download Install utilities  
RUN apk -Uuv add unzip wget  
  
# Install Grails  
WORKDIR /usr/lib/jvm  
RUN wget https://github.com/grails/grails-
core/releases/download/v$GRAILS_VERSION/grails-$GRAILS_VERSION.zip && \  
unzip grails-$GRAILS_VERSION.zip && \  
rm -rf grails-$GRAILS_VERSION.zip && \  
ln -s grails-$GRAILS_VERSION grails  
  
# Setup Grails path.  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
ENV GRADLE_HOME /usr/local/gradle  
ENV GRADLE_USER_HOME /root/.gradle  
ENV PATH ${PATH}:${GRADLE_HOME}/bin  
  
#Install Gradle  
WORKDIR /usr/local  
RUN wget https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-
bin.zip && \  
unzip gradle-$GRADLE_VERSION-bin.zip && \  
rm -f gradle-$GRADLE_VERSION-bin.zip && \  
ln -s gradle-$GRADLE_VERSION gradle  
  
# Clean up APK.  
RUN rm /var/cache/apk/*  
  
VOLUME ["/app"]  
WORKDIR /app

