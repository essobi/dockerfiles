FROM fedora:24  
MAINTAINER Mario Ceresa <mario.ceresa@upf.edu>  
  
RUN dnf -y update && dnf clean all  
  
# This installs also git boost and several others important libs  
RUN dnf -y groupinstall "Development Tools" "Development Libraries" && dnf
clean all  
  
RUN dnf -y install java-1.8.0-openjdk sudo cmake gcc-c++ && dnf clean all  
  
# Configure Jenkins user  
ENV HOME /home/jenkins  
RUN groupadd -g 10000 jenkins  
RUN useradd -c "Jenkins user" -d $HOME -u 10000 -g 10000 -m jenkins  
RUN echo "jenkins:jenkins" | chpasswd  
RUN usermod -aG wheel jenkins  
  
# Configure jnlp client  
ARG VERSION=3.2  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
  
USER jenkins  
RUN mkdir /home/jenkins/.jenkins  
WORKDIR /home/jenkins  
  
ENTRYPOINT ["jenkins-slave"]  

