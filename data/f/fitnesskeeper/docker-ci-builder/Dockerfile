FROM amazonlinux:2  
# This is the location of the releases.  
ENV HASHICORP_RELEASES=https://releases.hashicorp.com  
# This is the release of Vault to pull in.  
ENV VAULT_VERSION=0.10.1  
# This is the release of Consul to pull in.  
ENV CONSUL_VERSION=1.0.7  
# Java and maven are required for OASIS build (to build scala lambdas).  
RUN yum install -y \  
unzip \  
wget \  
git \  
tar \  
jq \  
docker \  
python-pip \  
awscli \  
go \  
zip \  
java-1.8.0-openjdk-devel \  
maven \  
&& /usr/sbin/alternatives --auto java \  
&& /usr/sbin/alternatives --auto javac \  
&& yum remove -y java-1.7.0-openjdk \  
&& yum clean all \  
&& rm -rf /var/cache/yum  
RUN pip install docker-compose dumb-init  
  
# Installs node / npm and grunt. Also required for OASIS build (for grunt).  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \  
&& . ~/.nvm/nvm.sh \  
&& nvm install --lts \  
&& npm install -g grunt-cli  
  
RUN wget
${HASHICORP_RELEASES}/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
\  
&& unzip -d /bin vault_${VAULT_VERSION}_linux_amd64.zip \  
&& chmod +x /bin/vault  
  
RUN wget
${HASHICORP_RELEASES}/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
\  
&& unzip -d /bin consul_${CONSUL_VERSION}_linux_amd64.zip \  
&& chmod +x /bin/consul  
  
COPY scripts/check-dockerhub.sh /usr/local/bin/  
COPY scripts/get-latest-nonmerge-commit.sh /usr/local/bin/  
COPY scripts/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  

