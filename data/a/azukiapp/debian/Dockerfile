# The container includes:  
#  
# azukiapp/debian:  
# * Debian 8.0, 8, jessie  
#  
  
FROM debian:jessie  
MAINTAINER Azuki <support@azukiapp.com>  
  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# install default packages  
# and make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by
default  
RUN packages=' \  
locales \  
python \  
curl \  
wget \  
vim \  
git-core \  
ca-certificates \  
' \  
set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $packages \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
&& apt-get autoremove --purge \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LANG en_US.utf8  

