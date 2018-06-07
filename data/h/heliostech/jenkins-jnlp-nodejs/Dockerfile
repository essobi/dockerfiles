FROM ruby:2.3  
MAINTAINER Camille Meulien <camille.meulien@gmail.com>  
  
COPY entrypoint.sh /usr/bin/  
RUN chmod 755 /usr/bin/entrypoint.sh  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
  
#  
# Install Java  
#  
RUN apt-get update \  
&& apt-get install -y openjdk-7-jre-headless  
  
#  
# Install NodeJS  
#  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get install --yes nodejs build-essential  
  
RUN npm install -g bower gulp  
  
#  
# Install Jenkins remoting jar  
#  
ARG JENKINS_REMOTING_VERSION=2.62.4  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${JENKINS_REMOTING_VERSION}/remoting-${JENKINS_REMOTING_VERSION}.jar
\  
&& useradd -d ${HOME} -m jenkins-slave \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
#  
# End  
#  
ENV HOME=/home/jenkins-slave  
USER jenkins-slave  
VOLUME ${HOME}  
WORKDIR ${HOME}  

