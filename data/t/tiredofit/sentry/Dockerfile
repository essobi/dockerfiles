FROM tiredofit/debian:stretch  
LABEL maintainer="Dave Conroy (dave at tiredofit dot ca)"  
  
ENV SENTRY_VERSION=8.22.0 \  
SENTRY_CONF="/etc/sentry" \  
SENTRY_FILESTORE_DIR="/var/lib/sentry/files" \  
PIP_VERSION=10.0.1  
  
### Create Users and Groups  
RUN set -x ; \  
addgroup --gid 9000 sentry ; \  
adduser --uid 9000 --gid 9000 --home /dev/null --gecos "Sentry" --disabled-
password sentry ; \  
\  
### Add Depdencies  
apt-get update ; \  
apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
git \  
libffi-dev \  
libjpeg-dev \  
libldap2-dev \  
libpq-dev \  
libpython2.7 \  
libsasl2-dev \  
libxmlsec1-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
make \  
pkg-config \  
python \  
python-dev \  
wget \  
; \  
\  
## Install PIP  
wget -O /usr/src/pip.py "https://bootstrap.pypa.io/get-pip.py"; \  
python /usr/src/pip.py \  
\--disable-pip-version-check \  
\--no-cache-dir \  
pip==$PIP_VERSION \  
; \  
\  
### Install RabbitMQ Support  
pip install librabbitmq==1.6.1 ; \  
python -c 'import librabbitmq' ; \  
\  
### Download and Install Sentry  
mkdir -p /usr/src/sentry ; \  
wget -O /usr/src/sentry/sentry-${SENTRY_VERSION}-py27-none-any.whl
"https://github.com/getsentry/sentry/releases/download/${SENTRY_VERSION}/sentry-${SENTRY_VERSION}-py27-none-
any.whl" ; \  
wget -O /usr/src/sentry/sentry_plugins-${SENTRY_VERSION}-py2.py3-none-any.whl
"https://github.com/getsentry/sentry/releases/download/${SENTRY_VERSION}/sentry_plugins-${SENTRY_VERSION}-py2.py3-none-
any.whl" ; \  
pip install \  
/usr/src/sentry/sentry-${SENTRY_VERSION}-py27-none-any.whl \  
/usr/src/sentry/sentry_plugins-${SENTRY_VERSION}-py2.py3-none-any.whl \  
sentry-ldap-auth \  
https://github.com/getsentry/sentry-auth-saml2/archive/master.zip ; \  
sentry --help ; \  
sentry plugins list ; \  
\  
mkdir -p $SENTRY_CONF ; \  
mkdir -p $SENTRY_FILESTORE_DIR ; \  
\  
rm -r /usr/src/* ; \  
\  
### Cleanup  
apt-get purge -y --auto-remove \  
g++ \  
make \  
python-dev \  
wget \  
; \  
  
apt-get purge -y \  
cpp \  
cpp-6 \  
icu-devtools \  
libc-dev-bin \  
libc6-dev \  
libffi-dev \  
libgcc-6-dev \  
libgcrypt20-dev \  
libgmp-dev \  
libgnutls28-dev \  
libgpg-error-dev \  
libicu-dev \  
libidn11-dev \  
libjpeg-dev \  
libjpeg62-turbo-dev \  
libldap2-dev \  
libnspr4-dev \  
libnss3-dev \  
libp11-kit-dev \  
libpq-dev \  
libsasl2-dev \  
libssl-dev \  
libstdc++-6-dev \  
libtasn1-6-dev \  
libxml2-dev \  
libxmlsec1-dev \  
libxslt1-dev \  
; \  
\  
apt-get clean ; \  
rm -rf /var/lib/apt/lists /var/log/*  
  
### Networking Configuration  
EXPOSE 9000  
  
### Volume Configuration  
VOLUME /var/lib/sentry/files  
  
### Add files  
ADD install /  

