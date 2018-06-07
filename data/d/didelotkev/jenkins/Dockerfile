FROM jenkins/jenkins:lts  
  
ENV JENKINS_OPTS --httpPort=3000  
# Needed to init jenkins admin user  
COPY custom.groovy /usr/share/jenkins/ref/init.groovy.d/custom.groovy  
  
USER root  
  
# Install docker CLI  
RUN curl -fsSLO
https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \  
&& tar xzvf docker-17.04.0-ce.tgz \  
&& mv docker/docker /usr/local/bin \  
&& rm -r docker docker-17.04.0-ce.tgz  
  
EXPOSE 8080  
EXPOSE 50000  
VOLUME /var/jenkins_home  
  
USER jenkins  

