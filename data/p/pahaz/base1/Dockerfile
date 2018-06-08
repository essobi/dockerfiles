FROM buildpack-deps:stretch  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates curl wget \  
gnupg2 dirmngr \  
git openssh-client \  
&& rm -rf /var/lib/apt/lists/*  
  
# KEYS!  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D \  
; do \  
gpg --keyserver keyserver.ubuntu.com --recv-keys "$key" || \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
# ############  
# unprivileged  
# ############  
# explicitly set user/group IDs  
RUN groupadd -r unprivileged --gid=999 && useradd -m -r -g unprivileged
--uid=999 unprivileged  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.10  
RUN set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -rf /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# ####  
# NODE 6.11 at https://github.com/nodejs/docker-
node/blob/17c50cb300581280805a4183524fbf57840f3a7e/6.11/stretch/Dockerfile  
# ####  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.11.3  
RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
&& case "${dpkgArch##*-}" in \  
amd64) ARCH='x64';; \  
ppc64el) ARCH='ppc64le';; \  
s390x) ARCH='s390x';; \  
arm64) ARCH='arm64';; \  
armhf) ARCH='armv7l';; \  
*) echo "unsupported architecture"; exit 1 ;; \  
esac \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
ENV YARN_VERSION 0.27.5  
RUN set -ex \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
# ######  
# PYTHON 3.6 at https://github.com/docker-
library/python/blob/c9954b06c8b178d7888bc1626bed5a14e43a9203/3.6/stretch/Dockerfile  
# ######  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# runtime dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
tcl \  
tk \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PYTHON_VERSION 3.6.2  
RUN set -ex \  
&& buildDeps=' \  
dpkg-dev \  
tcl-dev \  
tk-dev \  
' \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -rf python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--enable-loadable-sqlite-extensions \  
\--enable-shared \  
\--with-system-expat \  
\--with-system-ffi \  
\--without-ensurepip \  
&& make -j "$(nproc)" \  
&& make install \  
&& ldconfig \  
\  
&& apt-get purge -y --auto-remove $buildDeps \  
\  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python  
  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python3-config python-config  
  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 9.0.1  
RUN set -ex; \  
\  
wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \  
\  
python get-pip.py \  
\--disable-pip-version-check \  
\--no-cache-dir \  
"pip==$PYTHON_PIP_VERSION" \  
; \  
pip --version; \  
\  
find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' +; \  
rm -f get-pip.py  
  
# ######  
# DJANGO + PILLOW  
# ######  
# https://github.com/docker-
library/django/blob/819c332058c3638ab8f4fa5b9f70518e9aaf6325/3.4/Dockerfile  
# http://pillow.readthedocs.io/en/3.1.x/installation.html#building-on-linux  
# libcairo2-dev -- for pdf maker  
RUN apt-get update && apt-get install -y \  
gcc gettext \  
mysql-client \  
sqlite3 \  
postgresql-client libpq-dev binutils libproj-dev gdal-bin \  
libtiff5-dev libjpeg62-turbo-dev zlib1g-dev libfreetype6-dev \  
liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev \  
libxml2-dev libxslt-dev libffi-dev \  
libcairo2-dev \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --no-cache-dir --upgrade gunicorn uwsgi psycopg2 mysqlclient
virtualenv invoke Jinja2 ipython  
  
# Install PhantomJS release (TODO: add checksum!)  
ENV PHANTOM_VERSION phantomjs-2.1.1  
RUN set -x \  
&& apt-get update \  
&& cd /tmp \  
&& wget -q https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_VERSION-
linux-$(uname -m).tar.bz2 -O $PHANTOM_VERSION-linux-$(uname -m).tar.bz2 \  
&& tar xvjf $PHANTOM_VERSION-linux-$(uname -m).tar.bz2 \  
&& mv /tmp/$PHANTOM_VERSION-linux-$(uname -m)/bin/phantomjs
/usr/local/bin/phantomjs \  
&& rm -rf /tmp/* /var/lib/apt/lists/* \  
&& useradd --system --uid 7374 -m --shell /usr/sbin/nologin phantomjs \  
&& su phantomjs -s /bin/sh -c "phantomjs --version"  
  
RUN npm install -g bower && npm install -g gulp  
  
RUN apt-get update && apt-get upgrade -y  

