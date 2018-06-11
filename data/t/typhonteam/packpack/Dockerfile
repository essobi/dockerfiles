FROM debian:stretch  
MAINTAINER Tech <tech@typhon.com>  
  
# Fix missing locales  
ENV LC_ALL="C.UTF-8" LANG="C.UTF-8"  
# Skip interactive post-install scripts  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Don't install recommends  
RUN echo 'apt::install-recommends "false";' > /etc/apt/apt.conf.d/00recommends  
  
# Enable extra repositories  
RUN apt-get update && apt-get install -y --force-yes \  
apt-transport-https \  
curl \  
wget \  
gnupg \  
ca-certificates  
  
# Install base toolset  
RUN apt-get update && apt-get install -y --force-yes \  
sudo \  
git \  
build-essential \  
cmake \  
gdb \  
ccache \  
devscripts \  
debhelper \  
cdbs \  
fakeroot \  
lintian \  
equivs \  
rpm \  
alien \  
dh-systemd  
  
# Install varnish  
RUN curl -s
https://packagecloud.io/install/repositories/varnishcache/varnish60/script.deb.sh
| bash  
RUN apt-get update && apt-get install -y --force-yes varnish-dev  
  
# Enable sudo without password  
RUN echo '%adm ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# Fix invoke-rc.d  
RUN sed -i 's/101/0/' /usr/sbin/policy-rc.d  

