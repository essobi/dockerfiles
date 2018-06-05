FROM asvinours/php-base:latest  
  
RUN apt-get update \  
&& apt-get install -y \  
g++ \  
rsync \  
cmake \  
pngquant \  
autoconf \  
automake \  
libtool \  
nasm \  
make \  
imagemagick  
  
RUN mkdir -p /opt/mozjpeg \  
&& cd /opt/mozjpeg \  
&& git clone https://github.com/mozilla/mozjpeg.git . \  
&& git checkout v3.2 \  
&& autoreconf -fiv \  
&& mkdir build && cd build \  
&& sh ../configure \  
&& make install \  
&& ln -s /opt/mozjpeg/bin/jpegtran /usr/local/bin/mozjpeg  
  
RUN mkdir -p /opt/webp \  
&& cd /opt/webp \  
&& wget
https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-0.6.0.tar.gz
\  
&& tar -xzvf libwebp-0.6.0.tar.gz \  
&& cd libwebp-0.6.0 \  
&& ./configure --prefix=/usr \  
\--enable-libwebpmux \  
\--enable-libwebpdemux \  
\--enable-libwebpdecoder \  
\--enable-libwebpextras \  
\--enable-swap-16bit-csp \  
\--disable-static \  
&& make \  
&& make install  
  
RUN mkdir -p /opt/jpegoptim \  
&& cd /opt/jpegoptim \  
&& wget https://github.com/tjko/jpegoptim/archive/RELEASE.1.4.4.tar.gz \  
&& tar -xzvf RELEASE.1.4.4.tar.gz \  
&& cd jpegoptim-RELEASE.1.4.4 \  
&& ./configure \  
&& make \  
&& make strip \  
&& make install  
  
RUN mkdir -p /opt/butteraugli \  
&& cd /opt/butteraugli \  
&& git clone https://github.com/google/butteraugli.git . \  
&& cd butteraugli \  
&& make \  
&& ln -s "$(pwd)/butteraugli" /usr/local/bin/butteraugli  
  
RUN mkdir -p /opt/dssim \  
&& cd /opt/dssim \  
&& wget https://github.com/pornel/dssim/archive/1.3.2.tar.gz \  
&& tar -xzvf 1.3.2.tar.gz \  
&& cd dssim-1.3.2 \  
&& make \  
&& ln -s "$(pwd)/bin/dssim" /usr/local/bin/dssim  
  
RUN mkdir -p /opt/cjpeg-dssim \  
&& cd /opt/cjpeg-dssim \  
&& git clone https://github.com/technopagan/cjpeg-dssim.git . \  
&& ln -s "$(pwd)/cjpeg-dssim" /usr/local/bin/cjpeg-dssim  
  
  
ENV HOME /home/user  
  
CMD []  

