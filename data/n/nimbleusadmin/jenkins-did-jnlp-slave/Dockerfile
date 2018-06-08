FROM jenkinsci/jnlp-slave  
MAINTAINER Nimbleus, LLC  
  
USER root  
  
# Install latest version of docker  
RUN apt-get update  
RUN apt-get install -y curl  
RUN apt-get install -y apt-transport-https  
RUN apt-get install -y ca-certificates  
RUN apt-get install -y software-properties-common  
RUN curl -fsSL https://yum.dockerproject.org/gpg | apt-key add -  
RUN apt-key fingerprint 58118E89F3A912897C070ADBF76221572C52609D  
RUN add-apt-repository "deb https://apt.dockerproject.org/repo/
debian-$(lsb_release -cs) main"  
RUN apt-get update  
RUN apt-get -y install docker-engine  
  
RUN usermod -G docker jenkins  
  
USER jenkins  
  
ENTRYPOINT ["jenkins-slave"]  
  

