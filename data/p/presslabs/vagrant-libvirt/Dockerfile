FROM ubuntu:xenial  
MAINTAINER Presslabs <ping@presslabs.com>  
  
ENV VAGRANT_VERSION=1.9.5 \  
VAGRANT_LIBVIRT_VERSION=0.0.40 \  
VAGRANT_DEFAULT_PROVIDER=libvirt  
  
RUN set -ex \  
&& apt-get update && apt-get install --no-install-recommends -y \  
# install base packages  
build-essential \  
ca-certificates \  
iputils-ping \  
libvirt-bin \  
libvirt-dev \  
libxml2-dev \  
libxslt-dev \  
openssh-client \  
python-dev \  
python-pip \  
python-setuptools \  
python-wheel \  
ruby-dev \  
ruby-libvirt \  
wget \  
zlib1g-dev \  
  
&& wget -O /tmp/vagrant_${VAGRANT_VERSION}_x86_64.deb
"https://releases.hashicorp.com/vagrant/${VAGRANT_VERSION}/vagrant_${VAGRANT_VERSION}_x86_64.deb"
\  
&& dpkg -i /tmp/vagrant_${VAGRANT_VERSION}_x86_64.deb \  
&& rm /tmp/vagrant_${VAGRANT_VERSION}_x86_64.deb \  
  
# install vagrant libvirt plugin  
&& CONFIGURE_ARGS='with-ldflags=-L/opt/vagrant/embedded/lib with-libvirt-
include=/usr/include/libvirt with-libvirt-lib=/usr/lib' \  
GEM_HOME=~/.vagrant.d/gems \  
GEM_PATH=$GEM_HOME:/opt/vagrant/embedded/gems \  
PATH=/opt/vagrant/embedded/bin:$PATH \  
vagrant plugin install --plugin-version $VAGRANT_LIBVIRT_VERSION vagrant-
libvirt \  
  
&& vagrant plugin install sahara \  
&& vagrant plugin install fog \  
  
# install cleanup as per https://docs.docker.com/engine/userguide/eng-
image/dockerfile_best-practices/#apt-get  
&& rm -rf /var/lib/apt/lists/*  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT /usr/local/bin/docker-entrypoint.sh  

