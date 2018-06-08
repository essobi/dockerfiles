# Ubuntu base  
#  
# Updates packages and configure  
  
FROM ubuntu:xenial-20160809  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
  
# 1) Add some useful environment  
# 2) Configure timezone and locale  
# 3) Make a fake lsb_release command  
# 4) Make sure the package repository is up to date  
ARG APT_CACHER_NG  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8 HOME=/root \  
DEBIAN_FRONTEND=noninteractive TZ=Asia/Bangkok DISTRIB_CODENAME=xenial  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo "$TZ" > /etc/timezone && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure -f noninteractive locales && \  
dpkg-reconfigure -f noninteractive tzdata && \  
update-locale LANG=en_US.UTF-8 && \  
echo '#!/bin/bash\necho '$DISTRIB_CODENAME > /usr/bin/lsb_release && \  
chmod +x /usr/bin/lsb_release && \  
[ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy  

