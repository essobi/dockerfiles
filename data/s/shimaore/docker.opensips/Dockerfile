FROM debian:testing-slim  
MAINTAINER Stéphane Alnet <stephane@shimaore.net>  
  
# Install prereqs  
ENV MODULES \  
b2b_logic \  
cachedb_redis \  
db_http \  
httpd \  
json \  
rest_client \  
presence \  
presence_mwi \  
presence_dialoginfo \  
proto_tls \  
proto_wss \  
pua \  
pua_dialoginfo \  
tls_mgm  
  
RUN apt-get update && apt-get --no-install-recommends -y install \  
bison \  
build-essential \  
ca-certificates \  
flex \  
git \  
libcurl4-gnutls-dev \  
libjson-c-dev \  
libhiredis-dev \  
libmicrohttpd-dev \  
libncurses5-dev \  
libsctp-dev \  
libssl-dev \  
libxml2-dev \  
m4 \  
netbase \  
pkg-config \  
&& \  
useradd -m opensips && \  
mkdir -p /opt/opensips && \  
chown -R opensips.opensips /opt/opensips \  
&& \  
cd /home/opensips \  
&& \  
git clone -b 2.3 https://github.com/OpenSIPS/opensips.git opensips.git && \  
cd opensips.git && \  
git checkout cf9c0f17ebd193ab0becc5fd8c9dff4c11b3b0bb && \  
make TLS=1 SCTP=1 prefix=/opt/opensips include_modules="${MODULES}" && \  
make TLS=1 SCTP=1 prefix=/opt/opensips include_modules="${MODULES}" modules &&
\  
make TLS=1 SCTP=1 prefix=/opt/opensips include_modules="${MODULES}" install &&
\  
cd .. && \  
rm -rf opensips.git \  
&& \  
apt-get purge -y \  
bison \  
build-essential \  
ca-certificates \  
cpp-6 \  
flex \  
gcc-6 \  
git \  
m4 \  
pkg-config \  
&& apt-get autoremove -y && \  
apt-get install -y \  
libmicrohttpd12 \  
&& apt-get clean \  
&& rm -rf \  
/opt/opensips/etc/opensips/opensips.cfg \  
/opt/opensips/etc/opensips/tls/ \  
&& chown opensips /opt/opensips/etc/opensips/  
USER opensips  
WORKDIR /home/opensips  

