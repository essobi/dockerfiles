FROM jenkins/jenkins:lts  
  
USER root  
  
RUN apt-get update &&\  
apt-get install -qy git apt-utils curl dpkg jq libexpat1-dev libpython2.7-dev
python2.7-dev vim &&\  
apt-get install -f -qy &&\  
rm -rf /var/lib/apt/lists/* &&\  
curl -L -O https://github.com/cyberark/conjur-
cli/releases/download/v5.4.0/conjur_5.4.0-1_amd64.deb &&\  
dpkg -i conjur_5.4.0-1_amd64.deb &&\  
apt-get install -f -y &&\  
rm -f conjur_5.4.0-1_amd64.deb &&\  
curl -fsSL get.docker.com -o get-docker.sh &&\  
sh get-docker.sh &&\  
usermod -aG docker jenkins &&\  
curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose &&\  
chmod +x /usr/local/bin/docker-compose &&\  
apt-get clean &&\  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
USER jenkins  
  
VOLUME /cDemo /demo_cDemo_jenkins  
  
EXPOSE 8080 50000

