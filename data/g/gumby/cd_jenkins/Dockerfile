FROM ubuntu:12.04  
MAINTAINER Patrick Gombola, "pgumby@gmail.com"  
RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >>
/etc/apt/sources.list  
RUN apt-get update && apt-get clean  
  
# Git  
RUN apt-get install -q -y git  
  
# Grade  
ADD https://services.gradle.org/distributions/gradle-1.12-all.zip
/opt/gradle-1.12-all.zip  
RUN unzip /opt/gradle-1.12-all.zip  
ENV GRADLE_HOME /opt/gradle-1.12  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Jenkins  
RUN apt-get install -q -y openjdk-7-jre-headless && apt-get clean  
ADD http://mirrors.jenkins-ci.org/war/1.560/jenkins.war /opt/jenkins.war  
RUN ln -sf /jenkins /root/.jenkins  
  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
EXPOSE 8080  
VOLUME ["/jenkins"]  
CMD [""]  

