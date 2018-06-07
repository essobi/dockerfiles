FROM debian:jessie  
  
ENV OPENVAS_LIBRARIES_VERSION=8.0.7 \  
OPENVAS_GSA_VERSION=6.0.10  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends --fix-missing \  
pkg-config libssh-dev libgnutls28-dev libglib2.0-dev libpcap-dev \  
libgpgme11-dev uuid-dev bison libksba-dev libhiredis-dev libsnmp-dev \  
rsync wget cmake build-essential libgcrypt-dev libldap2-dev doxygen \  
libmicrohttpd-dev libxml2-dev libglib2.0-dev libxslt-dev xsltproc gettext && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /openvas-src && \  
  
# Building openvas-libraries  
cd /openvas-src && \  
wget -nv http://wald.intevation.org/frs/download.php/2291/openvas-
libraries-${OPENVAS_LIBRARIES_VERSION}.tar.gz && \  
tar zxvf openvas-libraries-${OPENVAS_LIBRARIES_VERSION}.tar.gz && \  
cd /openvas-src/openvas-libraries-${OPENVAS_LIBRARIES_VERSION} && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make -j $(nproc) && \  
make install && \  
make rebuild_cache && \  
  
# Building Greenbone Security Assistant  
cd /openvas-src && \  
wget -nv http://wald.intevation.org/frs/download.php/2299/greenbone-security-
assistant-${OPENVAS_GSA_VERSION}.tar.gz && \  
tar zxvf greenbone-security-assistant-${OPENVAS_GSA_VERSION}.tar.gz && \  
cd /openvas-src/greenbone-security-assistant-${OPENVAS_GSA_VERSION} && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make -j $(nproc) && \  
make install && \  
make rebuild_cache && \  
  
ldconfig  
  
EXPOSE 80  
  
ENTRYPOINT [ "/usr/local/sbin/gsad" ]  
CMD [ "--help" ]  

