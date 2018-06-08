FROM java:8-jdk  
  
MAINTAINER hello@clabs.com.ua <Dmytro Khaynas>  
  
RUN apt-get update && \  
apt-get -y install bash mc git  
  
ENV GRADLE_VERSION 2.12  
WORKDIR /usr/bin  
RUN curl -sLO
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip &&
\  
unzip gradle-${GRADLE_VERSION}-all.zip && \  
ln -s gradle-${GRADLE_VERSION} gradle && \  
rm gradle-${GRADLE_VERSION}-all.zip  
  
ENV GRADLE_HOME /usr/bin/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
WORKDIR /home/deployIt  
ADD run.sh run.sh  
RUN chmod +x run.sh  
CMD ["/home/deployIt/run.sh"]  

