FROM ubuntu:14.04  
MAINTAINER Jainish Shah <jainishshah@yahoo.com>  
  
# Let's start with some basic stuff.  
RUN apt-get update -qq && apt-get install -qqy nano curl \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables  
  
# Install Java 8  
RUN apt-get install -y software-properties-common python-software-properties
&& apt-add-repository -y ppa:webupd8team/java && apt-get update && echo
"oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" |
debconf-set-selections && apt-get install -y oracle-java8-installer  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
# Install Docker from Docker Inc. repositories.  
RUN curl -sSL https://get.docker.com/ | sh  
  
# Install the wrapper script from
https://raw.githubusercontent.com/docker/docker/master/hack/dind.  
ADD ./dind /usr/local/bin/dind  
RUN chmod +x /usr/local/bin/dind  
  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
  
ENV DOCKER_COMPOSE_VERSION 1.11.2  
RUN wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | apt-key
add -  
RUN sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ >
/etc/apt/sources.list.d/jenkins.list'  
RUN apt-get update && apt-get install -y zip supervisor jenkins git && rm -rf
/var/lib/apt/lists/*  
RUN usermod -a -G docker jenkins  
ENV JENKINS_HOME /var/lib/jenkins  
VOLUME /var/lib/jenkins  
  
# Install Docker Compose  
RUN curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
#Install JFrog CLI and Helm CLI  
RUN curl -fL https://getcli.jfrog.io | sh && mv jfrog /usr/local/bin/jfrog &&
chmod 777 /usr/local/bin/jfrog  
RUN curl -fL -O https://storage.googleapis.com/kubernetes-
helm/helm-v2.9.0-linux-amd64.tar.gz && tar -xvf helm-v2.9.0-linux-amd64.tar.gz
&& mv linux-amd64/helm /usr/local/bin/helm && rm -f helm-v2.9.0-linux-
amd64.tar.gz && chmod 777 /usr/local/bin/helm  
RUN chmod +x /usr/local/bin/docker-compose  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 8080  
CMD ["/usr/bin/supervisord"]  

