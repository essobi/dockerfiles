FROM debian:jessie  
  
#  
# Install wget/ssh/cron/vim/nodejs/npm via apt  
#  
RUN apt-get -qq update && \  
apt-get -qq install --no-install-recommends \  
wget \  
vim \  
curl \  
sudo \  
cron \  
openssh-client \  
git \  
npm && \  
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \  
apt-get -qq update && \  
apt-get -qq install nodejs && \  
ln -s /usr/local/bin/node /usr/local/bin/nodejs && \  
apt-get -qq autoremove && \  
apt-get -qq autoclean && \  
apt-get -qq clean all && \  
rm -rf /var/cache/apk/* /tmp/* /var/lib/apt/lists/*  
  
# Install etcd-load  
RUN npm install -g etcd-load  
  
#  
# Download kubectl binary  
#  
ARG K8S_VERSION="1.5.2"  
RUN wget --no-verbose http://storage.googleapis.com/kubernetes-
release/release/v${K8S_VERSION}/bin/linux/amd64/kubectl -O
/usr/local/bin/kubectl && \  
chmod 555 /usr/local/bin/kubectl  
  
# Move scripts to WORKDIR  
WORKDIR /root  
COPY scripts/* ./  
COPY crontab /etc/cron.d/backup  
COPY Dockerfile entrypoint.sh /  
  
CMD ["/entrypoint.sh"]  

