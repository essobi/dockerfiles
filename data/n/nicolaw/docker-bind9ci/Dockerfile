FROM ubuntu:trusty  
  
RUN apt-get -qq -o Dpkg::Use-Pty=0 update && \  
apt-get -qq -o Dpkg::Use-Pty=0 install -y --no-install-recommends \  
software-properties-common python-software-properties \  
< /dev/null > /dev/null  
  
RUN add-apt-repository ppa:nicolaw/blip  
  
RUN apt-get -qq -o Dpkg::Use-Pty=0 update && apt-get install -y \  
bind9 \  
bind9-host \  
bind9utils \  
libyaml-perl \  
perl \  
curl \  
rsync \  
psmisc \  
git \  
xz-utils \  
dnsutils \  
moreutils \  
libwww-perl \  
devscripts \  
quilt \  
debhelper \  
blip \  
&& rm -rf /var/lib/apt/lists/*  
  

