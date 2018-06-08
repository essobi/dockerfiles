FROM openjdk:8  
ENV GRADLE_VERSION 3.0  
WORKDIR /usr/bin  
  
RUN wget
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip &&
\  
unzip gradle-${GRADLE_VERSION}-all.zip && \  
ln -s gradle-${GRADLE_VERSION} gradle && \  
rm gradle-${GRADLE_VERSION}-all.zip  
  
ENV GRADLE_HOME /usr/bin/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
RUN apt-get update && \  
apt-get -y install python3-setuptools python3-dev && \  
easy_install3 pip && \  
pip install awscli && \  
apt-get clean

