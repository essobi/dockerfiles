  
FROM jenkins/jenkins:lts  
  
USER root  
  
RUN apt-get update &&\  
apt-get install -qy git apt-utils curl dpkg jq libexpat1-dev libpython2.7-dev
python2.7-dev vim &&\  
apt-get install -f -qy &&\  
rm -rf /var/lib/apt/lists/* &&\  
curl -L -O https://github.com/cyberark/summon/releases/download/v0.6.5/summon-
linux-amd64.tar.gz &&\  
tar -C /usr/local/bin -xzvf summon-linux-amd64.tar.gz &&\  
curl -L -O https://github.com/cyberark/conjur-
cli/releases/download/v5.4.0/conjur_5.4.0-1_amd64.deb &&\  
dpkg -i conjur_5.4.0-1_amd64.deb &&\  
apt-get install -f -y &&\  
rm -f summon-linux-amd64.tar.gz &&\  
rm -f conjur_5.4.0-1_amd64.deb &&\  
curl -fsSL get.docker.com -o get-docker.sh &&\  
sh get-docker.sh &&\  
rm get-docker.sh &&\  
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/darwin/amd64/kubectl &&\  
chmod +x ./kubectl &&\  
mv ./kubectl /usr/local/bin/kubectl &&\  
usermod -aG docker jenkins &&\  
apt-get clean &&\  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
USER jenkins  
  
EXPOSE 8080 50000

