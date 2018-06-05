FROM debian:8.3  
MAINTAINER Nico - Freifunk Hennef <nico@freifunk-hennef.de>  
  
ENV BATCTL_VERSION=2017.0  
ENV PACKAGES="build-essential checkinstall pkg-config curl libnl-genl-3-200
libnl-3-dev libnl-genl-3-200 libnl-genl-3-dev git gettext-base"  
ENV REMOVE_PACKAGES="build-essential checkinstall pkg-config libnl-3-dev
libnl-genl-3-dev"  
# Dollar sign for use in envsubst templates  
ENV DOLLAR='$'  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y $PACKAGES && \  
cd /usr/src && \  
curl -O https://downloads.open-
mesh.org/batman/stable/sources/batctl/batctl-${BATCTL_VERSION}.tar.gz && \  
tar xfz batctl-${BATCTL_VERSION}.tar.gz && \  
cd batctl-${BATCTL_VERSION} && \  
make && checkinstall -y make install && \  
cd .. && rm -rf batctl-${BATCTL_VERSION}* && \  
apt-get remove -y $REMOVE_PACKAGES && apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists  

