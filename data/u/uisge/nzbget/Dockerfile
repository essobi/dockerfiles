FROM phusion/baseimage:0.9.19  
MAINTAINER https://github.com/uisge-beatha  
ENV DEBIAN_FRONTEND noninteractive  
  
######################################  
## Environment  
######################################  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
######################################  
# Set correct environment variables  
######################################  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
######################################  
## Configure Directories  
######################################  
## SickRage configuration folder  
VOLUME /NZBGet-config  
  
## SickRage watched folder  
VOLUME /watched  
  
## Downloads  
VOLUME /downloads  
  
## SSL keys & certs  
VOLUME /certs  
  
## media  
VOLUME /media  
  
RUN mkdir -p /files /home/ashtaroth/monkey  
  
######################################  
## Upgrade OS  
######################################  
RUN apt-get update -q && apt-get upgrade -y -o Dpkg::Options::="--force-
confold"  
######################################  
## Misc setup  
######################################  
  
RUN add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu/ xenial
multiverse"  
RUN add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu/ xenial-
updates multiverse"  
RUN apt-get update -qq  
  
#Install general utilities  
RUN apt-get install -qy wget unrar unzip p7zip python2.7 dos2unix avahi-daemon
avahi-utils  
  
######################################  
## FFmpeg setup  
######################################  
#See https://junise.wordpress.com/2015/05/12/ffmpeg-installation-in-
ubuntu-14-04/  
#For original details for this FFmpeg setup  
#Install FFmpeg prerequisites  
RUN apt-get install -qy build-essential checkinstall git libfaac-dev libgpac-
dev \  
libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev librtmp-dev
libtheora-dev \  
libvorbis-dev pkg-config texi2html yasm zlib1g-dev  
  
# Install x264  
RUN apt-get -qy install libx264-dev  
RUN cd / | git clone --depth 1 git://git.videolan.org/x264 /x264 ; \  
cd /x264/ ; ./configure --enable-static ; make ; make install  
  
#\  
#checkinstall --pkgname=x264 --pkgversion="3:$(./version.sh \  
#awk -F'[" ]' '/POINT/{print $4"+git"$5}')" --backup=no --deldoc=yes \  
#--fstrans=no --default  
# Install AAC audio decoder 0.1.4  
RUN cd / ; wget --output-document="fdk-aac-0.1.4.tar.gz"
"http://downloads.sourceforge.net/project/opencore-amr/fdk-aac/fdk-
aac-0.1.4.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fopencore-
amr%2F&ts=1476407126&use_mirror=pilotfiber"; \  
tar xzvf fdk-aac-0.1.4.tar.gz ; cd fdk-aac-0.1.4 ; ./configure ; make ; \  
make install  
  
#checkinstall --pkgname=fdk-aac --pkgversion="0.1.0" --backup=no \  
#--deldoc=yes --fstrans=no --default  
# Install VP8 video encoder and decoder.  
RUN cd / ; git clone --depth 1 https://chromium.googlesource.com/webm/libvpx ;
\  
cd libvpx ; \  
./configure ; \  
make ; make install  
  
#checkinstall --pkgname=libvpx --pkgversion="1:$(date +%Y%m%d%H%M)-git"
--backup=no \  
#--deldoc=yes --fstrans=no --default  
# Add lavf support to x264  
# This allows x264 to accept just about any input that FFmpeg can handle and
is useful if  
# you want to use x264 directly. See a more detailed explanation of what this
means.  
RUN cd /x264 ; make distclean ; ./configure --enable-static ; make ; make
install  
  
  
#checkinstall --pkgname=x264 --pkgversion="3:$(./version.sh | \  
#awk -F'[" ]' '/POINT/{print $4"+git"$5}')" --backup=no --deldoc=yes \  
#--fstrans=no --default  
#Install FFmpeg  
RUN cd / ; git clone git://source.ffmpeg.org/ffmpeg ; cd /ffmpeg ; \  
./configure --enable-gpl --enable-libfdk-aac --enable-libmp3lame --enable-
libopencore-amrnb \  
\--enable-libopencore-amrwb --enable-librtmp --enable-libtheora --enable-
libvorbis \  
\--enable-libvpx --enable-libx264 --enable-nonfree --enable-version3 ; \  
make ; make install  
  
#checkinstall --pkgname=ffmpeg --pkgversion="5:$(date +%Y%m%d%H%M)-git"
--backup=no \  
#--deldoc=yes --fstrans=no --default #; \  
##hash x264 ffmpeg ffprobe #ffplay  
# Optional: install qt-faststart  
# This is a useful tool if you're showing your H.264 in MP4 videos on the web.  
# It relocates some data in the video to allow playback to begin before the
file is  
# completely downloaded. Usage: qt-faststart input.mp4 output.mp4.  
RUN cd /ffmpeg ; make tools/qt-faststart ; make install tools/qt-faststart  
  
#\  
#checkinstall --pkgname=qt-faststart --pkgversion="$(date +%Y%m%d%H%M)-git"
--backup=no \  
#--deldoc=yes --fstrans=no --default install -Dm755 tools/qt-faststart \  
#/usr/local/bin/qt-faststart  
######################################  
## NZBGet setup  
######################################  
#Download NZBGet setup script  
#See https://github.com/nzbget/nzbget/wiki/Installation-on-Linux  
RUN (wget -O - http://nzbget.net/info/nzbget-version-linux.json | \  
sed -n "s/^.*stable-download.*: \"\\(.*\\)\".*/\1/p" | \  
wget --no-check-certificate -i - -O /nzbget-latest-bin-linux.run ) || echo
"*** Download failed ***"  
  
RUN sh /nzbget-latest-bin-linux.run --destdir /opt/NZBGet  
  
  
#Clean up directories after installs  
RUN rm -rf /libvpx /fdk-aac-0.1.4* /x264 /nzbget-latest-bin-linux.run  
  
######################################  
## Python setup  
######################################  
RUN ln -s /usr/bin/python2.7 /usr/bin/python2  
RUN ln -s /usr/bin/python2.7 /usr/bin/python  
  
######################################  
## Expose Ports  
######################################  
## SickRage  
EXPOSE 6789  
######################################  
## Add Services to runit  
######################################  
## Add NZBGet  
RUN mkdir /etc/service/NZBGet  
ADD NZBGet.sh /etc/service/NZBGet/run  
RUN chmod +x /etc/service/NZBGet/run  
  
  
#Make DBUS requires this directory  
RUN mkdir -p /var/run/dbus  
VOLUME /var/run/dbus  
#Configure Avahi  
ADD avahi-daemon.conf /etc/avahi/avahi-daemon.conf  
  
######################################  
## Add boot scripts  
######################################  
# Add firstrun.sh to execute during container startup  
ADD startup.sh /etc/my_init.d/firstrun.sh  
RUN chmod +x /etc/my_init.d/firstrun.sh  
  
# Add initd.sh to execute during container startup  
ADD initd.sh /etc/my_init.d/initd.sh  
RUN chmod +x /etc/my_init.d/initd.sh  
  
#ADD Readme.md /Readme.md  
######################################  
## Clean up APT when done.  
######################################  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

