FROM openjdk:8-jre  
  
RUN apt-get update && \  
apt-get -y install lsb-release software-properties-common apt-transport-https  
  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add - && \  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(.
/etc/os-release; echo "$ID") $(lsb_release -cs) stable" && \  
apt-get update && \  
apt-get -y install docker-ce  
  
RUN curl -O https://repo.jenkins-ci.org/public/org/jenkins-ci/plugins/job-dsl-
core/1.66/job-dsl-core-1.66-standalone.jar  

