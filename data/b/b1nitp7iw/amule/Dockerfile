FROM alpine:latest  
MAINTAINER docker@chabs.name  
  
ENV AMULE_VERSION 2.3.2  
ENV UPNP_VERSION 1.6.22  
ENV CRYPTOPP_VERSION CRYPTOPP_5_6_5  
ENV CADDYPATH /home/amule/  
  
RUN apk --update add gd geoip libpng libwebp runit wxgtk2.8 zlib && \  
apk --update add --virtual build-dependencies alpine-sdk automake autoconf
bison g++ gcc gd-dev geoip-dev gettext gettext-dev git libpng-dev libwebp-dev
libtool libsm-dev make musl-dev wget curl wxgtk2.8-dev zlib-dev  
  
RUN mkdir -p /home/amule/.aMule  
  
# Build libupnp  
RUN mkdir -p /opt && cd /opt && \  
wget
"http://downloads.sourceforge.net/sourceforge/pupnp/libupnp-${UPNP_VERSION}.tar.bz2"
&& \  
tar xvfj libupnp*.tar.bz2 && cd libupnp* && ./configure --prefix=/usr && make
&& make install  
  
# Build crypto++  
RUN mkdir -p /opt && cd /opt && \  
git clone \--branch ${CRYPTOPP_VERSION} \--single-branch
"https://github.com/weidai11/cryptopp" /opt/cryptopp && \  
cd /opt/cryptopp && \  
sed -i -e 's/^CXXFLAGS/#CXXFLAGS/' GNUmakefile && export CXXFLAGS="${CXXFLAGS}
-DNDEBUG -fPIC" && \  
make -f GNUmakefile && make libcryptopp.so && install -Dm644 libcryptopp.so*
/usr/lib/ && \  
mkdir -p /usr/include/cryptopp && install -m644 *.h /usr/include/cryptopp/  
  
# Build amule from source  
RUN mkdir -p /opt/amule && \  
git clone \--branch ${AMULE_VERSION} \--single-branch
"https://github.com/amule-project/amule" /opt/amule && \  
cd /opt/amule && ./autogen.sh && ./configure \  
\--disable-gui \  
\--disable-amule-gui \  
\--disable-wxcas \  
\--disable-alc \  
\--disable-plasmamule \  
\--disable-kde-in-home \  
\--prefix=/usr \  
\--mandir=/usr/share/man \  
\--enable-unicode \  
\--without-subdirs \  
\--without-expat \  
\--enable-amule-daemon \  
\--enable-amulecmd \  
\--enable-webserver \  
\--enable-cas \  
\--enable-alcc \  
\--enable-fileview \  
\--enable-geoip \  
\--enable-mmap \  
\--enable-optimize \  
\--enable-upnp \  
\--disable-debug && \  
make && \  
make install  
  
RUN curl -o rclone-current-linux-amd64.zip
https://downloads.rclone.org/rclone-current-linux-amd64.zip \  
&& unzip rclone-current-linux-amd64.zip \  
&& mv /rclone-*-linux-amd64/rclone /usr/bin/ \  
&& rm -rf /rclone-*-linux-amd64 \  
&& rm rclone-current-linux-amd64.zip  
  
RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip  
RUN unzip ngrok-stable-linux-amd64.zip  
RUN mv ngrok /home/amule  
RUN rm ngrok-stable-linux-amd64.zip  
  
RUN wget -O "caddy.tar.gz"
"https://caddyserver.com/download/linux/amd64?plugins=http.filemanager&license=personal"  
RUN tar zxvf caddy.tar.gz  
RUN mv caddy /usr/bin/  
RUN rm -rf ./init  
  
RUN wget -O supercronic
https://github.com/aptible/supercronic/releases/download/v0.1.5/supercronic-
linux-amd64  
RUN chmod +x supercronic  
RUN mv supercronic /usr/bin/  
  
# Add startup script  
ADD Caddyfile /etc/Caddyfile  
  
ADD *.sh /home/amule/  
  
RUN chmod -R 777 /home/amule  
  
RUN rm -rf /var/cache/apk/* && rm -rf /opt && apk del build-dependencies  
  
WORKDIR /home/amule/.aMule  
  
EXPOSE 4711/tcp 4712/tcp 4672/udp 4665/udp 4662/tcp 4661/tcp 8080/tcp  
  
CMD ["/home/amule/amule.sh"]  
  

