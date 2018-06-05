FROM ruby:2.4-alpine  
  
  
################################################################  
########################## Enviroment ##########################  
################################################################  
############################ Python ############################  
# ensure local python is preferred over distribution python  
ENV PATH /usr/local/bin:$PATH  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# install ca-certificates so that HTTPS works consistently  
# the other runtime dependencies for Python are installed later  
RUN apk add --no-cache ca-certificates  
  
ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D  
ENV PYTHON_VERSION 3.6.2  
  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps \  
gnupg \  
openssl \  
tar \  
xz \  
\  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -rf "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& apk add --no-cache --virtual .build-deps \  
bzip2-dev \  
coreutils \  
dpkg-dev dpkg \  
expat-dev \  
gcc \  
gdbm-dev \  
libc-dev \  
libffi-dev \  
linux-headers \  
make \  
ncurses-dev \  
openssl \  
openssl-dev \  
pax-utils \  
readline-dev \  
sqlite-dev \  
tcl-dev \  
tk \  
tk-dev \  
xz-dev \  
zlib-dev \  
# add build deps before removing fetch deps in case there's overlap  
&& apk del .fetch-deps \  
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
\  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .python-rundeps $runDeps \  
&& apk del .build-deps \  
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
ENV PYTHON_PIP_VERSION 9.0.1  
  
RUN set -ex; \  
\  
apk add --no-cache --virtual .fetch-deps openssl; \  
\  
wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \  
\  
apk del .fetch-deps; \  
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
  
  
############################# Java #############################  
# A few problems with compiling Java from source:  
# 1. Oracle. Licensing prevents us from redistributing the official JDK.  
# 2. Compiling OpenJDK also requires the JDK to be installed, and it gets  
# really hairy.  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ENV JAVA_VERSION 8u111  
ENV JAVA_ALPINE_VERSION 8.111.14-r0  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
  
################################################################  
######################## Analysis Tools ########################  
################################################################  
########################### FindBugs ###########################  
  
ENV FINDBUGS_VERSION=3.0.1  
  
WORKDIR /usr/workdir  
RUN apk add --update \  
curl \  
&& rm -rf /var/cache/apk/*  
  
  
# Download the latest findbugs release  
RUN curl -sL \  
https://sourceforge.net/projects/findbugs/files/findbugs/${FINDBUGS_VERSION}/findbugs-${FINDBUGS_VERSION}.tar.gz/download
| \  
tar -xz && \  
mv findbugs-* /usr/bin/findbugs  
  
  
############################# PMD ##############################  
  
ENV PMD_VERSION=5.8.1  
  
# Download the latest pmd release  
RUN curl -sLO \  
https://github.com/pmd/pmd/releases/download/pmd_releases%2F${PMD_VERSION}/pmd-
bin-${PMD_VERSION}.zip && \  
unzip pmd-bin-*.zip && \  
rm pmd-bin-*.zip && \  
mv pmd-bin-* /usr/bin/pmd-bin  
  
  
########################## CheckStyle ##########################  
  
ENV CHECKSTYLE_VERSION=7.6.1  
  
  
# Download the latest checkstyle release  
RUN curl -sLO \  
https://sourceforge.net/projects/checkstyle/files/checkstyle/${CHECKSTYLE_VERSION}/checkstyle-${CHECKSTYLE_VERSION}-all.jar
&& \  
mv checkstyle-*.jar /usr/bin/checkstyle.jar  
  
  
########################### Brakeman ###########################  
  
ENV BRAKEMAN_VERSION=3.6.1  
  
RUN gem install brakeman --version ${BRAKEMAN_VERSION} --no-format-exec  
  
  
############################ JShint ############################  
  
RUN apk add --no-cache bash nodejs && \  
apk add --no-cache bash git openssh && \  
npm install -g bower && \  
npm install -g jshint && \  
npm install -g jshint-html-reporter --save  
  
  
  
########################### Retirejs ###########################  
  
RUN npm install -g retire  
  
  
  
############################ Bandit ############################  
#===================  
# Bandit User same id as jenkins  
#===================  
ARG user=bandit  
ARG group=bandit  
ARG uid=1000  
ARG gid=1001  
RUN addgroup -g ${gid} ${group} && \  
adduser -u ${uid} -G ${group} -D -s /bin/bash ${user}  
  
#===================  
# Bandit  
#===================  
RUN pip install bandit  
  
USER $user  
  
  
  
WORKDIR /workdir  

