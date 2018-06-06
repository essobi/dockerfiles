FROM codeworksio/ubuntu:18.04-20180210  
# SEE: https://github.com/docker-
library/python/blob/master/3.6/stretch/Dockerfile  
ARG APT_PROXY  
ARG APT_PROXY_SSL  
ENV PYTHON_VERSION="3.6.4" \  
PYTHON_DOWNLOAD_URL="https://www.python.org/ftp/python" \  
PYTHON_GPG_KEY="0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D" \  
PYTHON_PIP_VERSION="9.0.1" \  
PYTHON_PIP_DOWNLOAD_URL="https://bootstrap.pypa.io/get-pip.py"  
RUN set -ex; \  
\  
buildDependencies="\  
gcc \  
libssl-dev \  
tcl-dev \  
tk-dev \  
"; \  
if [ -n "$APT_PROXY" ]; then echo "Acquire::http { Proxy
\"http://${APT_PROXY}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
if [ -n "$APT_PROXY_SSL" ]; then echo "Acquire::https { Proxy
\"https://${APT_PROXY_SSL}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
apt-get --yes update; \  
apt-get --yes install \  
$buildDependencies \  
; \  
curl -L
"$PYTHON_DOWNLOAD_URL/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz; \  
curl -L
"$PYTHON_DOWNLOAD_URL/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys
$PYTHON_GPG_KEY; \  
gpg --batch --verify python.tar.xz.asc python.tar.xz; \  
rm -rf $GNUPGHOME python.tar.xz.asc; \  
mkdir -p /usr/src/python; \  
tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz; \  
rm python.tar.xz; \  
cd /usr/src/python; \  
./configure \  
\--enable-loadable-sqlite-extensions \  
\--enable-shared \  
\--without-ensurepip; \  
make -j$(nproc); \  
make install; \  
ldconfig; \  
ln -s /usr/local/bin/idle3 /usr/local/bin/idle; \  
ln -s /usr/local/bin/pydoc3 /usr/local/bin/pydoc; \  
ln -s /usr/local/bin/python3 /usr/local/bin/python; \  
ln -s /usr/local/bin/python3-config /usr/local/bin/python-config; \  
\  
curl -L "$PYTHON_PIP_DOWNLOAD_URL" -o /tmp/get-pip.py; \  
python /tmp/get-pip.py \  
\--disable-pip-version-check \  
\--no-cache-dir \  
"pip==$PYTHON_PIP_VERSION" \  
; \  
rm /tmp/get-pip.py; \  
find /usr/local -depth \\( \\( -type d -a -name test -o -name tests \\) -o \\(
-type f -a -name '*.pyc' -o -name '*.pyo' \\) \\) -exec rm -rf '{}' +; \  
rm -rf /usr/src/python; \  
apt-get purge --yes --auto-remove $buildDependencies; \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apt/*; \  
rm -f /etc/apt/apt.conf.d/00proxy  
  
### METADATA
###################################################################  
ARG IMAGE  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
ARG VCS_URL  
LABEL \  
org.label-schema.name=$IMAGE \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.schema-version="1.0"  

