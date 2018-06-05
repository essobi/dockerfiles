FROM alpine:3.7  
# ensure local python is preferred over distribution python  
ENV PATH /usr/local/bin:$PATH  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# install ca-certificates so that HTTPS works consistently  
# the other runtime dependencies for Python are installed later  
RUN apk add --no-cache ca-certificates  
  
ENV GPG_KEY C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF  
ENV PYTHON_VERSION 2.7.14  
  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps \  
gnupg \  
libressl \  
tar \  
xz \  
\  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& apk add --no-cache --virtual .build-deps \  
bzip2-dev \  
coreutils \  
dpkg-dev dpkg \  
gcc \  
gdbm-dev \  
libc-dev \  
linux-headers \  
make \  
ncurses-dev \  
libressl \  
libressl-dev \  
pax-utils \  
readline-dev \  
sqlite-dev \  
tcl-dev \  
tk \  
tk-dev \  
zlib-dev \  
# add build deps before removing fetch deps in case there's overlap  
&& apk del .fetch-deps \  
\  
&& cd /usr/src/python \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--enable-shared \  
\--enable-unicode=ucs4 \  
&& make -j "$(nproc)" \  
# set thread stack size to 1MB so we don't segfault before we hit
sys.getrecursionlimit()  
#
https://github.com/alpinelinux/aports/commit/2026e1259422d4e0cf92391ca2d3844356c649d0  
EXTRA_CFLAGS="-DTHREAD_STACK_SIZE=0x100000" \  
&& make install \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
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
  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 9.0.3  
  
RUN set -ex; \  
\  
apk add --no-cache --virtual .fetch-deps libressl; \  
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
  
RUN set -ex; \  
\  
mkdir -p \opt; \  
\  
cd /opt; \  
\  
wget https://download.jetbrains.com/python/pycharm-professional-2018.1.tar.gz;
\  
\  
tar xf pycharm*.tar.gz ; \  
\  
rm -rf pycharm*.tar.gz  
  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ENV JAVA_VERSION 8u111  
ENV JAVA_ALPINE_VERSION 8.151.12-r0  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8-jre="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
  
ENTRYPOINT [ "/opt/pycharm-2018.1/bin/pycharm.sh" ]  

