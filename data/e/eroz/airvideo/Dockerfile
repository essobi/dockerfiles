# ref: http://www.inmethod.com/forum/posts/list/1856.page  
FROM phusion/baseimage:0.9.11  
MAINTAINER rsanch1 <rsanch1@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables.  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# set sane localeRUN locale-gen en_US en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Correct user and group uid/guid  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /config nobody  
  
ADD sources.list /etc/apt/  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# dependicies of airvideo  
RUN apt-get -y --no-install-recommends install libmp3lame0 libx264-dev
libfaac0 faac openjdk-6-jre avahi-daemon ttf-wqy-microhei fonts-dejavu curl  
  
# airvideo server's files  
ADD AirVideoServerLinux.properties /opt/airvideo-server/  
ADD airvideo-server.service /etc/avahi/services/  
RUN curl -s
http://s3.amazonaws.com/AirVideo/Linux-2.4.6-beta3/AirVideoServerLinux.jar -o
/opt/airvideo-server/AirVideoServerLinux.jar  
RUN mkdir -p /opt/airvideo-server/bin  
  
# compile avconv  
RUN apt-get install -y build-essential libmp3lame-dev libfaac-dev yasm pkg-
config && \  
cd /tmp && \  
curl -s http://s3.amazonaws.com/AirVideo/Linux-2.4.6-beta3/libav.tar.bz2 -o
libav.tar.bz2 && \  
tar xf libav.tar.bz2 && \  
cd libav && \  
./configure --enable-pthreads --disable-shared --enable-static --enable-gpl
--enable-libx264 --enable-libmp3lame --enable-nonfree --enable-libfaac && \  
make -j4 && \  
strip -s -o /opt/airvideo-server/bin/avconv /tmp/libav/avconv && \  
apt-get purge -y build-essential libmp3lame-dev libfaac-dev yasm pkg-config &&
\  
apt-get autoremove -y && \  
apt-get autoclean && \  
rm -rf /tmp/libav.tar.bz2 /tmp/libav  
  
# run as nobody instead of root & fix permissions  
RUN chown -R nobody:users /opt/airvideo-server  
  
# Fix avahi-daemon not working without dbus  
RUN sed -i -e "s#\\#enable-dbus=yes#enable-dbus=false#g" /etc/avahi/avahi-
daemon.conf  
  
VOLUME ['/config']  
  
# Add config.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD config.sh /etc/my_init.d/config.sh  
RUN chmod +x /etc/my_init.d/config.sh  
  
# Add AirVideServer to runit  
RUN mkdir /etc/service/airvideo_server  
ADD airvideo_server.sh /etc/service/airvideo_server/run  
RUN chmod +x /etc/service/airvideo_server/run  
  
# Add avahi-daemon to runit  
RUN mkdir /etc/service/avahi-daemon  
ADD avahi-daemon.sh /etc/service/avahi-daemon/run  
RUN chmod +x /etc/service/avahi-daemon/run  
  

