FROM alpine  
  
ENV PKG_CONFIG_PATH /usr/local/lib/pkgconfig  
ENV DEV_PACKAGES wget tar gcc make g++ ncurses-dev zlib-dev  
ENV RUNTIME ncurses-libs ncurses zlib  
  
RUN mkdir /workplace  
  
WORKDIR /workplace  
RUN apk --no-cache add $DEV_PACKAGES $RUNTIME && \  
wget -qO- http://caca.zoy.org/files/libcaca/libcaca-0.99.beta19.tar.gz | tar
xz && \  
cd /workplace/libcaca-0.99.beta19 && \  
./configure && \  
make install clean && \  
cd /workplace && \  
wget -qO- http://caca.zoy.org/raw-attachment/wiki/toilet/toilet-0.3.tar.gz |
tar xz && \  
cd /workplace/toilet-0.3 && \  
./configure && \  
make install clean && \  
cd fonts && \  
make install && \  
cd && \  
apk del $DEV_PACKAGES && \  
rm -rf /workplace  
  
ENTRYPOINT [ "toilet" ]

