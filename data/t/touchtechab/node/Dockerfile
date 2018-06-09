FROM buildpack-deps:jessie-curl  
  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 5.6.0  
ENV LIBVIPS_VERSION_MAJOR 8  
ENV LIBVIPS_VERSION_MINOR 2  
ENV LIBVIPS_VERSION_PATCH 2  
ENV LIBVIPS_VERSION
$LIBVIPS_VERSION_MAJOR.$LIBVIPS_VERSION_MINOR.$LIBVIPS_VERSION_PATCH  
  
WORKDIR /tmp/docker  
  
RUN buildDeps='xz-utils pkg-config lsb-release automake build-essential git' \  
&& set -x \  
&& apt-get update && apt-get install -y --no-install-recommends $buildDeps\  
curl \  
libglib2.0-dev \  
gettext \  
libxml2-dev \  
imagemagick \  
libmagick++-dev \  
libpng12-dev \  
libexif-dev \  
libgsf-1-dev \  
libjpeg-dev \  
liblcms2-dev \  
libmagickcore-dev \  
fftw3-dev \  
&& curl -O
http://www.vips.ecs.soton.ac.uk/supported/$LIBVIPS_VERSION_MAJOR.$LIBVIPS_VERSION_MINOR/vips-$LIBVIPS_VERSION.tar.gz
\  
&& tar zvxf vips-$LIBVIPS_VERSION.tar.gz \  
&& cd vips-$LIBVIPS_VERSION \  
&& ./configure --enable-debug=no --without-python --without-orc $1 \  
&& make \  
&& make install \  
&& ldconfig \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg \--verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/docker/* \  
&& apt-get purge -y --auto-remove $buildDeps  
  
CMD [ "node" ]  

