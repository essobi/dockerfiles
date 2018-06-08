FROM centos:centos7  
MAINTAINER Sam Lee <samlee@ea.com>  
  
# Need root to build image  
USER root  
  
# install dev tools  
RUN yum install -y \  
unzip \  
tar \  
gzip \  
curl \  
ca-certificates \  
openssl \  
wget && \  
yum clean all && rm -rf /var/cache/yum/*  
  
# install Hashicorp tools  
RUN export PACKER_VERSION=0.10.1 && \  
export VAGRANT_VERSION=1.8.5 && \  
wget --directory-prefix=/tmp
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
&& \  
unzip /tmp/packer_${PACKER_VERSION}_linux_amd64.zip -d /usr/local/bin && \  
wget --directory-prefix=/tmp
https://releases.hashicorp.com/vagrant/${VAGRANT_VERSION}/vagrant_${VAGRANT_VERSION}_x86_64.rpm
&& \  
rpm -i /tmp/vagrant_${VAGRANT_VERSION}_x86_64.rpm && \  
rm -rf /tmp/*  
  
# install Virtualbox (Example version: 5.0.14_105127_el7-1)  
RUN export VIRTUALBOX_VERSION=5.1.8_111374_el7-1.x86_64 && \  
mkdir -p /opt/virtualbox && \  
cd /etc/yum.repos.d/ && \  
wget http://download.virtualbox.org/virtualbox/rpm/el/virtualbox.repo && \  
yum install -y \  
dkms \  
kernel-devel && \  
yum -y groupinstall "Development Tools" && \  
if [ "${VIRTUALBOX_VERSION}" = "latest" ]; \  
then yum install -y VirtualBox-5.1 ; \  
else yum install -y VirtualBox-5.1-${VIRTUALBOX_VERSION} ; \  
fi  
  
# install docker  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.12.1  
ENV DOCKER_SHA256
05ceec7fd937e1416e5dce12b0b6e1c655907d349d52574319a1e875077ccb79  
  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v  
  
# install chefdk  
ENV LANG=en_US.UTF-8  
RUN curl -L https://www.opscode.com/chef/install.sh | bash -s -- -P chefdk  
  
# install kitchen-docker  
RUN chef gem install kitchen-docker  
  
# cleanup  
RUN set -x \  
&& yum clean all \  
&& rm -rf /var/cache/yum/*  
  
CMD ["bash"]  

