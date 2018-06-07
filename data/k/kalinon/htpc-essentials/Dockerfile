FROM ubuntu:trusty  
MAINTAINER Holden Omans <holden.omans@gmail.com>  
  
# Set up required libs and ubuntu ENVs  
ENV DEBIAN_FRONTEND="noninteractive" \  
LANG="en_US.UTF-8" \  
LC_ALL="C.UTF-8" \  
LANGUAGE="en_US.UTF-8"  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >>
/etc/apt/sources.list && \  
apt-get -q update && \  
apt-get -qy --force-yes dist-upgrade && \  
apt-get install -qy \  
# Base apps  
git curl supervisor ca-certificates \  
# Python libs  
python-software-properties software-properties-common python-pip python-dev
build-essential python-imaging \  
# Headphones ffmpeg req  
procps bzip2 libgnutlsxx27 libogg0 libjpeg8 libpng12-0 \  
libvpx1 libtheora0 libxvidcore4 libmpeg2-4 \  
libvorbis0a libfaad2 libmp3lame0 libmpg123-0 libmad0 libopus0 libvo-aacenc0 \  
# pillow required libs  
libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev
tcl8.6-dev tk8.6-dev python-tk  
  
# Install unrar  
RUN curl http://www.rarlab.com/rar/unrarsrc-5.2.6.tar.gz -G -o
/root/unrarsrc-5.2.6.tar.gz && \  
tar xzf /root/unrarsrc-5.2.6.tar.gz -C /root/  
  
WORKDIR /root/unrar  
RUN make lib && make install-lib  
WORKDIR /  
RUN rm -r /root/unrar*  
ENV UNRAR_LIB_PATH /usr/lib/libunrar.so  
  
# Install PIP libs  
RUN pip install -U pip setuptools certifi && \  
pip install pillow configparser beautifulsoup4 unrar natsort PyPDF2  
  
# install Sabnzbd++  
RUN add-apt-repository -y ppa:jcfp/ppa && apt-get -q update && \  
apt-get install -qy sabnzbdplus sabnzbdplus-theme-classic sabnzbdplus-theme-
mobile \  
sabnzbdplus-theme-plush par2 python-yenc unzip unrar  
  
# Clone needed repos  
RUN git clone https://github.com/midgetspy/Sick-Beard.git /opt/sickbeard && \  
git clone https://github.com/RuudBurger/CouchPotatoServer.git /opt/couchpotato
&& \  
git clone https://github.com/gugahoi/maraschino.git /opt/maraschino && \  
git clone https://github.com/rembo10/headphones.git /opt/headphones && \  
git clone https://github.com/Kalinon/mylar.git /opt/mylar  
  
# Cleanup  
RUN add-apt-repository -y ppa:mc3man/trusty-media && apt-get -q update && \  
apt-get install -qy ffmpeg && \  
apt-get purge -y --auto-remove curl gcc make yasm bzip2 \  
libc6-dev libgnutls-dev libogg-dev librtmp-dev libjpeg-dev libpng12-dev \  
libvpx-dev libtheora-dev libxvidcore-dev libmpeg2-4-dev libssl-dev \  
libvorbis-dev libfaad-dev libmp3lame-dev libmpg123-dev libmad0-dev \  
libopus-dev libvo-aacenc-dev build-essential python-dev && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
# Set up needed scripts  
COPY ["supervisord.conf", "/etc/supervisor/conf.d/supervisord.conf"]  
RUN mkdir -p /var/log/supervisor  
  
# Declare volumes needed  
VOLUME ["/config","/data","/opt/mylar/cache"]  
  
# Final setup  
EXPOSE 5050 8080 8081 8085 8181 8090 7000  
ENTRYPOINT ["/usr/bin/supervisord"]

