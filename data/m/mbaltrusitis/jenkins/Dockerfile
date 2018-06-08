FROM jenkins/jenkins:lts  
  
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"  
  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
  
USER root  
  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt \  
&& wget
https://download.docker.com/linux/static/stable/x86_64/docker-17.06.2-ce.tgz \  
&& tar xvzf docker-17.06.2-ce.tgz \  
&& mv docker/docker /usr/bin/docker \  
&& chmod +x /usr/bin/docker \  
&& rm -rf docker/ \  
&& groupadd \--gid 999 docker \  
&& usermod -aG staff,docker jenkins \  
&& apt-get update && apt-get install \--fix-missing -yq rsync python python-
pip \  
&& pip install ansible  
  
USER jenkins  

