FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y \  
python-pip \  
curl \  
gnupg2 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV ETCD_VERSION 2.1.3  
RUN pip install awscli  
RUN curl -L
https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz -o /tmp/etcd.tar.gz && \  
cd tmp && \  
tar -xzf /tmp/etcd.tar.gz && \  
mv /tmp/etcd-v${ETCD_VERSION}-linux-amd64/etcdctl /usr/bin/etcdctl && \  
rm -rf /tmp/*  
  
RUN useradd -m decrypt  
VOLUME "/home/decrypt/keys"  
USER decrypt  
WORKDIR /home/decrypt  
  
ADD bin/get-app-environment.sh /usr/bin/get-app-environment.sh  
CMD [ "/usr/bin/get-app-environment.sh" ]  
  

