# Torchbox build of Python. This is based on the Torchbox uWSGI build;  
# the resulting image is suitable for running Python web applications.  
# Note that this includes a large number of packages to support building  
# common Python libraries.  
  
FROM torchbox/uwsgi:2.1  
  
ENV PYTHON_VERSION 3.4.5  
ENV PYTHON_PIP_VERSION 8.1.2  
ENV XMLSEC1_VERSION 1.2.22  
ENV LANG C.UTF-8  
  
RUN apk add --no-cache ca-certificates  
  
RUN set -ex \  
&& apk add --no-cache --virtual .python-builddeps \  
tar xz openssl bzip2-dev gcc libc-dev linux-headers \  
make ncurses-dev openssl openssl-dev readline-dev \  
sqlite-dev xz-dev zlib-dev wget pcre-dev \  
postgresql-client postgresql-dev postgresql \  
mariadb-client mariadb-dev \  
libxml2-dev libxslt-dev libpng-dev libjpeg-turbo-dev \  
tiff-dev rsync git openssh-client openssl-dev \  
curl wget openldap-dev libtool libltdl \  
&& mkdir -p /usr/src/python \  
&& cd /usr/src/python \  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-$PYTHON_VERSION.tar.xz"
\  
&& xz -dc python.tar.xz | tar xf - --strip-components=1 \  
&& ./configure --enable-shared --disable-static \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& wget -O /tmp/get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \  
&& /usr/local/bin/python3 /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION" \  
&& rm /tmp/get-pip.py \  
&& pip3 install --no-cache-dir --upgrade "pip==$PYTHON_PIP_VERSION" \  
&& cp -r /usr/src/uwsgi /usr/src/uwsgi-build \  
&& cd /usr/src/uwsgi-build/plugins \  
&& env PYTHON=/usr/local/bin/python3 uwsgi --build-plugin python \  
&& env PYTHON=/usr/local/bin/python3 uwsgi --build-plugin gevent \  
&& mkdir -p /usr/local/lib/uwsgi \  
&& cp *.so /usr/local/lib/uwsgi \  
&& cd /usr/src \  
&& wget http://www.aleksey.com/xmlsec/download/xmlsec1-$XMLSEC1_VERSION.tar.gz
\  
&& gzip -dc xmlsec1-$XMLSEC1_VERSION.tar.gz | tar xf - \  
&& cd xmlsec1-$XMLSEC1_VERSION \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf python.tar.xz \  
&& rm -rf /usr/src/python \  
&& rm -rf /usr/src/uwsgi-build \  
&& rm -rf /usr/src/xmlsec1-$XMLSEC1_VERSION \  
&& rm -rf /usr/src/xmlsec1-$XMLSEC1_VERSION.tar.gz \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .python-rundeps $runDeps \  
&& rm /usr/lib/libmysqld.a \  
&& rm -rf ~/.cache  
  
RUN cd /usr/local/bin \  
&& { [ -e easy_install ] || ln -s easy_install-* easy_install; } \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python3-config python-config  
  
CMD ["python3"]  

