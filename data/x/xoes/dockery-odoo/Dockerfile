FROM docker:latest  
  
ENV TERRAFORM_VERSION 0.11.7  
ENV CONSUL_VERSION 1.0.7  
ENV ETCD_VERSION v3.3.5  
ENV RANCHER_VERSION v2.0.0  
ENV KUBECTL_VERSION v1.10.2  
ENV ETCDCTL_API 3  
RUN apk add --no-cache py-pip ca-certificates openssl git unzip wget  
RUN update-ca-certificates  
  
# Docker Compose  
RUN pip install docker-compose  
  
# Grab Terraform, Consul, ETC & kubectl  
RUN cd /tmp && \  
wget
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin && \  
wget
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
&& \  
unzip consul_${CONSUL_VERSION}_linux_amd64.zip -d /usr/local/bin && \  
wget
https://github.com/coreos/etcd/releases/download/${ETCD_VERSION}/etcd-${ETCD_VERSION}-linux-
amd64.tar.gz && \  
tar -zxvf etcd-${ETCD_VERSION}-linux-amd64.tar.gz etcd-${ETCD_VERSION}-linux-
amd64/etcdctl -C /usr/local/bin/ --strip-components=1 && \  
wget
https://github.com/rancher/cli/releases/download/${RANCHER_VERSION}/rancher-
linux-amd64-${RANCHER_VERSION}.tar.gz && \  
tar -zxvf rancher-linux-amd64-${RANCHER_VERSION}.tar.gz -C /usr/local/bin/
--strip-components=2 && \  
wget https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \  
mv ./kubectl /usr/local/bin && \  
rm -rf /tmp/*  
  
RUN chmod -R +x /usr/local/bin  
  
# Some pip libraries for interacting with apis  
RUN pip install click hammock odoorpc websocket-client

