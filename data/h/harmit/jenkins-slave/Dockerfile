FROM java:8-jdk  
  
MAINTAINER Khorevaa@gmail.com  
  
ENV JENKINS_SWARM_VERSION 3.3  
ENV RANCHER_CLI_VERSION v0.5.0  
ENV HOME /home/jenkins-slave  
ENV WORKDIR /var/jenkins_home  
  
RUN useradd -c "Jenkins Slave user" -d $HOME -m jenkins-slave  
RUN curl --create-dirs -sSLo $HOME/swarm-client-$JENKINS_SWARM_VERSION.jar
https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION.jar  
#ADD swarm-client-3.3.jar $HOME/swarm-client-3.3.jar  
#We install newest docker into our docker in docker container  
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz \  
&& tar --strip-components=1 -xvzf docker-latest.tgz -C /usr/local/bin \  
&& chmod +x /usr/local/bin/docker  
  
# install Rancher CLI  
#RUN curl -fsSLO
https://github.com/rancher/cli/releases/download/$RANCHER_CLI_VERSION/rancher-
linux-amd64-$RANCHER_CLI_VERSION.tar.gz \  
# && tar --strip-components=2 -xzvf rancher-linux-
amd64-$RANCHER_CLI_VERSION.tar.gz -C /usr/local/bin \  
# && chmod +x /usr/local/bin/rancher  
#RUN rm rancher-linux-amd64-$RANCHER_CLI_VERSION.tar.gz  
VOLUME /var/lib/docker  
VOLUME /var/jenkins_home  
  
WORKDIR /var/jenkins_home  
  
#ENV JENKINS_USERNAME jenkins  
#ENV JENKINS_PASSWORD jenkins  
#ENV JENKINS_MASTER http://jenkins:8080  
ADD cmd.sh /cmd.sh  
  
CMD /bin/bash /cmd.sh  

