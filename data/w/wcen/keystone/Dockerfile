FROM ubuntu:14.04.5  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y cloud-archive:mitaka && \  
apt-get update && apt-get -y dist-upgrade && \  
apt-get install -y keystone && \  
apt-get install -y python-openstackclient  
  
# packages for ldap  
RUN apt-get install -y python-dev && \  
apt-get install -y python-pip && \  
apt-get install -y python-ldap && \  
apt-get install -y libldap2-dev && \  
apt-get install -y libsasl2-dev && \  
pip install ldappool  
  
# Download kubectl  
ENV KUBE_VERSION 1.5.1  
RUN apt-get install -y curl && \  
curl -O https://storage.googleapis.com/kubernetes-
release/release/v${KUBE_VERSION}/bin/linux/amd64/kubectl && \  
chmod +x kubectl  
  
COPY config /etc/keystone  
COPY entrypoint.sh /entrypoint.sh  
  
RUN su -s /bin/sh -c "keystone-manage db_sync" keystone  
  
ENTRYPOINT ["/entrypoint.sh"]  

