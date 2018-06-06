FROM dabaopku/docker:Base  
  
ENV PATH /usr/local/bin:$PATH  
ENV LANG C.UTF-8  
ENV PYTHONIOENCODING UTF-8  
ENV PYTHON_VERSION 2.7.15  
  
COPY ./data /data  
  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps \  
tar \  
xz \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f /data/Python-2.7.15.tar.xz
\  
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
&& cd /usr/src/python \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--enable-shared \  
\--enable-unicode=ucs4 \  
&& make -j "$(nproc)" \  
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
&& find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' \+ \  
&& python /data/get-pip.py \  
\--disable-pip-version-check \  
\--no-cache-dir \  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' \+ \  
&& rm -rf /data \  
&& rm -rf /usr/src/python \  
&& apk del .fetch-deps \  
&& apk del .build-deps \  
&& apk del .python-rundeps  
  
CMD ["sh", "-l"]

