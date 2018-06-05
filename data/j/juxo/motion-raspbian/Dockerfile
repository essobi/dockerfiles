FROM debian:stretch  
  
RUN apt-get update && apt-get upgrade -y --force-yes --no-install-recommends  
RUN apt-get install --force-yes -y autoconf automake build-essential pkgconf
libtool libzip-dev libjpeg62-turbo libjpeg62-turbo-dev git libavformat-dev
libavcodec-dev libavutil-dev libswscale-dev libavdevice-dev libavformat-dev
libavcodec-dev libavutil-dev libswscale-dev libavdevice-dev ssmtp mailutils  
RUN git clone https://github.com/Motion-Project/motion.git  
RUN cd motion && autoreconf -fiv && ./configure && make && make install  
CMD ["motion"]

