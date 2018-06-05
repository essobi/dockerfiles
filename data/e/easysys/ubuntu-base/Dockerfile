FROM ubuntu:14.04  
MAINTAINER bexio ag <ops@bexio.com>  
  
# Use non interactive package management.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install helpers and utilities  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ant \  
curl \  
git \  
less \  
openssh-client \  
python-software-properties \  
software-properties-common \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add the S6 Overlay init system.  
ARG s6_overlay_version=1.21.2.1  
RUN set -ex \  
&& curl -sL https://github.com/just-
containers/s6-overlay/releases/download/v${s6_overlay_version}/s6-overlay-
amd64.tar.gz \  
| tar -xzC /  
  
# Add ssh key helper.  
ADD with_ssh_key.sh /sbin/with_ssh_key  
  

