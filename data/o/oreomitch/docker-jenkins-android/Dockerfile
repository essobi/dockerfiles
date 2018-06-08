#######################################################################  
# Dockerfile to build a Jenkins CI container image  
# Based on Ubuntu  
#######################################################################  
  
# Set the base image to Ubuntu  
FROM oreomitch/ubuntu-android-sdk:15.04-JDK7  
# File Author / Maintainer  
MAINTAINER Mitchell Wong Ho <oreomitch@gmail.com>  
  
RUN apt-get install -y unzip  
ADD https://services.gradle.org/distributions/gradle-2.4-all.zip /opt/  
RUN unzip /opt/gradle-2.4-all.zip -d /opt/gradle  
ENV GRADLE_HOME /opt/gradle/gradle-2.4-all  
ENV PATH $GRADLE_HOME/bin:$PATH  
  
# Add git  
RUN apt-get install -y git-core  
  
# Add Jenkins  
# Thanks to orchardup/jenkins Dockerfile  
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key
add -  
RUN echo "deb http://pkg.jenkins-ci.org/debian-stable binary/" >>
/etc/apt/sources.list  
RUN apt-get update  
# HACK: https://issues.jenkins-ci.org/browse/JENKINS-20407  
RUN mkdir /var/run/jenkins  
RUN mkdir /opt/data  
RUN apt-get install -y jenkins  
RUN service jenkins stop  
EXPOSE 8080 48429  
VOLUME ["/var/lib/jenkins"]  
USER jenkins  
ENTRYPOINT [ "java","-jar","/usr/share/jenkins/jenkins.war" ]  
## END  

