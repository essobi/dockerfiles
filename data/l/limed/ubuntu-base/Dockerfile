# vim: set filetype=dockerfile  
FROM ubuntu:16.04  
MAINTAINER Ed Lim <limed@sudoers.org>  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
LANG="en_US.UTF-8" \  
LC_ALL="en_US.UTF-8" \  
LANGUAGE="en_US.UTF-8"  
# Does the following:  
# - Add the trusty-proposed repo  
# - enable multiverse on all repos  
# - Install some utilities  
# - Remove stuff  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ xenial-proposed restricted
main multiverse universe" >> /etc/apt/sources.list \  
&& sed -i "/^# deb.*multiverse/ s/^# //" /etc/apt/sources.list \  
&& apt-get --quiet update \  
&& apt-get install --no-install-recommends -qy bzip2 \  
tar \  
python \  
python-pip \  
python-software-properties \  
curl \  
apt-transport-https \  
ca-certificates \  
supervisor \  
openssl \  
software-properties-common \  
&& apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& apt-get purge -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ADD files/vimrc /root/.vimrc  
RUN chown root:root /root/.vimrc  
RUN mkdir -p /data  

