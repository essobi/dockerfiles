FROM jenkins/jenkins:lts  
  
# Change user to root, as docker-in-docker won't work as the jenkins user
(even  
# with group addition), at least on Mac  
USER root  
# Add symlinks for Docker auth files to Jenkins home. Docker looks in the  
# current users' context  
RUN ln -s "${JENKINS_HOME}/.dockercfg" "/root/.dockercfg" \  
&& ln -s "${JENKINS_HOME}/.docker" "/root/.docker"  
RUN curl -fsSL get.docker.com | sh \  
&& apt-get clean  
  
RUN apt-get update \  
&& apt-get install -y golang \  
&& GOPATH=/root/go go get -u github.com/awslabs/amazon-ecr-credential-
helper/ecr-login/cli/docker-credential-ecr-login \  
&& mv /root/go/bin/docker-credential-ecr-login /usr/local/bin/ \  
&& rm -rf /root/go \  
&& apt-get purge -y golang \  
&& apt-get autoremove -y  

