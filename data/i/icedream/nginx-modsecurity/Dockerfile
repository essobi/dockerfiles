FROM nginx:1.10.3  
  
MAINTAINER Carl Kittelberger "icedream@icedream.pw"  
  
# TODO - verify against Nginx GPG key ID: 7BD9BF62 (simply add the key to the
keyring, the verification seems to be done by apt-get source)  
  
ARG MODSECURITY_GIT_URL="https://github.com/SpiderLabs/ModSecurity.git"  
ARG MODSECURITY_VERSION="v3/master"  
ARG MODSECURITY_SOURCE_DIR="/usr/src/modsecurity-${MODSECURITY_VERSION}"  
ARG MODSECURITY_NGINX_VERSION=master  
ARG MODSECURITY_NGINX_GIT_URL=https://github.com/SpiderLabs/ModSecurity-
nginx.git  
ARG MODSECURITY_NGINX_SOURCE_DIR="/usr/src/modsecurity-
nginx-${MODSECURITY_NGINX_VERSION}"  
  
RUN apt-get update \  
&& apt-get install -yq --no-install-recommends \  
debian-keyring \  
dpkg-dev \  
lsb-release \  
&& apt-mark auto debian-keyring dpkg-dev \  
&& echo "deb-src http://nginx.org/packages/debian/ $(lsb_release -cs) nginx" \  
| tee -a /etc/apt/sources.list >/dev/null \  
&& apt-get update \  
&& (cd /usr/src \  
&& apt-get source nginx=${NGINX_VERSION} \  
) \  
&& apt-get build-dep -y nginx=${NGINX_VERSION} \  
&& apt-mark auto $(\  
apt-cache showsrc nginx |\  
sed -e '/Build-Depends/!d;s/Build-Depends: \|,\|([^)]*),*\|\[[^]]*\]//g' \  
) \  
&& apt-get install --no-install-recommends -y coreutils git \  
&& apt-mark auto git \  
&& apt-get install -y \  
autoconf \  
automake \  
autotools-dev \  
bison \  
curl \  
dh-autoreconf \  
doxygen \  
flex \  
g++ \  
libcurl3-gnutls \  
libcurl4-gnutls-dev \  
libgeoip1 \  
libgeoip-dev \  
libpcre++0 \  
libpcre++-dev \  
libtool \  
libxml2 \  
libxml2-dev \  
libyajl2 \  
libyajl-dev \  
&& apt-mark auto \  
autoconf \  
automake \  
autotools-dev \  
bison \  
dh-autoreconf \  
doxygen \  
flex \  
g++ \  
libcurl4-gnutls-dev \  
libgeoip-dev \  
libpcre++-dev \  
libtool \  
libxml2-dev \  
libyajl-dev \  
&& git clone "${MODSECURITY_GIT_URL}" "${MODSECURITY_SOURCE_DIR}" \  
&& (cd "${MODSECURITY_SOURCE_DIR}" \  
&& git checkout "${MODSECURITY_VERSION}" \  
&& sh ./build.sh \  
&& git submodule update --init \  
&& ./configure \  
&& make -j$(nproc) \  
&& make install \  
) \  
&& git clone "${MODSECURITY_NGINX_GIT_URL}" "${MODSECURITY_NGINX_SOURCE_DIR}"
\  
&& (cd "${MODSECURITY_NGINX_SOURCE_DIR}" \  
&& git checkout "${MODSECURITY_NGINX_VERSION}" \  
) \  
&& (cd /usr/src/nginx-*/ \  
&& mkdir -p debian/modules \  
&& ln -s "${MODSECURITY_NGINX_SOURCE_DIR}" debian/modules/modsecurity \  
&& sed -i 's,\\./configure,\\./configure --add-
module=$(MODULESDIR)/modsecurity,' debian/rules \  
&& DEB_BUILD_OPTIONS=nodoc dpkg-buildpackage -b -uc -us -tc -j$(nproc) \  
&& dpkg -i ../nginx_*.deb \  
) \  
&& apt-get autoremove --purge -y \  
&& rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /usr/src/modsecurity*
/usr/src/nginx*  

