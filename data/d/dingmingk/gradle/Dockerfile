FROM java:openjdk-8-jdk  
MAINTAINER dingmingk <dingmingk@gmail.com>  
  
ENV GRADLE_VERSION 2.6  
ENV GRADLE_HOME /gradle  
  
RUN curl -sLO
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip \  
&& unzip gradle-${GRADLE_VERSION}-all.zip \  
&& mv gradle-${GRADLE_VERSION} $GRADLE_HOME \  
&& rm gradle-${GRADLE_VERSION}-all.zip \  
&& chmod -R 777 $GRADLE_HOME  
  
ENV PATH $PATH:$GRADLE_HOME/bin  
ENV GRADLE_USER_HOME /project/.gradle  
  
WORKDIR /project  
  
ENTRYPOINT ["gradle"]  
CMD ["-version"]  

