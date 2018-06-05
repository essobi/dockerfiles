FROM debian:jessie  
MAINTAINER FluxoTI <lucas.gois@fluxoti.com>  
  
RUN useradd --system asterisk  
  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends \  
subversion \  
automake \  
aptitude \  
autoconf \  
binutils-dev \  
build-essential \  
ca-certificates \  
curl \  
libcurl4-openssl-dev \  
libedit-dev \  
libgsm1-dev \  
libjansson-dev \  
libogg-dev \  
libpopt-dev \  
libresample1-dev \  
libspandsp-dev \  
libspeex-dev \  
libspeexdsp-dev \  
libsqlite3-dev \  
libsrtp0-dev \  
libssl-dev \  
libvorbis-dev \  
libxml2-dev \  
libxslt1-dev \  
portaudio19-dev \  
python-pip \  
unixodbc-dev \  
uuid \  
uuid-dev \  
xmlstarlet \  
unixodbc \  
unixodbc-dev \  
libmyodbc \  
python-dev \  
python-pip \  
python-mysqldb \  
git \  
&& \  
apt-get purge -y --auto-remove && rm -rf /var/lib/apt/lists/* && \  
pip install alembic  
  
ENV ASTERISK_VERSION=14.3.0 PJPROJECT_VERSION=2.5.5  
COPY build-asterisk.sh /build-asterisk  
RUN /build-asterisk  
  
CMD ["/usr/sbin/asterisk", "-f"]

