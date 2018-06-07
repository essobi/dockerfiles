FROM resin/raspberrypi3-python:2.7-slim AS build  
MAINTAINER orbsmiv@hotmail.com  
  
RUN [ "cross-build-start" ]  
  
# Set environment variables  
ARG DEBIAN_FRONTEND=noninteractive  
  
ARG VERSION_TAG="v1.9.12"  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
alsa-base \  
libicu-dev \  
libasound2-dev \  
libsamplerate0-dev \  
libsndfile1-dev \  
libreadline-dev \  
libxt-dev \  
libudev-dev \  
libavahi-client-dev \  
git \  
gcc-4.8 \  
g++-4.8  
  
RUN mkdir /tmp/jackd-compile \  
&& git clone \--recursive --depth 1 --branch ${VERSION_TAG} \  
git://github.com/jackaudio/jack2 /tmp/jackd-compile  
  
ARG CC=/usr/bin/gcc-4.8  
ARG CXX=/usr/bin/g++-4.8  
WORKDIR /tmp/jackd-compile  
  
RUN ./waf configure --alsa --libdir=/usr/lib/arm-linux-gnueabihf/  
RUN ./waf build  
RUN ./waf install  
RUN ldconfig  
  
RUN [ "cross-build-end" ]  
  
FROM resin/armv7hf-debian:stretch  
# FROM arm32v7/debian:stretch-slim  
RUN [ "cross-build-start" ]  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
WORKDIR /  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libasound2 \  
libsamplerate0 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY \--from=build /usr/local/bin/jack* /usr/local/bin/  
COPY \--from=build /usr/local/bin/alsa* /usr/local/bin/  
COPY \--from=build /usr/local/share/man/man1/jack* /usr/local/share/man/man1/  
COPY \--from=build /usr/local/share/man/man1/alsa* /usr/local/share/man/man1/  
COPY \--from=build /usr/lib/arm-linux-gnueabihf/libjack* /usr/lib/arm-linux-
gnueabihf/  
COPY \--from=build /usr/lib/arm-linux-gnueabihf/jack/* /usr/lib/arm-linux-
gnueabihf/jack/  
COPY \--from=build /usr/local/include/jack/* /usr/local/include/jack/  
COPY \--from=build /usr/lib/arm-linux-gnueabihf/pkgconfig/jack.pc
/usr/lib/arm-linux-gnueabihf/pkgconfig/jack.pc  
  
RUN echo "@audio - memlock 256000" >> /etc/security/limits.conf \  
&& echo "@audio - rtprio 75" >> /etc/security/limits.conf  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
# CMD ["-r", "-v", "-d", "alsa", "-d", "hw:0", "-p", "1024", "-n", "3", "-s",
"-r", "48000", "-P"]  
CMD ["/usr/local/bin/jackd", "-m", "-r", "-p", "32", "-T", "-v", "-d", "alsa",
"-d", "hw:0", "-n", "3", "-p", "2048", "-P", "-r", "48000", "-s"]  
  
# CMD ["/usr/local/bin/jackd", "-r", "-v", "-d", "alsa", "-d", "hw:0", "-p",
"1024", "-n", "3", "-s", "-r", "48000", "-P"]  
RUN [ "cross-build-end" ]  

