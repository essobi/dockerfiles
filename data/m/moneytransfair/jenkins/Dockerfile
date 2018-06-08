# Based on https://github.com/jenkinsci/docker/blob/master/README.md  
FROM jenkins/jenkins:lts  
  
USER root  
  
RUN apt-get update && apt-get install -y less maven sudo  
  
# Install docker cli  
RUN curl "https://get.docker.com/builds/`uname -s`/`uname -m`/docker-
latest.tgz" > docker.tgz \  
&& tar -xvzf docker.tgz \  
&& mv docker/* /usr/bin \  
&& rm -rf docker.tgz docker  
  
# Add script and custom entrypoint to fix docker socket permissions  
COPY docker-permissions.sh /opt/docker-permissions.sh  
COPY custom-jenkins.sh /opt/custom-jenkins.sh  
  
# Allow user jenkins to fix the docker socket permissions  
# From https://blog.virtualzone.de/2017/06/let-jenkins-build-docker-
images.html  
# From https://stackoverflow.com/questions/42164653/docker-in-docker-
permissions-error  
# From https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-
ci/  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
# drop back to the regular jenkins user - good practice  
USER jenkins  
  
ENTRYPOINT ["/bin/tini", "--", "/opt/custom-jenkins.sh"]  

