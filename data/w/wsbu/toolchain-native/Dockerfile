FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install --yes --no-install-recommends \  
apt-transport-https \  
autoconf \  
automake \  
autopoint \  
bc \  
bison \  
ca-certificates \  
ccache \  
curl \  
docbook-xml \  
docbook-xsl \  
doxygen \  
fakeroot \  
flex \  
g++ \  
gawk \  
gcc \  
gettext \  
git-core \  
golang-1.10 \  
gperf \  
graphviz \  
groff \  
inotify-tools \  
intltool \  
kmod \  
liblist-moreutils-perl \  
liblzo2-dev \  
libtool \  
libxml-dom-perl \  
libxml2-utils \  
lua5.3 \  
make \  
net-tools \  
nodejs \  
npm \  
openssh-client \  
pkg-config \  
python \  
python-m2crypto \  
python-pip \  
python-setuptools \  
python-wheel \  
rsync \  
scons \  
sudo \  
texinfo \  
u-boot-tools \  
uuid-dev \  
w3m \  
wget \  
xsltproc \  
xutils-dev \  
xz-utils \  
zip \  
zlib1g-dev \  
&& rm --recursive --force /var/lib/apt/lists/* \  
&& npm install -g showdown \  
&& pip --no-cache-dir install conan==1.3.0 \  
&& ln -sf /bin/bash /bin/sh \  
&& ln -sf /usr/bin/lua5.3 /usr/bin/lua \  
&& ln -sf /usr/bin/nodejs /usr/bin/node \  
&& ln -sf /usr/lib/go-1.10/bin/gofmt /usr/bin/gofmt \  
&& ln -sf /usr/lib/go-1.10/bin/go /usr/bin/go  
  
  
RUN mkdir /src \  
&& wget --quiet -O /src/cmake.sh
https://cmake.org/files/v3.10/cmake-3.10.2-Linux-x86_64.sh \  
&& sh /src/cmake.sh --prefix=/usr/local --exclude-subdir --skip-license \  
&& git clone https://github.com/wsbu/cross-browser.git \  
\--branch x419_z1 --depth 1 /src/crossbrowser \  
&& cd /src/crossbrowser/x/xc \  
&& gcc -c xc.c -O2 \  
&& gcc -o xc xc.o -O2 \  
&& cp --force xc /bin \  
&& strip /bin/xc \  
&& mkdir --parents /lib/crossbrowser \  
&& cp --archive /src/crossbrowser/x/lib/*.js /lib/crossbrowser \  
&& cp --archive /src/crossbrowser/x/lib/old/*.js /lib/crossbrowser \  
&& git clone https://github.com/wsbu/mtd-utils.git \  
\--branch v2.0.1 --depth 1 /src/mtd-utils \  
&& cd /src/mtd-utils \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& rm --recursive --force /src  
  
ENV HOME=/home/captain \  
CONAN_PRINT_RUN_COMMANDS=1  
COPY conan/profile "${HOME}/.conan/profiles/default"  
COPY conan/settings.yml "${HOME}/.conan/settings.yml"  
COPY conan/registry.txt "${HOME}/.conan/registry.txt"  
  
RUN groupadd --gid 1000 captain \  
&& useradd --home-dir "$HOME" \  
\--uid 1000 --gid 1000 \  
captain \  
&& mkdir --parents \  
$HOME/.ssh \  
&& chown --recursive captain:captain "$HOME" \  
&& chmod --recursive 777 "$HOME" \  
&& echo "ALL ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
  
COPY start.sh /start.sh  
ENTRYPOINT ["/start.sh"]  

