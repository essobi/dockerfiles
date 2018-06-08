FROM openjdk:8  
MAINTAINER Mohammad Naghavi <mohamnag@gmail.com>  
  
ENV GRADLE_VERSION 4.0.1  
ENV GRADLE_HOME /usr/bin/gradle  
ENV GRADLE_USER_HOME /cache  
  
ADD https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip
/usr/bin/gradle.zip  
WORKDIR /usr/bin  
RUN apt-get install -y unzip && \  
unzip gradle.zip && \  
ln -s gradle-${GRADLE_VERSION} gradle && \  
rm gradle.zip  
  
# clean up  
RUN apt-get remove -y unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
VOLUME $GRADLE_USER_HOME  
VOLUME /app  
  
WORKDIR /app  
CMD ["gradle", "-version"]  

