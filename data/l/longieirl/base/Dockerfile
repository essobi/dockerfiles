#  
# Base image Dockerfile  
#  
# Base  
FROM ubuntu:14.04  
  
MAINTAINER jlongieirl@gmail.com  
  
# Set environment variables  
ENV HOME /root  
ENV LANG C.UTF-8  
RUN locale-gen en_US.UTF-8  
ENV PYTHON_VERSION 2.7.10  
ENV PYTHON_PIP_VERSION 7.1.0  
  
RUN apt-get update  
RUN apt-get update --fix-missing  
RUN apt-get purge -y python.*  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ruby \  
git \  
git-core \  
curl \  
perl \  
wget \  
ca-certificates \  
autoconf \  
automake \  
bzip2 \  
file \  
g++ \  
gcc \  
libbz2-dev \  
libc6-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libwebp-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
make \  
patch \  
xz-utils \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -x \  
&& mkdir -p /usr/src/python \  
&& curl -SL
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz \  
&& curl -SL
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc \  
&& gpg --verify python.tar.xz.asc \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz* \  
&& cd /usr/src/python \  
&& ./configure --enable-shared --enable-unicode=ucs4 \  
&& make -j$(nproc) \  
&& make install \  
&& ldconfig \  
&& curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python \  
&& pip install --no-cache-dir --upgrade pip==$PYTHON_PIP_VERSION \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python  
  
# Define working directory  
WORKDIR /root  
  
# Define default command  
CMD ["bash"]  
  

