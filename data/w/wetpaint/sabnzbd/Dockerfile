FROM lsiobase/ubuntu:xenial  
MAINTAINER sparklyballs  
MAINTAINER wetpaint  
  
# environment settings  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV HOME="/config" \  
PYTHONIOENCODING=utf-8  
# install packages  
RUN \  
echo "deb http://ppa.launchpad.net/jcfp/nobetas/ubuntu xenial main" >>
/etc/apt/sources.list.d/sabnzbd.list && \  
echo "deb-src http://ppa.launchpad.net/jcfp/nobetas/ubuntu xenial main" >>
/etc/apt/sources.list.d/sabnzbd.list && \  
echo "deb http://ppa.launchpad.net/jcfp/sab-addons/ubuntu xenial main" >>
/etc/apt/sources.list.d/sabnzbd.list && \  
echo "deb-src http://ppa.launchpad.net/jcfp/sab-addons/ubuntu xenial main" >>
/etc/apt/sources.list.d/sabnzbd.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:11371 --recv-keys
0x98703123E0F52B2BE16D586EF13930B14BB9F05F && \  
apt-get update && \  
apt-get install -y \  
p7zip-full \  
par2-tbb \  
python-sabyenc \  
sabnzbdplus \  
ffmpeg \  
git \  
unrar \  
unzip && \  
  
# cleanup  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
RUN locale-gen en_US.UTF-8  
  
# add local files  
COPY root/ /  
  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
RUN dpkg-reconfigure --frontend noninteractive locales  
  
# ports and volumes  
EXPOSE 8080 9090  
VOLUME /config /downloads /incomplete-downloads /scripts  

