FROM ubuntu:14.04  
MAINTAINER Cristian Gauxachs (cristiangauma) <cristian.gauxachs@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#  
# Installing dependences  
#  
RUN apt-get update \  
&& apt-get install -y git v4l-utils python-pip python-dev libssl-dev
libcurl4-openssl-dev libjpeg-dev autoconf automake build-essential libtool
libzip-dev software-properties-common \  
libavutil-dev libavformat-dev libavcodec-dev libswscale-dev  
  
#  
# Installing ffmpeg  
#  
RUN add-apt-repository -y ppa:kirillshkrogalev/ffmpeg-next \  
&& apt-get update \  
&& apt-get install -y ffmpeg  
  
#  
# Compiling motion daemon  
#  
RUN cd /tmp && git clone https://github.com/Mr-Dave/motion.git \  
&& cd motion \  
&& autoreconf -fiv \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig \  
&& mkdir /etc/motion/ \  
&& cp /usr/local/etc/motion/motion-dist.conf /etc/motion/motion.conf \  
&& cd /tmp \  
&& rm -rf motion  
  
#  
# Installing and configuring MotionEye  
#  
RUN pip install motioneye \  
&& mkdir -p /etc/motioneye \  
&& cp /usr/local/share/motioneye/extra/motioneye.conf.sample
/etc/motioneye/motioneye.conf \  
&& mkdir -p /var/lib/motioneye  
  
VOLUME ["/var/lib/motioneye"]  
VOLUME ["/etc/motioneye"]  
  
WORKDIR /usr/local/bin  
  
EXPOSE 8765  
CMD ["./meyectl","startserver", "-c /etc/motioneye/motioneye.conf"]  

