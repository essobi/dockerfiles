# VERSION 1.0.1  
# AUTHOR: Bodastage Solutions  
# DESCRIPTION: BTS-CE Mediation Server  
# BUILD: docker build --rm -t bodastage/bts-ce-mediation .  
# SOURCE: https://github.com/bodastage/boda-ce-mediation  
#  
# Installs: Python3, jre8 from OpenJDK, zip, unzip, git, airflow,procps, 7zip
and urar  
#  
# Compiled from:  
# https://github.com/docker-library/python/3.6/stretch/slim/Dockerfile  
# https://github.com/docker-library/openjdk/8-jdk/slim/Dockerfile  
# https://github.com/puckel/docker-airflow/Dockerfile  
#  
  
FROM debian:stretch-slim  
  
LABEL maintainer Bodastage Engineering<engineering@bodastage.com>  
  
# Python3  
# ########################################################################  
# ensure local python is preferred over distribution python  
ENV PATH /usr/local/bin:$PATH  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# runtime dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
libexpat1 \  
libffi6 \  
libgdbm3 \  
libreadline7 \  
libsqlite3-0 \  
libssl1.1 \  
netcat \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D  
ENV PYTHON_VERSION 3.6.5  
  
RUN set -ex \  
&& buildDeps=" \  
dpkg-dev \  
gcc \  
libbz2-dev \  
libc6-dev \  
libexpat1-dev \  
libffi-dev \  
libgdbm-dev \  
liblzma-dev \  
libncursesw5-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
make \  
tcl-dev \  
tk-dev \  
wget \  
xz-utils \  
zlib1g-dev \  
# as of Stretch, "gpg" is no longer included by default  
$(command -v gpg > /dev/null || echo 'gnupg dirmngr') \  
" \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& for server in ha.pool.sks-keyservers.net \  
hkp://p80.pool.sks-keyservers.net:80 \  
keyserver.ubuntu.com \  
hkp://keyserver.ubuntu.com:80 \  
pgp.mit.edu; do \  
gpg --keyserver "$server" \--recv-keys "$GPG_KEY" && break || echo "Trying new
server..."; \  
done \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -rf "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--enable-loadable-sqlite-extensions \  
\--enable-shared \  
\--with-system-expat \  
\--with-system-ffi \  
\--without-ensurepip \  
&& make -j "$(nproc)" \  
&& make install \  
&& ldconfig \  
\  
&& apt-get purge -y --auto-remove $buildDeps \  
\  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python  
  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python3-config python-config  
  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 9.0.3  
  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends wget; \  
rm -rf /var/lib/apt/lists/*; \  
\  
wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \  
\  
apt-get purge -y --auto-remove wget; \  
\  
python get-pip.py \  
\--disable-pip-version-check \  
\--no-cache-dir \  
"pip==$PYTHON_PIP_VERSION" \  
; \  
pip --version; \  
\  
find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' +; \  
rm -f get-pip.py  
  
# CMD ["python3"]  
# zip, unzip, wget,gnupg, file and other useful utilities  
# ########################################################################  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
zip \  
unzip \  
xz-utils \  
wget \  
gnupg \  
file \  
procps \  
p7zip-full \  
unrar-free \  
&& rm -rf /var/lib/apt/lists/*  
  
# Potgresclient  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main 10" >
/etc/apt/sources.list.d/pgdg.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add - \  
&& apt-get update \  
&& apt-get install --allow-unauthenticated --no-install-recommends --no-
upgrade -y postgresql-client-10;  
  
# JRE8  
# ########################################################################  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
# do some fancy footwork to create a JAVA_HOME that's cross-architecture-safe  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
# do some fancy footwork to create a JAVA_HOME that's cross-architecture-safe  
RUN ln -svT "/usr/lib/jvm/java-8-openjdk-$(dpkg --print-architecture)"
/docker-java-home  
ENV JAVA_HOME /docker-java-home  
  
ENV JAVA_VERSION 8u171  
ENV JAVA_DEBIAN_VERSION 8u171-b11-1~deb9u1  
  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20170531+nmu1  
  
RUN set -ex; \  
\  
# deal with slim variants not having man page directories (which causes
"update-alternatives" to fail)  
if [ ! -d /usr/share/man/man1 ]; then \  
mkdir -p /usr/share/man/man1; \  
fi; \  
\  
apt-get update; \  
apt-get install -y \  
openjdk-8-jdk-headless="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
# verify that "docker-java-home" returns what we expect  
[ "$(readlink -f "$JAVA_HOME")" = "$(docker-java-home)" ]; \  
\  
# update-alternatives so that future installs of other OpenJDK versions don't
change /usr/bin/java  
update-alternatives --get-selections | awk -v home="$(readlink -f
"$JAVA_HOME")" 'index($3, home) == 1 { $2 = "manual"; print | "update-
alternatives --set-selections" }'; \  
# ... and verify that it actually worked for one of the alternatives we care
about  
update-alternatives --query java | grep -q 'Status: manual'  
  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
# Airflow  
# ###########################################  
  
ARG AIRFLOW_VERSION=1.9.0  
ARG AIRFLOW_HOME=/usr/local/airflow  
  
# Define en_US.  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_MESSAGES en_US.UTF-8  
  
RUN set -ex \  
&& buildDeps=' \  
python3-dev \  
libkrb5-dev \  
libsasl2-dev \  
libssl-dev \  
libffi-dev \  
build-essential \  
libblas-dev \  
liblapack-dev \  
libpq-dev \  
git \  
' \  
&& apt-get update -yqq \  
&& apt-get upgrade -yqq \  
&& apt-get install -yqq --no-install-recommends \  
$buildDeps \  
python3-pip \  
python3-requests \  
apt-utils \  
curl \  
rsync \  
netcat \  
locales \  
&& sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \  
&& useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \  
&& pip install -U pip setuptools wheel \  
&& pip install Cython \  
&& pip install pytz \  
&& pip install pyOpenSSL \  
&& pip install ndg-httpsclient \  
&& pip install pyasn1 \  
&& pip install pika \  
&& pip install apache-
airflow[crypto,celery,postgres,hive,jdbc]==$AIRFLOW_VERSION \  
&& pip install celery[redis]==4.0.2 \  
&& apt-get purge --auto-remove -yqq $buildDeps \  
&& apt-get autoremove -yqq --purge \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
COPY script/entrypoint.sh /entrypoint.sh  
RUN chmod 777 /entrypoint.sh  
  
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg  
RUN chown -R airflow: ${AIRFLOW_HOME}  
  
EXPOSE 8080 5555 8793  
  
USER airflow  
  
WORKDIR ${AIRFLOW_HOME}  
  
ENTRYPOINT ["/entrypoint.sh"]  

