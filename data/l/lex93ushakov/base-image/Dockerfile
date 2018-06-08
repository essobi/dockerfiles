FROM ubuntu:16.04  
MAINTAINER Alex Ushakov <a93ushakov@gmail.com>  
  
RUN \  
echo "deb http://mirror.datacenter.by/ubuntu/ xenial main " >
/etc/apt/sources.list && \  
echo "deb http://mirror.datacenter.by/ubuntu/ xenial-security main restricted"
>> /etc/apt/sources.list  
  
# Community-maintained open-source software  
RUN \  
echo "deb http://mirror.datacenter.by/ubuntu/ xenial universe" >>
/etc/apt/sources.list && \  
echo "deb http://mirror.datacenter.by/ubuntu/ xenial-security universe" >>
/etc/apt/sources.list  
  
# Major bug fix updates produced after the final release of the distro  
RUN \  
echo "deb http://mirror.datacenter.by/ubuntu/ xenial-updates main restricted"
>> /etc/apt/sources.list && \  
echo "deb http://mirror.datacenter.by/ubuntu/ xenial-updates universe" >>
/etc/apt/sources.list  
  
RUN \  
apt-get update && \  
apt-get upgrade -y  
  
# software for quick container debugging  
RUN \  
apt-get install \  
-y \  
\--no-install-recommends \  
git \  
ca-certificates \  
wget \  
curl \  
vim-nox \  
tmux  
  
RUN rm -rf /var/lib/apt  
  
ONBUILD RUN apt-get update && apt-get upgrade -y  

