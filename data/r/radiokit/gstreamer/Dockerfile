FROM ubuntu:xenial  
  
ARG GST_VERSION=1.12.3  
  
RUN apt-get -y update  
  
# Install compiler etc.  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
autoconf \  
automake \  
autopoint \  
bison \  
flex \  
libtool \  
yasm \  
nasm \  
git-core \  
build-essential \  
gettext  
  
# Install dependencies necessary to build our custom GStreamer build  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libglib2.0-dev \  
libpthread-stubs0-dev \  
libssl-dev \  
liborc-dev \  
libmpg123-dev \  
libmp3lame-dev \  
libsoup2.4-dev \  
libshout3-dev \  
libpulse-dev  
  
  
# Fetch and build GStreamer  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gstreamer && \  
cd gstreamer && \  
git checkout $GST_VERSION && \  
./autogen.sh --prefix=/usr --disable-gtk-doc && \  
make -j`nproc` && \  
make install && \  
cd .. && \  
rm -rvf /gstreamer  
  
# Fetch and build gst-plugins-base  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gst-plugins-base && \  
cd gst-plugins-base && \  
git checkout $GST_VERSION && \  
./autogen.sh --prefix=/usr \  
--disable-gtk-doc \  
--disable-adder \  
--disable-app \  
--disable-videoconvert \  
--disable-gio \  
--disable-subparse \  
--disable-tcp \  
--disable-videotestsrc \  
--disable-videorate \  
--disable-videoscale \  
--disable-x \  
--disable-xvideo \  
--disable-xshm \  
--disable-alsa \  
--disable-cdparanoia \  
--disable-ivorbis \  
--disable-libvisual \  
--disable-pango \  
--disable-theora && \  
make -j`nproc` && \  
make install && \  
cd .. && \  
rm -rvf /gst-plugins-base  
  
# Fetch and build gst-plugins-good  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gst-plugins-good && \  
cd gst-plugins-good && \  
git checkout $GST_VERSION && \  
./autogen.sh --prefix=/usr \  
--disable-gtk-doc \  
--disable-alpha \  
--disable-avi \  
--disable-deinterlace \  
--disable-dtmf \  
--disable-effectv \  
--disable-flv \  
--disable-flx \  
--disable-goom \  
--disable-goom2k1 \  
--disable-imagefreeze \  
--disable-interleave \  
--disable-isomp4 \  
--disable-matroska \  
--disable-monoscope \  
--disable-rtp \  
--disable-rtpmanager \  
--disable-rtsp \  
--disable-shapewipe \  
--disable-smpte \  
--disable-udp \  
--disable-videobox \  
--disable-videocrop \  
--disable-videofilter \  
--disable-videomixer \  
--disable-y4m \  
--disable-directsound \  
--disable-waveform \  
--disable-oss \  
--disable-oss4 \  
--disable-sunaudio \  
--disable-osx_audio \  
--disable-osx_video \  
--disable-gst_v4l2 \  
--disable-x \  
--disable-aalib \  
--disable-aalibtest \  
--disable-cairo \  
--disable-flac \  
--disable-gdk_pixbuf \  
--disable-jack \  
--disable-jpeg \  
--disable-libcaca \  
--disable-libdv \  
--disable-libpng \  
--disable-dv1394 \  
--disable-vpx && \  
make -j`nproc` && \  
make install && \  
cd .. && \  
rm -rvf /gst-plugins-good  
  
# Fetch and build gst-plugins-bad  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gst-plugins-bad && \  
cd gst-plugins-bad && \  
git checkout $GST_VERSION && \  
./autogen.sh --prefix=/usr \  
--disable-gtk-doc \  
--disable-accurip \  
--disable-adpcmdec \  
--disable-adpcmenc \  
--disable-aiff \  
--disable-videoframe_audiolevel \  
--disable-asfmux \  
--disable-compositor \  
--disable-bayer \  
--disable-camerabin2 \  
--disable-coloreffects \  
--disable-dvbsuboverlay \  
--disable-dvdspu \  
--disable-faceoverlay \  
--disable-festival \  
--disable-fieldanalysis \  
--disable-freeverb \  
--disable-frei0r \  
--disable-gaudieffects \  
--disable-geometrictransform \  
--disable-gdp \  
--disable-inter \  
--disable-interlace \  
--disable-ivfparse \  
--disable-ivtc \  
--disable-jp2kdecimator \  
--disable-jpegformat \  
--disable-librfb \  
--disable-midi \  
--disable-mpegdemux \  
--disable-mpegtsdemux \  
--disable-mpegtsmux \  
--disable-mpegpsmux \  
--disable-mxf \  
--disable-netsim \  
--disable-onvif \  
--disable-pcapparse \  
--disable-pnm \  
--disable-rawparse \  
--disable-sdp \  
--disable-siren \  
--disable-smooth \  
--disable-speed \  
--disable-subenc \  
--disable-timecode \  
--disable-videofilters \  
--disable-videoparsers \  
--disable-videosignal \  
--disable-vmnc \  
--disable-y4m \  
--disable-yadif \  
--disable-directsound \  
--disable-wasapi \  
--disable-direct3d \  
--disable-winscreencap \  
--disable-winks \  
--disable-android_media \  
--disable-apple_media \  
--disable-bluez \  
--disable-avc \  
--disable-shm \  
--disable-vcd \  
--disable-opensles \  
--disable-uvch264 \  
--disable-nvenc \  
--disable-tinyalsa \  
--disable-msdk \  
--disable-assrender \  
--disable-voamrwbenc \  
--disable-voaacenc \  
--disable-bs2b \  
--disable-bz2 \  
--disable-chromaprint \  
--disable-curl \  
--disable-dash \  
--disable-dc1394 \  
--disable-decklink \  
--disable-directfb \  
--disable-wayland \  
--disable-webp \  
--disable-daala \  
--disable-dts \  
--disable-resindvd \  
--disable-faac \  
--disable-faad \  
--disable-fbdev \  
--disable-fdk_aac \  
--disable-flite \  
--disable-gsm \  
--disable-fluidsynth \  
--disable-kate \  
--disable-kms \  
--disable-ladspa \  
--disable-lv2 \  
--disable-libde265 \  
--disable-libmms \  
--disable-srtp \  
--disable-dtls \  
--disable-ttml \  
--disable-modplug \  
--disable-mpeg2enc \  
--disable-mplex \  
--disable-musepack \  
--disable-neon \  
--disable-ofa \  
--disable-openal \  
--disable-opencv \  
--disable-openexr \  
--disable-openh264 \  
--disable-openjpeg \  
--disable-openmpt \  
--disable-openni2 \  
--disable-rsvg \  
--disable-gl \  
--disable-gtk3 \  
--disable-qt \  
--disable-vulkan \  
--disable-teletextdec \  
--disable-wildmidi \  
--disable-smoothstreaming \  
--disable-sndfile \  
--disable-soundtouch \  
--disable-spc \  
--disable-gme \  
--disable-dvb \  
--disable-acm \  
--disable-vdpau \  
--disable-sbc \  
--disable-schro \  
--disable-zbar \  
--disable-rtmp \  
--disable-spandsp \  
--disable-hls \  
--disable-x265 \  
--disable-webrtcdsp && \  
make -j`nproc` && \  
make install && \  
cd .. && \  
rm -rvf /gst-plugins-bad  
  
# Fetch and build gst-plugins-ugly  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gst-plugins-ugly && \  
cd gst-plugins-ugly && \  
git checkout $GST_VERSION && \  
./autogen.sh --prefix=/usr \  
--disable-gtk-doc \  
--disable-asfdemux \  
--disable-dvdlpcmdec \  
--disable-dvdsub \  
--disable-xingmux \  
--disable-realmedia \  
--disable-a52dec \  
--disable-amrnb \  
--disable-amrwb \  
--disable-cdio \  
--disable-dvdread \  
--disable-sidplay \  
--disable-x264 && \  
make -j`nproc` && \  
make install && \  
cd .. && \  
rm -rvf /gst-plugins-ugly  
  
# Do some cleanup  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean && \  
apt-get autoremove -y  

