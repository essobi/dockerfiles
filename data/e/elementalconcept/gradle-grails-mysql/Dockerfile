# Use ubuntu 16 based java 8 image  
FROM cogniteev/oracle-java:java8  
MAINTAINER bishesh16  
  
ARG GRADLE_VERSION=2.6  
ENV GRAILS_VERSION 3.1.8  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update apt-get  
RUN apt-get -qq update  
RUN apt-get -qq -y install curl wget unzip  
  
#Install Gradle  
WORKDIR /usr/bin  
RUN curl -sLO
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip &&
\  
unzip gradle-${GRADLE_VERSION}-all.zip && \  
ln -s gradle-${GRADLE_VERSION} gradle && \  
rm gradle-${GRADLE_VERSION}-all.zip  
  
# Setup Gradle path.  
ENV GRADLE_HOME /usr/bin/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
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
  
# install mysql with root/root  
RUN echo "mysql-server-5.7 mysql-server/root_password password root" |
debconf-set-selections  
RUN echo "mysql-server-5.7 mysql-server/root_password_again password root" |
debconf-set-selections  
RUN apt-get -y install mysql-server-5.7  
  
RUN mkdir /app  
WORKDIR /app  
  
CMD /bin/bash  

