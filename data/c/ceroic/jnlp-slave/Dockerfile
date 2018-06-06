FROM java:8-jdk  
MAINTAINER Ceroic <ops@ceroic.com>  
  
ENV HOME /home/jenkins  
ENV REMOTING_VERSION 2.59  
RUN useradd -c "Jenkins user" -d $HOME -m jenkins  
  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar http://repo.jenkins-
ci.org/public/org/jenkins-
ci/main/remoting/${REMOTING_VERSION}/remoting-${REMOTING_VERSION}.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
COPY jenkins-slave.sh /usr/local/bin/jenkins-slave  
  
VOLUME /home/jenkins  
WORKDIR /home/jenkins  
USER jenkins  
  
ENTRYPOINT ["jenkins-slave"]

