FROM codenvy/ubuntu_jdk8  
  
ENV GRADLE_VERSION=2.14.1  
ENV GRADLE_HOME /home/user/gradle-$GRADLE_VERSION  
ENV PATH $GRADLE_HOME/bin:$PATH  
  
RUN wget -P /home/user/ --quiet
https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip && \  
cd /home/user/ && unzip gradle-$GRADLE_VERSION-bin.zip && rm
gradle-$GRADLE_VERSION-bin.zip  
  
USER root  
  
RUN curl -fsSL https://get.docker.com/ | sh  
  
RUN gpasswd -a user docker  
  
USER user  
EXPOSE 9000  
WORKDIR /projects  
  

