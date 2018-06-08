FROM rubdos/android-java8  
  
# Copyright 2016 Ruben De Smet  
MAINTAINER Ruben De Smet "ruben.de.smet@rubdos.be"  
RUN wget --quiet -O /tmp/gradle.zip
https://services.gradle.org/distributions/gradle-2.10-bin.zip && unzip
/tmp/gradle.zip -d /opt && rm -rf /tmp/gradle.zip  
  
ENV GRADLE_HOME /opt/gradle-2.10  
ENV PATH ${PATH}:${GRADLE_HOME}/bin  
  
COPY build.gradle /tmp/  
COPY src /tmp/src  
RUN cd /tmp/ && gradle test  
RUN ls /tmp/  
RUN rm -rf /tmp/*  
  
WORKDIR /opt/workspace  

