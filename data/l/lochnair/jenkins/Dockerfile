FROM lochnair/base:alpine-jre8  
  
LABEL Description="Docker image for Jenkins"  
  
RUN \  
apk add \  
\--no-cache \  
\--update \  
coreutils \  
docker \  
openjdk8-jre \  
openssh-client \  
ttf-dejavu \  
unzip  
  
# Jenkins version to install  
ARG JENKINS_VER="2.60.2"  
# Install Jenkins  
RUN \  
curl -o /app/jenkins.war -L "http://mirrors.jenkins.io/war-
stable/${JENKINS_VER}/jenkins.war" && \  
curl -o /app/jenkins.war.sha256 -L "http://mirrors.jenkins.io/war-
stable/${JENKINS_VER}/jenkins.war.sha256" && \  
cd /app && \  
sha256sum jenkins.war.sha256 || exit 1 && \  
rm jenkins.war.sha256 && \  
cd -  
  
# Add container user to Docker group  
RUN \  
usermod -aG docker cont  
  
## Environment variables  
ENV DOCKER_HOST="unix:///var/run/docker.sock"  
ENV JENKINS_HOME="/config"  
ENV JENKINS_OPTS="--httpListenAddress=0.0.0.0 --httpPort=8080
-Djava.awt.headless=true"  
VOLUME /config  
  
COPY root/ /  

