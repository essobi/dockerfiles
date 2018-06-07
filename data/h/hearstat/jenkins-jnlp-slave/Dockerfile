FROM ubuntu:xenial  
  
MAINTAINER Hearst Automation Team "atat@hearst.com"  
# Environment Variables  
ENV JENKINS_HOME /var/lib/jenkins  
  
RUN apt-get update &&\  
apt-get install -y openssh-server \  
bash \  
curl \  
openjdk-8-jdk &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/* &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
# Add user and group jenkins to the image  
RUN useradd -m -p jenkins -d $JENKINS_HOME -s /bin/bash -U jenkins  
  
RUN curl --create-dirs -sSLo ${JENKINS_HOME}/slave.jar http://repo.jenkins-
ci.org/public/org/jenkins-ci/main/remoting/2.56/remoting-2.56.jar \  
&& chmod 755 ${JENKINS_HOME} \  
&& chmod 644 ${JENKINS_HOME}/slave.jar  
  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
  
# Volumes  
VOLUME /var/lib/jenkins  
# Downgrade User  
USER jenkins  
  
# Set directory, install gemfile  
WORKDIR $JENKINS_HOME  
  
# Run Jenkins Slave  
ENTRYPOINT ["jenkins-slave"]  

