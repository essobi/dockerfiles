FROM bmoorman/ubuntu:xenial  
  
ENV OPENVPN_USERNAME="**username**" \  
OPENVPN_PASSWORD="**password**" \  
OPENVPN_GATEWAY="Automatic" \  
OPENVPN_LOCAL_NETWORK="192.168.0.0/16"  
  
ARG DEBIAN_FRONTEND="noninteractive"  
  
WORKDIR /etc/openvpn  
  
RUN echo 'deb http://ppa.launchpad.net/jcfp/nobetas/ubuntu xenial main' >
/etc/apt/sources.list.d/sabnzbd.list \  
&& echo 'deb-src http://ppa.launchpad.net/jcfp/nobetas/ubuntu xenial main' >>
/etc/apt/sources.list.d/sabnzbd.list \  
&& echo 'deb http://ppa.launchpad.net/jcfp/sab-addons/ubuntu xenial main' >
/etc/apt/sources.list.d/sabnzbd-addons.list \  
&& echo 'deb-src http://ppa.launchpad.net/jcfp/sab-addons/ubuntu xenial main'
>> /etc/apt/sources.list.d/sabnzbd-addons.list \  
&& apt-key adv \--keyserver keyserver.ubuntu.com \--recv-keys 4BB9F05F \  
&& apt-get update \  
&& apt-get install \--yes \--no-install-recommends \  
curl \  
openssh-client \  
openvpn \  
p7zip-full \  
par2-tbb \  
python-cryptography \  
python-sabyenc \  
sabnzbdplus \  
unrar \  
unzip \  
wget \  
&& wget \--quiet \--directory-prefix /tmp
"http://ftp.debian.org/debian/pool/main/n/netselect/netselect_0.3.ds1-28+b1_amd64.deb"
\  
&& dpkg \--install /tmp/netselect_*_amd64.deb \  
&& apt-get autoremove \--yes \--purge \  
&& apt-get clean \  
&& rm \--recursive \--force /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD https://www.privateinternetaccess.com/openvpn/openvpn.zip /etc/openvpn/  
#ADD https://www.privateinternetaccess.com/openvpn/openvpn-strong.zip
/etc/openvpn/  
  
COPY openvpn/ /etc/openvpn/  
COPY sabnzbd/ /etc/sabnzbd/  
  
VOLUME /config /data  
  
EXPOSE 8080  
  
CMD ["/etc/openvpn/start.sh"]  
  
HEALTHCHECK \--interval=60s \--timeout=5s CMD curl \--silent \--location
\--fail http://localhost:8080/ > /dev/null || exit 1  

