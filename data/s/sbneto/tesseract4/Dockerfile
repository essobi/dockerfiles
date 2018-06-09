FROM sbneto/phusion-python:3.6  
# https://github.com/DanBloomberg/leptonica/releases  
# https://github.com/tesseract-ocr/tesseract/commits/master  
ENV LEPTONICA_VERSION="1.75.1" \  
TESSERACT_SHA="ce7ee87fa40745f9e4cb13ec0329787afd13ff56" \  
TESSDATA_PREFIX="/usr/local/share" \  
PATH="/usr/local/bin:/usr/local/lib:$PATH"  
  
RUN set -ex \  
&& apt-get update \  
&& buildDeps=" \  
g++ \  
autoconf \  
automake \  
libtool \  
autoconf-archive \  
pkg-config \  
libpng-dev \  
libjpeg8-dev \  
libtiff5-dev \  
libgif-dev \  
zlib1g-dev \  
" \  
&& apt-get install -y --no-install-recommends \  
$buildDeps \  
libpng12-0 \  
libjpeg8 \  
libtiff5 \  
libgif7 \  
zlib1g \  
wget \  
git \  
unzip \  
# DOWNLOADING LEPTONICA  
&& wget -O leptonica.tar.gz
"https://github.com/DanBloomberg/leptonica/releases/download/$LEPTONICA_VERSION/leptonica-$LEPTONICA_VERSION.tar.gz"
\  
&& mkdir -p /usr/src/leptonica \  
&& tar -xzC /usr/src/leptonica -f leptonica.tar.gz \  
&& rm leptonica.tar.gz \  
# DOWNLOADING TESSERACT  
&& wget -O tesseract.zip "https://github.com/tesseract-
ocr/tesseract/archive/$TESSERACT_SHA.zip" \  
&& mkdir -p /usr/src/tesseract \  
&& unzip tesseract.zip -d /usr/src/tesseract \  
&& rm tesseract.zip \  
# COMPILING LEPTONICA  
&& cd /usr/src/leptonica/leptonica-$LEPTONICA_VERSION \  
&& autoreconf -vi \  
&& ./autobuild \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /usr/src/leptonica \  
# COMPILING TESSERACT  
&& cd /usr/src/tesseract/tesseract-$TESSERACT_SHA \  
&& ./autogen.sh \  
&& ./configure LDFLAGS="-L/usr/local/lib" CFLAGS="-O2 -I/usr/local/include" \  
&& make \  
&& make install \  
&& ldconfig \  
&& rm -rf /usr/src/tesseract \  
# CLEANUP  
&& apt-get purge -yqq $buildDeps \  
&& apt-get autoremove -yqq \  
&& apt-get clean \  
&& rm -Rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  

