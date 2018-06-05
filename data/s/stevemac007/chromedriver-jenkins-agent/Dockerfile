FROM selenium/standalone-chrome  
MAINTAINER Steve Mactaggart <steve@whitesquaresoft.com>  
LABEL Description="This is a chrome/chromedriver image including Jenkins agent
executable (slave.jar)"  
  
USER root  
  
RUN apt-get update  
RUN apt-get -y install python git curl  
  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
  
ENV HOME /home/jenkins  
RUN groupadd -g 10000 jenkins  
RUN useradd -c "Jenkins user" -d $HOME -u 10000 -g 10000 -m jenkins  
  
ARG VERSION=3.5  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
USER jenkins  
RUN mkdir /home/jenkins/.jenkins  
VOLUME /home/jenkins/.jenkins  
WORKDIR /home/jenkins  
  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
ENTRYPOINT ["jenkins-slave"]  

