FROM python:latest  
  
MAINTAINER Juan Carlos Tong <juancarlos.tong@shipwire.com>  
  
RUN apt-get update && apt-get -y install default-jre fabric  
  
#  
# Jenkins Slave  
#  
ENV HOME /home/jenkins  
RUN useradd -c "Jenkins user" -d $HOME -m jenkins  
  
ARG VERSION=2.62  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
  
RUN chmod 755 /usr/local/bin/jenkins-slave  
  
VOLUME /home/jenkins  
WORKDIR /home/jenkins  
USER jenkins  
  
RUN echo $PATH  
  
ENTRYPOINT ["jenkins-slave"]  
  
#  
# Purge  
#  
USER root  
  
RUN rm -rf /sbin/sln \  
; rm -rf /var/cache/{ldconfig,yum}/*  

