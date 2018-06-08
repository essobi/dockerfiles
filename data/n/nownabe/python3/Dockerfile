FROM alpine:3.5  
MAINTAINER nownabe  
  
ENV PATH /usr/local/bin:$PATH  
ENV LANG C.UTF-8  
  
ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D  
ENV PYTHON_VERSION 3.6.0  
ENV PYTHON_PIP_VERSION 9.0.1  
  
RUN apk update --no-cache \  
# run deps  
&& apk add --no-cache ca-certificates musl zlib openssl \  
# fetch python  
&& apk add --no-cache --virtual .fetch-deps gnupg openssl tar xz \  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
# build & install python  
&& apk add --no-cache --virtual .build-deps \  
bzip2-dev \  
gcc \  
gdbm-dev \  
libc-dev \  
linux-headers \  
make \  
ncurses-dev \  
openssl-dev \  
pax-utils \  
readline-dev \  
sqlite-dev \  
tcl-dev \  
tk \  
tk-dev \  
xz-dev \  
zlib-dev \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
&& cd /usr/src/python \  
&& ./configure \  
\--enable-loadable-sqlite-extensions \  
\--enable-shared \  
\--enable-optimization \  
&& make -j $(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& cd \  
# create links  
&& ln -s /usr/local/bin/idle3 /usr/local/bin/idle \  
&& ln -s /usr/local/bin/pydoc3 /usr/local/bin/pydoc \  
&& ln -s /usr/local/bin/python3 /usr/local/bin/python \  
&& ln -s /usr/local/bin/python3-config /usr/local/bin/python-config \  
&& ln -s /usr/local/bin/pip3 /usr/local/bin/pip \  
&& ln -s /usr/local/bin/easy_install-3.6 /usr/local/bin/easy_install \  
# clean up  
&& apk del .build-deps .fetch-deps \  
&& rm -rf /usr/src/python ~/.cache \  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' +  

