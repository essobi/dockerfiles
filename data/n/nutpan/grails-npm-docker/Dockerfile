FROM java:8  
ENV GRAILS_VERSION 3.2.4  
WORKDIR /usr/lib/jvm  
RUN wget https://github.com/grails/grails-
core/releases/download/v$GRAILS_VERSION/grails-$GRAILS_VERSION.zip && \  
unzip grails-$GRAILS_VERSION.zip && \  
rm -rf grails-$GRAILS_VERSION.zip && \  
ln -s grails-$GRAILS_VERSION grails  
  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
RUN apt-get update  
RUN apt-get install -y nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g uglify-js  
RUN apt-get install -y maven  
RUN wget https://services.gradle.org/distributions/gradle-3.4.1-bin.zip  
RUN mkdir /opt/gradle  
RUN unzip -d /opt/gradle gradle-3.4.1-bin.zip  
ENV PATH $PATH:/opt/gradle/gradle-3.4.1/bin  
  
RUN mkdir /workbench  
  
WORKDIR /workbench  

