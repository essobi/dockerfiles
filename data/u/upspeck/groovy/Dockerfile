FROM upspeck/java:1.8  
MAINTAINER Jeyson Maia <jeyson@upspeck.io>  
  
# Groovy  
ENV GROOVY_VERSION 2.4.5  
WORKDIR /usr/lib  
RUN wget
http://mirror.nbtelecom.com.br/apache/groovy/${GROOVY_VERSION}-incubating/distribution/apache-
groovy-sdk-${GROOVY_VERSION}.zip  
RUN unzip "apache-groovy-sdk-${GROOVY_VERSION}.zip"  
RUN ln -s "/usr/lib/groovy-${GROOVY_VERSION}/bin/groovy" /usr/bin/groovy  
RUN rm "apache-groovy-sdk-${GROOVY_VERSION}.zip"  
RUN mkdir -p /usr/src/app  
  
# Set Appropriate Environmental Variables  
ENV GROOVY_HOME /usr/src/groovy  
ENV PATH $PATH:$GROOVY_HOME/bin  
  
USER $USER  
# Default command is "/usr/bin/groovy -version" on /usr/bin/app dir  
# (ie. Mount project at /usr/bin/app "docker --rm -v /path/to/app:/usr/bin/app
groovy <command>")  
#VOLUME /usr/bin/app  
WORKDIR /usr/bin/app  

