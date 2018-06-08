FROM java:8-jre  
  
MAINTAINER Knut Ahlers <knut@ahlers.me>  
  
ENV JENKINS_SWARM_VERSION 1.26  
  
ADD jenkins-slave.sh /usr/local/bin/jenkins-slave.sh  
  
RUN bash -c "if ! [ -e /usr/lib/apt/methods/https ]; then apt-get update &&
apt-get install -y apt-transport-https; fi"  
  
RUN useradd -c "Jenkins Slave user" -d /home/jenkins -u 233 -m jenkins \  
&& curl --create-dirs -sSLo /usr/share/jenkins/swarm-
client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar \  
http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-
ci/plugins/swarm-client/$JENKINS_SWARM_VERSION/swarm-
client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar \  
&& chmod 755 /usr/share/jenkins \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 \  
&& sh -c "echo deb https://get.docker.io/ubuntu docker main >
/etc/apt/sources.list.d/docker.list" \  
&& apt-get update \  
&& apt-get install -y git-core lxc-docker sudo make unzip \  
&& echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \  
&& chmod 755 /usr/local/bin/jenkins-slave.sh \  
&& curl -sSLo /tmp/s3sync.zip
https://gobuilder.me/get/github.com/Luzifer/s3sync/s3sync_master_linux-
amd64.zip \  
&& unzip /tmp/s3sync.zip -d /tmp/ \  
&& mv /tmp/s3sync/s3sync /usr/local/bin/  
  
  
USER jenkins  
  
VOLUME /home/jenkins  
  
ENTRYPOINT ["/usr/local/bin/jenkins-slave.sh"]  

