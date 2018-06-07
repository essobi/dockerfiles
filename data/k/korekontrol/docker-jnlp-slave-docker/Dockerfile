FROM openjdk:8-jdk  
MAINTAINER Marek Obuchowicz <marek@korekontrol.eu>  
  
# Install docker client  
RUN curl -sSL https://get.docker.com/ | sh  
  
# Tini  
ADD https://github.com/krallin/tini/releases/download/v0.15.0/tini /tini  
RUN chmod +x /tini  
  
# AWSCLI  
RUN apt-get update -qy && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qy python-pip groff-base && \  
pip install awscli && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Jenkins  
ENV HOME /home/jenkins  
RUN useradd -c "Jenkins user" -d $HOME -u 10000 -g 999 -m jenkins  
LABEL Description="This is a base image, which provides the Jenkins agent
executable (slave.jar) and docker client" Vendor="KoreKontrol" Version="3.7"  
  
ARG VERSION=3.7  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
USER jenkins  
RUN mkdir /home/jenkins/.jenkins  
VOLUME /home/jenkins/.jenkins  
WORKDIR /home/jenkins  
  
# jnlp slave  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
ENTRYPOINT ["/tini", "--", "jenkins-slave"]  

