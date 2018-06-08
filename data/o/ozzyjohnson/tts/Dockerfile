FROM debian:wheezy  
  
MAINTAINER Ozzy Johnson <docker@ozzy.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV ESPEAK_REPO https://github.com/rhdunn/espeak.git  
  
# So we can grab wxWidgets 3.0 - the 2.8 version in the repos will bomb.  
RUN apt-key adv --fetch-keys http://repos.codelite.org/CodeLite.asc \  
&& echo "deb http://repos.codelite.org/wx3.0.2/debian/ wheezy libs" \  
>> /etc/apt/sources.list  
  
# For MBROLA and voices.  
RUN echo "deb http://http.debian.net/debian wheezy non-free" \  
>> /etc/apt/sources.list  
  
# Update and install minimal.  
RUN \  
apt-get update \  
\--quiet \  
&& apt-get install \  
\--yes \  
\--no-install-recommends \  
\--no-install-suggests \  
autoconf=2.69-1 \  
automake=1:1.11.6-1 \  
ca-certificates \  
g++ \  
gcc=4:4.7.2-1 \  
git \  
libpulse-dev \  
libsox-fmt-mp3 \  
libtool=2.4.2-1.1 \  
libwxgtk3.0-dev \  
make=3.81-8.2 \  
mbrola \  
mbrola-us1 \  
mbrola-en1 \  
pkg-config \  
sox \  
xvfb \  
# Clean up packages.  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Get ready to build.  
WORKDIR /tmp  
  
# Get and build eSpeak.  
RUN \  
git clone $ESPEAK_REPO  
  
# We need a display variable and Xvfb since espeak depends on GTK.  
ENV DISPLAY :100.0  
RUN \  
Xvfb :100 > /dev/null 2>&1 \  
& cd espeak \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install \  
&& rm -rf /tmp/espeak  
  
VOLUME ["/data"]  
  
WORKDIR /data  
  
CMD ["bash"]  

