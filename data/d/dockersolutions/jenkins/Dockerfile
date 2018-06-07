FROM debian:jessie  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
# install all dependencies  
RUN (apt-get update &&\  
apt-get install -y curl daemon expect git-core jq mercurial net-tools
openjdk-7-jre-headless psmisc sudo unzip wget &&\  
rm -rf /var/lib/apt/lists/*)  
  
ENV JENKINS_HOME /var/lib/jenkins  
  
# install jenkins 1.653; originally downloaded from mirrors.jenkins-ci.org but
holy shit it's slow  
RUN (wget
"http://mirror1.net.one.com/jenkins/debian/binary/jenkins_1.653_all.deb" -O
/tmp/jenkins_1.653_all.deb &&\  
dpkg -i /tmp/jenkins_1.653_all.deb &&\  
rm /tmp/jenkins_1.653_all.deb &&\  
mkdir -p ${JENKINS_HOME}/plugins)  
  
# create symlink for persistent /usr/local/bin  
RUN (mkdir ${JENKINS_HOME}/bin &&\  
rm -rf /usr/local/bin &&\  
ln -sf ${JENKINS_HOME}/bin /usr/local/bin)  
  
# install docker-compose  
RUN (wget -O /usr/local/bin/docker-compose
"https://github.com/docker/compose/releases/download/1.21.0/docker-compose-
Linux-x86_64" &&\  
chmod +x /usr/local/bin/docker-compose)  
  
# install notary  
RUN (wget -O /usr/local/bin/notary
"https://github.com/docker/notary/releases/download/v0.4.3/notary-Linux-amd64"
&&\  
chmod +x /usr/local/bin/notary)  
  
# install docker client (we have to use CE here because licensing...)  
RUN (wget -O /tmp/docker-static.tgz
"https://download.docker.com/linux/static/stable/x86_64/docker-17.06.2-ce.tgz"
&&\  
cd /tmp &&\  
tar -vxzf docker-static.tgz &&\  
mv /tmp/docker/docker /usr/local/bin/docker &&\  
chmod +x /usr/local/bin/docker &&\  
rm -rf /tmp/docker /tmp/docker-static.tgz)  
  
# install kubectl  
RUN (wget -O /usr/local/bin/kubectl
"https://storage.googleapis.com/kubernetes-
release/release/v1.8.9/bin/linux/amd64/kubectl" &&\  
chmod +x /usr/local/bin/kubectl)  
  
COPY ./jenkins/ ${JENKINS_HOME}/  
COPY entrypoint.sh /entrypoint.sh  
  
# create jenkins user  
RUN (userdel jenkins &&\  
groupadd -g 510 jenkins &&\  
groupadd -g 998 docker &&\  
useradd -u 510 -g 510 -G docker -d ${JENKINS_HOME} jenkins &&\  
chown -R jenkins:jenkins ${JENKINS_HOME})  
  
# grant sudo access to jenkins user  
RUN (echo 'jenkins ALL = (ALL) NOPASSWD: ALL' > /etc/sudoers.d/jenkinsnosudo
&&\  
chmod 0440 /etc/sudoers.d/jenkinsnosudo)  
  
USER jenkins  
VOLUME ["/var/lib/jenkins"]  
EXPOSE 8080  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["java","-jar","/usr/share/jenkins/jenkins.war"]  

