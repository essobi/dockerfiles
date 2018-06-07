FROM ubuntu:16.04  
MAINTAINER Andy Kirkham  
  
# Command And Control node base definition  
  
ENV TF_VERSION="0.11.3"  
ENV PK_VERSION="1.2.1"  
ENV MV_VERSION="3.5.3"  
ENV ANT_VERSION="1.10.2"  
ENV HELM_VERSION="2.8.2"  
ENV KUBECTL_VERSION="1.9.0"  
  
# Command And Control node base definition  
  
WORKDIR /tmp  
ENV PKGS \  
ansible \  
git \  
ssh \  
subversion \  
curl \  
unzip \  
jq \  
awscli \  
openjdk-8-jdk \  
python-pip \  
cmake \  
autoconf \  
apt-utils \  
vim \  
file \  
wget \  
qt4-default \  
libapr1-dev \  
libsvn-dev \  
libsvncpp-dev \  
libsvncpp3 libsvn1  
  
WORKDIR /tmp  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential software-
properties-common \  
&& DEBIAN_FRONTEND=noninteractive apt-add-repository -y ppa:ansible/ansible \  
&& DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y $PKGS --no-install-
recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -sSL
https://launchpad.net/ubuntu/+archive/primary/+files/libjansson4_2.9-1_amd64.deb
> libjansson4_2.9-1_amd64.deb \  
&& DEBIAN_FRONTEND=noninteractive dpkg -i libjansson4_2.9-1_amd64.deb \  
&& rm -f libjansson4_2.9-1_amd64.deb \  
&& curl -sSL https://launchpad.net/ubuntu/+archive/primary/+files/libjansson-
dev_2.9-1_amd64.deb > libjansson-dev_2.9-1_amd64.deb \  
&& DEBIAN_FRONTEND=noninteractive dpkg -i libjansson-dev_2.9-1_amd64.deb \  
&& rm -f libjansson-dev_2.9-1_amd64.deb \  
&& curl -sSL
https://launchpad.net/ubuntu/+archive/primary/+files/libjansson4-dbgsym_2.9-1_amd64.ddeb
> libjansson4-dbgsym_2.9-1_amd64.ddeb \  
&& DEBIAN_FRONTEND=noninteractive dpkg -i libjansson4-dbgsym_2.9-1_amd64.ddeb
\  
&& rm -f libjansson4-dbgsym_2.9-1_amd64.ddeb \  
&& echo "export JAVA_HOME=\"/usr\"" >> /etc/bash.bashrc \  
&& echo "Loading Terraform ${TF_VERSION}" \  
&& curl -sSL
https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip
> terraform.zip \  
&& unzip terraform.zip \  
&& mv terraform /usr/local/bin/terraform \  
&& chmod 755 /usr/local/bin/terraform \  
&& rm -f terraform.zip \  
&& echo "Loading Packer ${PK_VERSION}" \  
&& curl -sSL
https://releases.hashicorp.com/packer/${PK_VERSION}/packer_${PK_VERSION}_linux_amd64.zip
> packer.zip \  
&& unzip packer.zip \  
&& mv packer /usr/local/bin/packer \  
&& chmod 755 /usr/local/bin/packer \  
&& rm -f packer.zip \  
&& echo "Loading Maven ${MV_VERSION}" \  
&& curl -sSL http://www-
eu.apache.org/dist/maven/maven-3/${MV_VERSION}/binaries/apache-
maven-${MV_VERSION}-bin.tar.gz > apache-maven-${MV_VERSION}-bin.tar.gz \  
&& tar -zxf apache-maven-${MV_VERSION}-bin.tar.gz \  
&& rm -f apache-maven-${MV_VERSION}-bin.tar.gz \  
&& mv apache-maven-${MV_VERSION} /usr/local \  
&& echo "export MVN_HOME=\"/usr/local/apache-maven-${MV_VERSION}\"" >>
/etc/bash.bashrc \  
&& echo "Loading Ant ${ANT_VERSION}" \  
&& curl -sSL http://www-eu.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz > apache-ant-${ANT_VERSION}-bin.tar.gz \  
&& tar -zxf apache-ant-${ANT_VERSION}-bin.tar.gz \  
&& rm -f apache-ant-${ANT_VERSION}-bin.tar.gz \  
&& mv apache-ant-${ANT_VERSION} /usr/local \  
&& echo "export ANT_HOME=\"/usr/local/apache-ant-${ANT_VERSION}\"" >>
/etc/bash.bashrc \  
&& echo "export PATH=\"$PATH:/usr/local/apache-
maven-${MV_VERSION}/bin:/usr/local/apache-ant-${ANT_VERSION}/bin\"" >>
/etc/bash.bashrc \  
&& echo "Loading Jansson 2.9.1" \  
&& curl -sSL
https://launchpad.net/ubuntu/+archive/primary/+files/libjansson4_2.9-1_amd64.deb
> libjansson4_2.9-1_amd64.deb \  
&& dpkg -i libjansson4_2.9-1_amd64.deb \  
&& rm -f libjansson4_2.9-1_amd64.deb \  
&& curl -sSL https://launchpad.net/ubuntu/+archive/primary/+files/libjansson-
dev_2.9-1_amd64.deb > libjansson-dev_2.9-1_amd64.deb \  
&& dpkg -i libjansson-dev_2.9-1_amd64.deb \  
&& rm -f libjansson-dev_2.9-1_amd64.deb \  
&& curl -sSL
https://launchpad.net/ubuntu/+archive/primary/+files/libjansson4-dbgsym_2.9-1_amd64.ddeb
> libjansson4-dbgsym_2.9-1_amd64.ddeb \  
&& dpkg -i libjansson4-dbgsym_2.9-1_amd64.ddeb \  
&& rm -f libjansson4-dbgsym_2.9-1_amd64.ddeb \  
# Because "apt-get install awscli" gives us a version that's too old.  
&& echo "Updating awscli" \  
&& apt-get remove -y awscli \  
&& curl -sSL "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" \  
&& unzip awscli-bundle.zip \  
&& ./awscli-bundle/install -i /usr/local/aws -b /usr/bin/aws \  
&& rm -rf awscli-bundle \  
&& rm -f awscli-bundle.zip \  
&& wget -q --https-only --timestamping \  
https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 \  
https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64 \  
&& chmod +x cfssl_linux-amd64 cfssljson_linux-amd64 \  
&& mv cfssl_linux-amd64 /usr/local/bin/cfssl \  
&& mv cfssljson_linux-amd64 /usr/local/bin/cfssljson \  
&& echo "Loading kubectl ${KUBECTL_VERSION}" \  
&& curl -o kubectl https://storage.googleapis.com/kubernetes-
release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl \  
&& chmod +x kubectl \  
&& mv kubectl /usr/local/bin/ \  
&& echo "Loading helm ${HELM_VERSION}" \  
&& curl -o helm-v${HELM_VERSION}-linux-amd64.tar.gz https://kubernetes-
helm.storage.googleapis.com/helm-v${HELM_VERSION}-linux-amd64.tar.gz \  
&& tar -zxf helm-v${HELM_VERSION}-linux-amd64.tar.gz \  
&& mv linux-amd64/helm /usr/local/bin/helm \  
&& rm -rf linux-amd64 \  
&& rm -f helm-v${HELM_VERSION}-linux-amd64.tar.gz \  
&& pip install --upgrade pip \  
&& pip install eb \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/* \  
&& mkdir -p /workspace  
WORKDIR /root  
  

