FROM ferreol/yorick  
  
MAINTAINER Ferréol Soulez <ferreol.soulez@univ-lyon1.fr>  
  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
apk add \--update \--no-cache \--virtual .build-deps make wget build-base zip
&& \  
mkdir -p /opt && cd /opt && \  
wget https://github.com/emmt/Yeti/archive/master.zip && \  
unzip master.zip && rm master.zip && cd Yeti-master &&\  
./configure \--with-fftw=no \--with-regex=yes \--with-tiff=no && \  
make all && make install && cd /opt && rm -rf Yeti-master &&\  
cd /opt/yorick/i-start && ln -s ../i0/yeti.i yeti.i && \  
apk del .build-deps && \  
rm -rf /var/cache/apk/*  
  

