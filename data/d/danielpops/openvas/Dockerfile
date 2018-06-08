FROM ubuntu:xenial  
MAINTAINER danielpops@gmail.com  
  
RUN apt-get update > /dev/null \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
alien \  
autoconf \  
bison \  
clang \  
cmake \  
curl \  
doxygen \  
flex \  
g++ \  
gcc \  
gcc-mingw-w64 \  
git \  
gnutls-bin \  
heimdal-dev \  
heimdal-multidev \  
libglib2.0-dev \  
libgnutls-dev \  
libgpgme11-dev \  
libhiredis-dev \  
libksba-dev \  
libldap2-dev \  
libmicrohttpd-dev \  
libpcap-dev \  
libpopt-dev \  
libsnmp-dev \  
libsqlite3-dev \  
libssh-dev \  
libxml2-dev \  
libxslt-dev \  
nsis \  
openssh-client \  
openssl \  
perl-base \  
pkg-config \  
python-lxml \  
python-pip \  
redis-server \  
rpm \  
rsync \  
sqlfairy \  
sqlite3 \  
tcl \  
texlive-latex-extra \  
texlive-fonts-recommended \  
uuid-dev \  
vim \  
wget \  
xmltoman \  
xsltproc \  
> /dev/null \  
&& apt-get clean  
  
  
# Install nmap from source  
# Openvas recommends an ancient version  
ENV NMAP_VERSION=nmap-7.60  
WORKDIR /nmap/  
RUN curl -O https://nmap.org/dist/$NMAP_VERSION.tar.bz2 \  
&& bzip2 -cd $NMAP_VERSION.tar.bz2 | tar xvf - > /dev/null \  
&& cd /nmap/$NMAP_VERSION/ \  
&& ./configure --prefix=/ > /dev/null \  
&& make > /dev/null \  
&& make install \  
&& rm -rf /nmap/  
  
WORKDIR /openvas  
  
RUN for i in openvas-libraries-9.0.1,2420 openvas-scanner-5.1.1,2423 openvas-
manager-7.0.2,2448 greenbone-security-assistant-7.0.2,2429 openvas-
cli-1.4.5,2397; do \  
IFS=","; \  
set -- $i; \  
wget http://wald.intevation.org/frs/download.php/$2/$1.tar.gz; \  
tar xfvz $1.tar.gz > /dev/null; \  
cd $1; \  
cmake . > /dev/null; \  
make install > /dev/null; \  
cd ..; \  
rm -rf $1; \  
rm -rf $1.tar.gz; \  
done  
  
RUN ldconfig  
  
ADD redis.conf /etc/redis/redis.conf  
ADD setup.sh setup.sh  
RUN chmod +x setup.sh  
  
# Takes very long  
RUN ./setup.sh  
  
ADD start.sh start.sh  
RUN chmod +x start.sh  
  
ENTRYPOINT ["/openvas/start.sh"]  

