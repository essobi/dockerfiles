FROM debian:stable-slim  
  
ENV CONJUR_MAJOR_VERSION 4  
  
RUN apt-get update -y &&\  
apt-get install -y curl jq sudo software-properties-common openssl gpgv
python3-pip build-essential libssl-dev libffi-dev python-dev vim iputils-ping  
  
RUN curl -LO https://github.com/cyberark/conjur-
cli/releases/download/v5.4.0/conjur_5.4.0-1_amd64.deb &&\  
dpkg -i conjur_5.4.0-1_amd64.deb &&\  
rm -f conjur_5.4.0-1_amd64.deb &&\  
curl -sSL https://raw.githubusercontent.com/cyberark/summon/master/install.sh
| bash &&\  
curl -sSL https://raw.githubusercontent.com/cyberark/summon-
conjur/master/install.sh | bash  
  
RUN apt-get clean &&\  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
VOLUME /scripts /pem  
  
CMD ["sleep","infinity"]  

