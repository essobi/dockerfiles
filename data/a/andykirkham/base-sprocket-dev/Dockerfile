FROM ubuntu:xenial  
MAINTAINER Andy Kirkham  
  
# Command And Control node base definition  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update  
  
ENV PKGS \  
build-essential \  
software-properties-common \  
autoconf \  
g++ \  
gcc \  
make \  
bison \  
re2c \  
cmake \  
check \  
valgrind \  
apt-utils \  
ca-certificates \  
file \  
libc-dev \  
pkg-config \  
libffi-dev \  
libssl-dev \  
libxslt1-dev \  
libxml2 \  
libxml2-dev \  
curl \  
libcurl3 \  
libedit2 \  
libsqlite3-0 \  
libxml2 \  
xz-utils \  
vim \  
mlocate \  
wget \  
unzip \  
libmysqlclient-dev \  
mysql-client \  
libconfig9 \  
libconfig-dev \  
libbison-dev \  
libcurl4-gnutls-dev \  
libedit-dev \  
libevent-dev \  
libzmq3-dev \  
libnanomsg-dev \  
libmemcached-dev \  
libev-dev \  
librabbitmq-dev \  
git \  
netcat  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y $PKGS --no-install-
recommends  
  
# We want the latest (we can at least) version of Jansson, even in 16.04 we
get a hopelessly out-dated 2.5 version via apt-get  
# Not sure why there's no easy to install PPA for this.  
WORKDIR /tmp  
RUN curl -sSL
https://launchpad.net/ubuntu/+archive/primary/+files/libjansson4_2.9-1_amd64.deb
> libjansson4_2.9-1_amd64.deb \  
&& dpkg -i libjansson4_2.9-1_amd64.deb \  
&& rm -f libjansson4_2.9-1_amd64.deb  
RUN curl -sSL https://launchpad.net/ubuntu/+archive/primary/+files/libjansson-
dev_2.9-1_amd64.deb > libjansson-dev_2.9-1_amd64.deb \  
&& dpkg -i libjansson-dev_2.9-1_amd64.deb \  
&& rm -f libjansson-dev_2.9-1_amd64.deb  
RUN curl -sSL
https://launchpad.net/ubuntu/+archive/primary/+files/libjansson4-dbgsym_2.9-1_amd64.ddeb
> libjansson4-dbgsym_2.9-1_amd64.ddeb \  
&& dpkg -i libjansson4-dbgsym_2.9-1_amd64.ddeb \  
&& rm -f libjansson4-dbgsym_2.9-1_amd64.ddeb  
  
ENV HTTP_PARSER_VER "2.7.1"  
  
RUN curl -sSL https://github.com/nodejs/http-
parser/archive/v$HTTP_PARSER_VER.zip > http-parser-$HTTP_PARSER_VER.zip \  
&& unzip http-parser-$HTTP_PARSER_VER.zip \  
&& cd http-parser-$HTTP_PARSER_VER \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf http-parser-$HTTP_PARSER_VER \  
&& rm http-parser-$HTTP_PARSER_VER.zip \  
&& cp /usr/local/lib/libhttp_parser.so.$HTTP_PARSER_VER /usr/lib/x86_64-linux-
gnu/ \  
&& ln -s /usr/lib/x86_64-linux-gnu/libhttp_parser.so.$HTTP_PARSER_VER
/usr/lib/x86_64-linux-gnu/libhttp_parser.so  
  
RUN mkdir -p /workspace  
WORKDIR /workspace  
  

