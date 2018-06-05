FROM debian:jessie  
MAINTAINER Briefy <developers@briefy.co>  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
  
RUN mkdir /root/.aws/  
  
# Add aws configuration  
ADD ./aws_config /root/.aws/config  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
git \  
libsqlite3-0 \  
libpq5 \  
libpq-dev \  
libssl1.0.0 \  
openssh-client \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D  
  
ENV PYTHON_VERSION 3.6.3  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 9.0.1  
  
RUN set -ex \  
&& buildDeps=' \  
curl \  
gcc \  
libbz2-dev \  
libc6-dev \  
liblzma-dev \  
libmemcached11 \  
libmemcached-dev \  
libncurses-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
make \  
tcl-dev \  
tk-dev \  
xz-utils \  
zlib1g-dev \  
' \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python \  
&& ./configure \  
\--enable-loadable-sqlite-extensions \  
\--enable-shared \  
&& make -j$(nproc) \  
&& make install \  
&& ldconfig \  
&& pip3 install --no-cache-dir --upgrade pip==$PYTHON_PIP_VERSION \  
&& pip3 install --no-cache-dir --upgrade psycopg2 pycrypto \  
&& pip3 install --no-cache-dir --upgrade pylibmc --install-option="--with-
libmemcached=/usr" \  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /usr/src/python ~/.cache  
  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin \  
&& ln -s easy_install-3.6 easy_install \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s pip3 pip \  
&& ln -s python3-config python-config  
  
# Install base requirements  
ADD ./requirements.txt /requirements.txt  
RUN pip3 install --no-cache-dir --upgrade -r /requirements.txt && rm
/requirements.txt  
  
CMD ["python3"]  
  

