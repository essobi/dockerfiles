FROM jenkins/jenkins:2.90  
# need to install some stuff  
USER root  
RUN apt-get update && apt-get install -y \  
git \  
apt-transport-https \  
ca-certificates \  
curl \  
lsb-release \  
software-properties-common  
  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add -  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable"  
  
  
RUN apt-get update && apt-get install -y \  
docker-ce  
  
  
ENV JENKINS_HOME "/var/jenkins_home"  
ENV JENKINS_HOME_PLUGINS "/usr/share/jenkins/ref/plugins"  
#RUN /usr/local/bin/install-plugins.sh \  
# build-pipeline-plugin \  
# cloudbees-folder \  
# dashboard-view \  
# gradle \  
# job-dsl \  
# plugin-usage-plugin \  
# build-flow-plugin \  
# buildgraph-view \  
# build-metrics \  
# build-timeout \  
# claim \  
# config-file-provider \  
# configurationslicing \  
# console-column-plugin \  
# ansicolor \  
# greenballs \  
# htmlpublisher \  
# credentials \  
# ssh-credentials \  
# github \  
# ghprb \  
# workflow-scm-step \  
# subversion \  
# git \  
# git-client \  
# git-parameter \  
# git-changelog \  
# pipeline-build-step \  
# workflow-aggregator \  
# parameterized-trigger \  
# slave-setup \  
# cisco-spark \  
# multi-slave-config-plugin \  
# marathon \  
# ssh-slaves \  
# docker-plugin \  
# docker-workflow \  
# docker-slaves \  
# docker-build-publish \  
# simple-travis-runner  
  
USER jenkins  
  
  
VOLUME $JENKINS_HOME  
EXPOSE 50000  
EXPOSE 8080  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  

