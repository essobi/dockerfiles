FROM buildpack-deps:jessie  
  
  
ENV NODE_VERSION="5.12.0" \  
PHANTOMJS_VERSION="2.1.14" \  
PYTHON_VERSION="2.7.13"  
LABEL com.moccu.type="djuggernaut" \  
com.moccu.version.node="${NODE_VERSION}" \  
com.moccu.version.phantom="${PHANTOMJS_VERSION}" \  
com.moccu.version.python="${PYTHON_VERSION}"  
  
# Libraries  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
bzip2 \  
locales \  
libpq-dev \  
libjpeg-dev \  
liblcms2-dev \  
libfreetype6 \  
libfontconfig \  
zlib1g-dev \  
libxml2-dev \  
libxslt1-dev \  
fontforge \  
ttfautohint \  
&& apt-get purge -y python.* \  
&& apt-get autoremove -y \  
&& apt-get clean all \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8  
  
ENV LANG=en_US.UTF-8  
# Phantom  
# Todo: Validate hash  
RUN mkdir -p /srv/var \  
&& wget -q -O /tmp/phantomjs-$PHANTOMJS_VERSION.tar.gz \  
https://github.com/paladox/phantomjs/archive/$PHANTOMJS_VERSION.tar.gz \  
&& tar -xzf /tmp/phantomjs-$PHANTOMJS_VERSION.tar.gz -C /tmp \  
&& rm -f /tmp/phantomjs-$PHANTOMJS_VERSION.tar.gz \  
&& mv /tmp/phantomjs-$PHANTOMJS_VERSION/ /srv/var/phantomjs \  
&& ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs  
  
# Node  
ENV NPM_CONFIG_LOGLEVEL info  
  
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
; do gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; done  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
RUN npm install -g jspm grunt-cli  
  
# Python  
RUN set -ex \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
"C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
&& cd /usr/src/python \  
&& ./configure --enable-shared --enable-unicode=ucs4 \  
&& make -j$(nproc) \  
&& make install \  
&& ldconfig \  
&& curl -fSL 'https://bootstrap.pypa.io/get-pip.py' | python2 \  
&& pip install --no-cache-dir --upgrade --ignore-installed pip setuptools
wheel \  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python ~/.cache  
  
CMD ["bash"]  

