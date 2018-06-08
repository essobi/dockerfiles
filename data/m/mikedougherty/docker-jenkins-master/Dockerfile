FROM jenkins:latest  
  
MAINTAINER Mike Dougherty <mike.dougherty@docker.com>  
  
ENV REFRESHED_AT 2015-04-16  
# Install docker and put jenkins in the docker group  
USER root  
  
RUN curl -sSL https://test.docker.com/ubuntu/ -o install-docker.sh \  
&& [ "$( shasum install-docker.sh | cut -d ' ' -f 1 )" =
"fb5ff1718d5b66642e1638f21eaf63f4faa2e9a6" ] \  
&& sh install-docker.sh \  
&& apt-get clean \  
&& rm -rf install-docker.sh /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& docker --version  
  
RUN usermod -aG docker jenkins  
USER jenkins  
  
## TODO: SSL stuff, e.g.:  
# COPY https.pem /var/lib/jenkins/cert  
# COPY https.key /var/lib/jenkins/pk  
# ENV JENKINS_OPTS --httpPort=-1 --httpsPort=8083
--httpsCertificate=/var/lib/jenkins/cert --httpsPrivateKey=/var/lib/jenkins/pk  
COPY plugins.txt /plugins.txt  
RUN plugins.sh /plugins.txt  
  
COPY ref /usr/share/jenkins/ref  

