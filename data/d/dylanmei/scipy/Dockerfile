FROM debian:jessie  
  
# Remove traces of debian python  
RUN apt-get purge -y python.*  
  
# http://bugs.python.org/issue19846  
ENV LANG C.UTF-8  
# OS pre-requisites  
RUN apt-get update && apt-get install -y --no-install-recommends \  
curl \  
net-tools \  
ca-certificates \  
libssl1.0.0 \  
&& rm -rf /var/lib/apt/lists/*  
  
# Python 3 and SciPy stack  
# gpg: key F73C700D: public key "Larry Hastings <larry@hastings.org>" imported  
ENV GPG_KEY 97FC712E4C024BBEA48A61ED3A5CA953F73C700D  
ENV PYTHON_VERSION 3.5.1  
ENV PYTHON_PIP_VERSION 8.0.2  
  
RUN set -ex \  
&& buildDeps=' \  
gcc \  
libbz2-dev \  
libc6-dev \  
libncurses-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
make \  
xz-utils \  
zlib1g-dev \  
pkg-config \  
g++ \  
gfortran \  
' \  
&& apt-get update && apt-get install -y --no-install-recommends \  
$buildDeps \  
libfreetype6-dev \  
libpng3 \  
liblapack-dev \  
libopenblas-dev \  
\  
&& rm -rf /var/lib/apt/lists/* \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc \  
&& gpg --verify python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz* \  
&& rm -r ~/.gnupg \  
\  
&& cd /usr/src/python \  
&& ./configure --enable-shared --enable-unicode=ucs4 \  
&& make -j$(nproc) \  
&& make install \  
&& ldconfig \  
&& pip3 install --no-cache-dir --upgrade --ignore-installed
pip==$PYTHON_PIP_VERSION \  
&& pip3 install numpy scipy pandas matplotlib scikit-learn \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /usr/src/python \  
\  
&& cd /usr/local/bin \  
&& ln -s easy_install-3.5 easy_install \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python-config3 python-config  
  
WORKDIR /usr/src  

