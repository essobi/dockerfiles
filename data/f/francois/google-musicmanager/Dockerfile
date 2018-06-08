FROM debian:stretch  
MAINTAINER François Billant <fbillant@gmail.com>  
  
RUN sed -i.bak 's/stretch main/stretch main contrib non-free/g'
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y \  
fontconfig fontconfig-config fonts-dejavu-core iso-codes libaudio2 libbsd0
libcap2 libcap2-bin libdbus-1-3 libdrm2 libexpat1 libflac8 libfontconfig1
libfreetype6 libgl1-mesa-glx libglapi-mesa libglib2.0-0 libgstreamer-plugins-
base1.0-0 libgstreamer1.0-0 libice6 libjbig0 libjpeg62-turbo liblcms2-2
libmng1 libogg0 liborc-0.4-0 libpng16-16 libqt4-network libqt4-opengl
libqt4-xml libqt4-xmlpatterns libqtcore4 libqtdbus4 libqtgui4 libqtwebkit4
libsm6 libsqlite3-0 libtiff5 libvorbis0a libvorbisfile3 libx11-6 libx11-data
libx11-xcb1 libxau6 libxcb-dri2-0 libxcb-dri3-0 libxcb-glx0 libxcb-present0
libxcb-sync1 libxcb1 libxdamage1 libxdmcp6 libxext6 libxfixes3 libxrender1
libxshmfence1 libxt6 libxxf86vm1 qtcore4-l10n ucf x11-common xdg-utils
libcurl3 wget procps \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /opt && \  
wget --no-check-certificate https://dl.google.com/linux/direct/google-
musicmanager-beta_current_amd64.deb && \  
dpkg -i google-musicmanager-beta_current_amd64.deb  
  
COPY run.sh /  
  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  

