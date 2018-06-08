FROM alpine:3.6  
MAINTAINER Dmitry Karikh <the.dr.hax@gmail.com>  
  
# Slave settings  
ENV JENKINS_MASTER_USERNAME="jenkins" \  
JENKINS_MASTER_PASSWORD="jenkins" \  
JENKINS_MASTER_URL="http://jenkins:8080/" \  
JENKINS_SLAVE_ROOT="/root/jenkins-slave" \  
JENKINS_SLAVE_MODE="exclusive" \  
JENKINS_SLAVE_NAME="swarm-$RANDOM" \  
JENKINS_SLAVE_WORKERS="1" \  
JENKINS_SLAVE_LABELS="" \  
  
# Preinstall packages at startup  
# see entrypoint.d/install-packages.sh  
REQUIRED_PACKAGES=""  
RUN apk --no-cache add openjdk8-jre wget git  
  
# Install Jenkins slave (swarm) and other scripts  
ADD root/ /  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/swarm.sh"]  

