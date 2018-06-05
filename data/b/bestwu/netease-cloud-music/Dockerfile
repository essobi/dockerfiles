FROM bestwu/deepin:panda  
LABEL name=netease-cloud-music \  
version=1.1.0 \  
release=1 \  
maintainer='Peter Wu <piterwu@outlook.com>'  
  
RUN echo 'deb http://mirrors.kernel.org/deepin panda main' >
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends locales && \  
echo 'zh_CN.UTF-8 UTF-8' > /etc/locale.gen && \  
locale-gen && \  
echo -e 'LANG="zh_CN.UTF-8"\nLANGUAGE="zh_CN:zh"\n' > /etc/default/locale && \  
source /etc/default/locale && \  
apt-get install -y --no-install-recommends fonts-wqy-microhei dbus-x11
netease-cloud-music && \  
apt-get -y autoremove && apt-get clean -y && apt-get autoclean -y && \  
rm -rf var/lib/apt/lists/* var/cache/apt/* var/log/*  
  
ENV LANGUAGE=zh_CN.UTF-8 \  
LC_ALL=zh_CN.UTF-8 \  
LANG=zh_CN.UTF-8 \  
TZ=UTC-8 \  
APP=netease-cloud-music \  
AUDIO_GID=63 \  
GID=1000 \  
UID=1000  
  
RUN groupadd -o -g $GID netease && \  
groupmod -o -g $AUDIO_GID audio && \  
useradd -d "/home/netease" -m -o -u $UID -g netease -G audio netease  
  
ADD entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

