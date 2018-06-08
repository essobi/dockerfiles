# THIS IS A WORK IN PROGRESS!  
# How I'm running the container after building it:  
#docker run -d --name sagetv-server \  
# -v /mnt/user/Media/Pictures:/media/pictures -v /mnt/user/Media/:/media/music
\  
# -v /mnt/user/Media/Movies:/media/videos/movies -v /mnt/user/Media/TV\
Shows:/media/videos/tv_shows \  
# -v /mnt/user/temp/Recordings:/recordings \  
# -v /mnt/vms/docker-config/sagetv:/config \  
# -p 42024:42024 -p 7818:7818 -p 8270:8270/udp -p 31100:31100/udp -p
31099:31099 \  
# -p 16867:16867/udp -p 16869:16869/udp -p 16881:16881/udp \  
# -t coppit/sagetv-server  
FROM phusion/baseimage:0.9.17  
MAINTAINER David Coppit <david@coppit.org>  
  
ENV APP_NAME="SageTV Media Center Server"  
ENV DEBIAN_FRONTEND noninteractive  
  
# Speed up APT  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup \  
&& echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
# Auto-accept Oracle JDK license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# Install Oracle Java 8  
RUN add-apt-repository ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get install -y oracle-java8-installer  
  
# Create dir to keep things tidy  
RUN mkdir /files  
  
RUN set -x \  
# && apt-get update \  
&& apt-get install -y unzip \  
build-essential \  
libx11-dev libxt-dev libraw1394-dev libavc1394-dev libiec61883-dev
libfreetype6-dev yasm autoconf libtool  
  
# Now let's fetch down a specific version of SageTV (for reproducible builds)
and build it  
RUN wget -O /files/sagetv.zip
https://github.com/google/sagetv/archive/d9ed4ecbcf9cb8e8553f4fde56d345f552d8491a.zip  
  
RUN unzip -d /files /files/sagetv.zip  
  
WORKDIR /files/sagetv-d9ed4ecbcf9cb8e8553f4fde56d345f552d8491a/build  
  
# HACKS for 64-bit and newer Java  
RUN set -x \  
&& sed -i 's/i386/amd64/' ubuntufiles/server/DEBIAN/control \  
&& sed -i 's/sun-java6-jre/oracle-java8-installer/'
ubuntufiles/server/DEBIAN/control  
  
RUN export JDK_HOME=/usr/lib/jvm/java-8-oracle \  
&& ./buildall.sh  
  
# It seems like everything is statically linked. At least, startsage didn't
complain about missing shared libs when I  
# removed all this stuff.  
RUN set -x \  
&& apt-get purge -y unzip \  
build-essential \  
libx11-dev libxt-dev libraw1394-dev libavc1394-dev libiec61883-dev
libfreetype6-dev yasm autoconf libtool \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# HACK: i386 is a lie here. It's amd64.  
RUN dpkg -i sagetv-server_9.0.0_i386.deb  
  
RUN rm -rf /files  
  
WORKDIR /  
  
VOLUME ["/recordings", "/media", "/config"]  
  
# Client (TCP 42024 for connecting, TCP 7818 for streaming, UDP 8270 for
finding servers)  
EXPOSE 42024 7818 8270  
# All extenders (UDP 31100 for discovery, TCP 31099 for connections?)  
EXPOSE 31100 31099  
# Hauppage extender (all UDP)  
EXPOSE 16867 16869 16881  
CMD /opt/sagetv/server/startsage && sleep infinity  

