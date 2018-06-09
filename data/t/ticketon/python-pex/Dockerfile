FROM debian:jessie  
LABEL maintainer "Fill Quazy <admin@njoyx.net> (@drfill)"  
  
ENV PATH /usr/local/bin:$PATH  
ENV LANG C.UTF-8  
ENV GPG_KEY C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF  
ENV BUILD_DIR '/build'  
  
ARG PY_VERSION  
ARG PY_PIP_VERSION  
  
ENV PYTHON_VERSION ${PY_VERSION:-'2.7.14'}  
ENV PYTHON_PIP_VERSION ${PY_PIP_VERSION:-'9.0.1'}  
  
RUN set -ex; \  
apt-get update && apt-get install -y --no-install-recommends \  
tcl \  
tk \  
ca-certificates \  
curl \  
wget \  
bzr \  
git \  
mercurial \  
openssh-client \  
subversion \  
procps  
  
RUN set -ex; \  
mkdir -p ${BUILD_DIR}; \  
if ! command -v gpg > /dev/null; then \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
gnupg2 \  
dirmngr \  
; \  
fi  
  
RUN set -ex; \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >
/etc/apt/sources.list.d/pgdg.list; \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add -; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
autoconf \  
automake \  
bzip2 \  
dpkg-dev \  
file \  
g++ \  
gcc \  
imagemagick \  
libbz2-dev \  
libc6-dev \  
libcurl4-openssl-dev \  
libdb-dev \  
libevent-dev \  
libffi-dev \  
libgdbm-dev \  
libgeoip-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libkrb5-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libncurses-dev \  
libpng-dev \  
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
dpkg-dev \  
tcl-dev \  
tk-dev \  
libtiff5-dev \  
libfreetype6-dev \  
liblcms2-dev \  
libopenjpeg-dev \  
libwebp-dev \  
libsnappy-dev \  
liblz4-dev \  
\  
$( \  
if apt-cache show 'default-libmysqlclient-dev' 2>/dev/null | grep -q
'^Version:'; then \  
echo 'default-libmysqlclient-dev'; \  
else \  
echo 'libmysqlclient-dev'; \  
fi \  
); \  
rm -rf /var/lib/apt/lists/*  
  
RUN set -ex \  
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
\--enable-shared \  
\--enable-unicode=ucs4 \  
&& make -j "$(nproc)" \  
&& make install \  
&& ldconfig \  
\  
&& find /usr/local -depth \  
\( \  
\( -type d -a \( -name test -o -name tests \) \) \  
-o \  
\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \  
\) -exec rm -rf '{}' + \  
&& rm -rf /usr/src/python  
  
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
\( \  
\( -type d -a \( -name test -o -name tests \) \) \  
-o \  
\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \  
\) -exec rm -rf '{}' +; \  
rm -f get-pip.py  
  
RUN set -ex \  
&& mkdir -p $HOME/.ssh/ \  
&& printf "Host github.com\n\tStrictHostKeyChecking no\n" >> $HOME/.ssh/config
\  
&& printf "Host gist.github.com\n\tStrictHostKeyChecking no\n" >>
$HOME/.ssh/config \  
&& printf "Host bitbucket.org\n\tStrictHostKeyChecking no\n" >>
$HOME/.ssh/config \  
&& printf "Host gitlab.com\n\tStrictHostKeyChecking no\n" >> $HOME/.ssh/config
\  
&& ssh-keygen -f $HOME/.ssh/id_rsa -t rsa -N '' -b 4096  
  
WORKDIR ${BUILD_DIR}  
  
RUN pip install --no-cache-dir pex virtualenv "ipython<6"  
VOLUME ["${BUILD_DIR}", "${BUILD_DIR}/dist"]  
  
CMD ["ipython"]

