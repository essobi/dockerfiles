# From & maintainer  
FROM stakater/java:oracle-8  
MAINTAINER Rasheed Amir <rasheed@aurorasolutions.io>  
  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
  
# Set customizable env vars defaults.  
ENV GRAILS_VERSION 2.3.8  
ENV JAVA_OPTS -Xms256m -Xmx512m -XX:MaxPermSize=256m  
ENV GRAILS_DEPENDENCY_CACHE_DIR /home/stakater/.m2/repository  
  
  
# Install grails  
WORKDIR /usr/lib/jvm  
RUN wget
http://dist.springframework.org.s3.amazonaws.com/release/GRAILS/grails-$GRAILS_VERSION.zip  
RUN unzip grails-$GRAILS_VERSION.zip  
RUN rm -rf grails-$GRAILS_VERSION.zip  
RUN ln -s grails-$GRAILS_VERSION grails  
  
  
# Setup grails path  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
  
# Clean up APT.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

