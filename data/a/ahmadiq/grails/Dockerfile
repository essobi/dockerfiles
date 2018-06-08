FROM phusion/baseimage:0.9.16  
MAINTAINER Ahmad Iqbal <ahmad@aurorasolutions.io>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Set customizable env vars defaults.  
ENV GRAILS_VERSION 2.4.3  
ENV java_version 1.8.0_25  
ENV filename jdk-8u25-linux-x64.tar.gz  
ENV downloadlink http://download.oracle.com/otn-
pub/java/jdk/8u25-b17/$filename -O /tmp/$filename  
ENV JAVA_HOME /usr/lib/jvm/jdk$java_version  
ENV PATH $JAVA_HOME/bin:$PATH  
ENV GRAILS_DEPENDENCY_CACHE_DIR /app/.m2/repository  
  
# Download Install utilities  
RUN apt-get update && apt-get install -y unzip wget && apt-get clean  
  
#Download java  
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" $downloadlink -O /tmp/$filename  
RUN mkdir /usr/lib/jvm && tar -zxf /tmp/$filename -C /usr/lib/jvm/  
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000
&& update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac
20000  
  
# Install Grails  
WORKDIR /usr/lib/jvm  
RUN wget
http://dist.springframework.org.s3.amazonaws.com/release/GRAILS/grails-$GRAILS_VERSION.zip  
RUN unzip grails-$GRAILS_VERSION.zip  
RUN rm -rf grails-$GRAILS_VERSION.zip  
RUN ln -s grails-$GRAILS_VERSION grails  
  
# Setup Grails path.  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
# Clean up APT.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/app"]  
WORKDIR /app  

