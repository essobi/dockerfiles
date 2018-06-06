FROM jenkins/jenkins:lts  
  
USER root  
  
ENV CONJUR_MAJOR_VERSION=4  
  
RUN apt-get update &&\  
apt-get install -qy git apt-utils curl dpkg jq libexpat1-dev libpython2.7-dev
python2.7-dev vim sudo &&\  
apt-get install -f -qy &&\  
rm -rf /var/lib/apt/lists/* &&\  
curl -sSL https://raw.githubusercontent.com/cyberark/summon/master/install.sh
| bash &&\  
curl -sSL https://raw.githubusercontent.com/cyberark/summon-
conjur/master/install.sh | bash &&\  
curl -L -O https://github.com/cyberark/conjur-
cli/releases/download/v5.4.0/conjur_5.4.0-1_amd64.deb &&\  
dpkg -i conjur_5.4.0-1_amd64.deb &&\  
apt-get install -f -y &&\  
curl -fsSL get.docker.com -o get-docker.sh &&\  
sh get-docker.sh &&\  
usermod -aG docker jenkins &&\  
apt-get clean &&\  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
VOLUME /scripts /pem  
  
USER jenkins  
  
EXPOSE 8080 50000

