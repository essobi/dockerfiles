FROM alpine:3.3  
ENV HOME /home/tidal  
  
RUN mkdir -p $HOME  
  
RUN apk --update add \  
autoconf libtool automake \  
bash \  
curl \  
gcc g++ make \  
git \  
zlib \  
alsa-lib-dev \  
libsamplerate-dev \  
libsndfile-dev \  
linux-pam \  
python \  
&& addgroup root audio \  
&& echo "@audio - memlock 256000" >> /etc/security/limits.conf \  
&& echo "@audio - rtprio 75" >> /etc/security/limits.conf  
  
RUN cd $HOME \  
&& curl -L https://github.com/radarsat1/liblo/archive/0.28.tar.gz | tar xz \  
&& cd $HOME/liblo-0.28 \  
&& sed -i "s/^#include <sys\/poll.h>\s*$/#include <poll.h>/" ./src/server.c \  
&& sh ./autogen.sh \  
&& make \  
&& make install  
  
RUN git clone git://github.com/jackaudio/jack2 --depth 1 $HOME/jack2 \  
&& cd $HOME/jack2 \  
&& ./waf configure --alsa \  
&& ./waf build \  
&& ./waf install  
  
RUN git clone https://github.com/tidalcycles/Dirt $HOME/Dirt \  
&& cd $HOME/Dirt \  
&& make clean \  
&& make  
  
RUN cd $HOME/Dirt \  
&& git submodule update --init  
  
COPY dirt.sh $HOME/dirt.sh  
RUN chmod +x $HOME/dirt.sh  
  
WORKDIR $HOME  
ENTRYPOINT ./dirt.sh  

