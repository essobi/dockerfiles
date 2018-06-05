FROM ubuntu:xenial  
  
MAINTAINER Joachim Wickman <joachim@wickman.in>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y -qq && \  
apt-get install -y git-core subversion mercurial nano sudo wget \  
build-essential libssl-dev libncurses5-dev unzip gawk zlib1g-dev && \  
  
# clean up  
apt-get remove -y openssh-client manpages manpages-dev krb5-locales locales &&
\  
apt-get -y autoremove && \  
apt-get clean && \  
  
# add user  
useradd -m openwrt && \  
echo 'openwrt ALL=NOPASSWD: ALL' > /etc/sudoers.d/openwrt  
  
USER openwrt  
  
# clone openwrt repo: Chaos Calmer 15.05  
RUN cd ~ && git clone \--depth=1 git://git.openwrt.org/15.05/openwrt.git && \  
openwrt/scripts/feeds update -a  
  
CMD ["/bin/bash"]  

