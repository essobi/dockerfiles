FROM vicamo/android-pdk:xenial-oracle-java-6  
  
# 5C5364B55E51A24C: Launchpad PPA for Ubuntu Phablet Team  
# C2518248EEA14886: Launchpad VLC  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial multiverse" >
/etc/apt/sources.list.d/xenial_multiverse.list \  
&& echo "deb-src http://archive.ubuntu.com/ubuntu xenial multiverse" >>
/etc/apt/sources.list.d/xenial_multiverse.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu xenial-updates multiverse" >>
/etc/apt/sources.list.d/xenial_multiverse.list \  
&& echo "deb-src http://archive.ubuntu.com/ubuntu xenial-updates multiverse"
>> /etc/apt/sources.list.d/xenial_multiverse.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu xenial-security multiverse" >>
/etc/apt/sources.list.d/xenial_multiverse.list \  
&& echo "deb-src http://archive.ubuntu.com/ubuntu xenial-security multiverse"
>> /etc/apt/sources.list.d/xenial_multiverse.list \  
&& echo "deb http://ppa.launchpad.net/phablet-team/tools/ubuntu xenial main" >
/etc/apt/sources.list.d/ppa.launchpad.net_phablet-team_xenial.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys 5C5364B55E51A24C
\  
&& apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys C2518248EEA14886
\  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
abootimg \  
cpio \  
g++-4.8-multilib \  
imagemagick \  
kmod \  
libasound2-dev:i386 \  
libesd0-dev:i386 \  
libpulse-dev:i386 \  
openssh-client \  
phablet-tools \  
phablet-tools-citrain \  
pxz \  
software-properties-common \  
ubuntu-device-flash \  
ubuntu-emulator \  
&& apt-get clean \  
&& rm -f /var/lib/apt/lists/*_dists_*  

