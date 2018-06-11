FROM linuxserver/sabnzbd  
COPY ./newswrappersig.txt /  
# verify sha  
ENV /usr/bin/sha256sum -c /newswrappersig.txt  
# install reqs  
# install packages  
RUN \  
echo "deb http://ppa.launchpad.net/jcfp/ppa/ubuntu xenial main" >>
/etc/apt/sources.list.d/sabnzbd.list && \  
echo "deb-src http://ppa.launchpad.net/jcfp/ppa/ubuntu xenial main" >>
/etc/apt/sources.list.d/sabnzbd.list && \  
echo "deb http://ppa.launchpad.net/jcfp/sab-addons/ubuntu xenial main" >>
/etc/apt/sources.list.d/sabnzbd.list && \  
echo "deb-src http://ppa.launchpad.net/jcfp/sab-addons/ubuntu xenial main" >>
/etc/apt/sources.list.d/sabnzbd.list && \  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:11371 \--recv-keys
0x98703123E0F52B2BE16D586EF13930B14BB9F05F && \  
apt-get update && \  
apt-get install -y \  
python-socks && \  
# cleanup  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# copy our hack in  
ADD
https://raw.githubusercontent.com/bbosmat/sabnzbd/feature/socks_proxy/sabnzbd/newswrapper.py
/usr/share/sabnzbdplus/sabnzbd/newswrapper.py  

