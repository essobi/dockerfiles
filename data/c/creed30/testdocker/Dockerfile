FROM java:8-jdk  
  
RUN apt-get update && apt-get install --yes sudo  
  
# add NodeJS 5.x repo  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
  
RUN apt-get update && apt-get install --yes nodejs  
  
# integrated qlik/gradle  
ENV GRADLE_VERSION 2.9  
WORKDIR /usr/bin  
RUN curl -sLO
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip &&
\  
unzip gradle-${GRADLE_VERSION}-all.zip && \  
ln -s gradle-${GRADLE_VERSION} gradle && \  
rm gradle-${GRADLE_VERSION}-all.zip  
  
ENV GRADLE_HOME /usr/bin/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
RUN mkdir /build  
WORKDIR /build  

