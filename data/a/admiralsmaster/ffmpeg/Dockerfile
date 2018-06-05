FROM nuagebec/ubuntu:16.04  
LABEL maintainer "Ariel Kuechler <github.ariel@kuechler.info>"  
  
VOLUME /data/persistent  
  
ENV HOME_DIR /root  
  
  
RUN apt-get update -y \  
&& apt-get -y upgrade \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \  
man-db autoconf automake build-essential libass-dev libfreetype6-dev \  
libsdl2-dev libtheora-dev libtool libva-dev libvdpau-dev libvorbis-dev
libxcb1-dev libxcb-shm0-dev \  
libxcb-xfixes0-dev pkg-config texinfo zlib1g-dev cmake mercurial tmux \  
frei0r-plugins frei0r-plugins-dev ladspa-sdk libiec61883-0 libiec61883-dev
libavc1394-0 libavc1394-dev \  
libbs2b0 libbs2b-dev libcaca0 libcaca-dev libflite1 flite1-dev libgme0 libgme-
dev libgsm1 libgsm1-dev \  
libmodplug1 libmodplug-dev libopencv-dev libopenjpeg5 libopenjpeg-dev librtmp1
librtmp-dev \  
libschroedinger-1.0-0 libschroedinger-dev libshine3 libshine-dev libsnappy-dev
libsnappy1v5 libsoxr-dev \  
libsoxr0 libssh-4 libssh-dev libspeex1 libspeex-dev libtwolame0 libtwolame-dev
libwavpack1 libwavpack-dev \  
libwebp-dev libwebp5 libxvidcore-dev libxvidcore4 libzmq3-dev libzmq5 libzvbi0
libzvbi-dev libopenal1 \  
libopenal-dev libcdio-paranoia1 libcdio-paranoia-dev libgnutls30
libgnutls28-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY compile.sh ${HOME_DIR}/  
  
RUN chmod u+x ${HOME_DIR}/compile.sh  
  
RUN ${HOME_DIR}/compile.sh  

