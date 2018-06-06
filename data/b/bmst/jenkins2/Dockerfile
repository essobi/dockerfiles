FROM jenkinsci/jenkins:2.107.1  
USER root  
  
RUN apt-get update && \  
apt-get install -y wget git mercurial zip graphviz sudo && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JENKINS_HOME /var/jenkins_home  
  
# install docker  
RUN wget -O - https://get.docker.com | sh  
RUN usermod -G docker jenkins  
RUN echo 'DOCKER_OPTS="-H tcp://0.0.0.0:4243 -H unix:///var/run/docker.sock"'
>> /etc/default/docker  
  
# Install the plugins using jenkins itself.  
COPY plugins.txt /plugins.txt  
RUN install-plugins.sh $(cat /plugins.txt)  
  
# Disable the upgrade wizard  
RUN echo -n 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state
&& \  
echo -n 2.0 >
/usr/share/jenkins/ref/jenkins.install.InstallUtil.lastExecVersion  
  
RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref  
  
USER jenkins  
  

