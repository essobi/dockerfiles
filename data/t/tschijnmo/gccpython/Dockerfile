FROM gcc:latest  
  
#  
# Installation of Python 3  
#  
# The following are primarily based on the official Docker image for Python at  
# https://hub.docker.com/_/python.  
#  
# ensure local python is preferred over distribution python  
ENV PATH /usr/local/bin:$PATH  
  
# runtime dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
tcl \  
tk \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D  
ENV PYTHON_VERSION 3.6.4  
  
RUN set -ex \  
&& buildDeps=' \  
dpkg-dev \  
tcl-dev \  
tk-dev \  
' \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -rf "$GNUPGHOME" python.tar.xz.asc \  
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
  
RUN set -ex; \  
pip3 list --outdated | awk '{print $1}' | xargs pip3 install -U  
  
  
#  
# Install cmake  
#  
  
RUN set -ex \  
&& wget -O cmake.tar.gz "https://cmake.org/files/v3.10/cmake-3.10.1.tar.gz" \  
&& mkdir -p /usr/src/cmake \  
&& tar -xzC /usr/src/cmake --strip-components=1 -f cmake.tar.gz \  
&& rm cmake.tar.gz \  
\  
&& cd /usr/src/cmake \  
&& ./bootstrap && make && make install \  
&& rm -rf /usr/src/cmake  
  

