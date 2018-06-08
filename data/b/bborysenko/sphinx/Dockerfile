FROM alpine:3.6  
  
RUN set -xe ;\  
# The envsubst is used to generate Sphinx config  
apk add --no-cache libintl ;\  
apk add --no-cache --virtual .build_deps gettext ;\  
cp /usr/bin/envsubst /usr/local/bin/envsubst ;\  
apk del .build_deps ;\  
mv /usr/local/bin/envsubst /usr/bin/envsubst ;\  
# Create user, group and directory structure  
addgroup -g 82 -S sphinx ;\  
adduser -u 82 -S -D -h /var/lib/sphinx -s /sbin/nologin -G sphinx sphinx ;\  
mkdir -p /etc/sphinx/conf.d /var/log/sphinx /var/run/sphinx ;\  
chown sphinx:sphinx /var/log/sphinx /var/run/sphinx ;\  
# Install runtime dependencies  
apk add --no-cache \  
expat \  
libpq \  
libstdc++ \  
mariadb-client-libs \  
unixodbc ;\  
# Install build dependencies  
apk add --no-cache --virtual .build_deps \  
curl \  
expat-dev \  
g++ \  
gcc \  
libre2-dev \  
make \  
mariadb-dev \  
postgresql-dev \  
snowball-dev \  
unixodbc-dev \  
;\  
# Fetch Sphinx source code  
SPHINX_VERSION=2.3.2-beta ;\  
SPHINX_SOURCE="http://sphinxsearch.com/files/sphinx-${SPHINX_VERSION}.tar.gz"
;\  
curl -fSL --connect-timeout 30 ${SPHINX_SOURCE} | tar xz -C /tmp ;\  
cd /tmp/sphinx-${SPHINX_VERSION} ;\  
# Patch source code for Alpine  
sed -i 's/PAGE_SIZE/PAGE_SIZES/g' src/sphinx.cpp ;\  
sed -i '1493s/#ifndef __APPLE__/#if defined(linux) \&\& defined(__GLIBC__)/'
src/sphinxstd.cpp ;\  
  
./configure \  
\--prefix=/usr \  
\--exec-prefix=/usr \  
\--sysconfdir=/etc/sphinx \  
\--localstatedir=/var/lib/sphinx \  
\--enable-id64 \  
\--with-iconv \  
\--with-libexpat \  
\--with-libstemmer \  
\--with-mysql \  
\--with-pgsql \  
\--with-re2 \  
\--with-unixodbc \  
;\  
make -j $(getconf _NPROCESSORS_ONLN) ;\  
make install ;\  
# Clean  
apk del .build_deps ;\  
rm -rf /tmp/sphinx-${SPHINX_VERSION} ;\  
rm -f /etc/sphinx/example.sql \  
/etc/sphinx/sphinx-min.conf.dist \  
/etc/sphinx/sphinx.conf.dist  
  
EXPOSE 9312 9306 9307  
  
RUN set -xe ;\  
# Unpack s6-overlay  
apk add --no-cache --virtual .fetch-deps curl ;\  
S6_OVERLAY_VERSION="1.20.0.0" ;\  
S6_OVERLAY_SHA256="8827420ce1bcdb5f6219e3295c4b7cb46b7829ce0156ebc5310d782215bbcde1"
;\  
S6_OVERLAY_URL="https://github.com/just-
containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz" ;\  
S6_OVERLAY_TAR="/tmp/s6.tar.gz" ;\  
curl --retry 7 -Lsfo ${S6_OVERLAY_TAR} ${S6_OVERLAY_URL} ;\  
echo -n "${S6_OVERLAY_SHA256} ${S6_OVERLAY_TAR}" | sha256sum -c > /dev/null ;\  
tar xzf ${S6_OVERLAY_TAR} -C / ;\  
rm -f ${S6_OVERLAY_TAR} ;\  
mkdir -p /etc/{fix-attrs.d,cont-init.d,services.d,cont-finish.d} ;\  
apk del .fetch-deps  
  
RUN set -xe \  
\  
&& apk add --no-cache --virtual .build_deps curl \  
&& curl -sS -o /usr/bin/wait-for
https://raw.githubusercontent.com/eficode/wait-for/master/wait-for \  
&& chmod +x /usr/bin/wait-for \  
&& apk del .build_deps  
  
COPY rootfs /  
  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2  
  
CMD ["/init"]  

