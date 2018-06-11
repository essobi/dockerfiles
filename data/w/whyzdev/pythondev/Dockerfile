FROM whyzdev/pythondev:alpinebase  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION=9.0.1  
  
ENV LD_LIBRARY_PATH=/opt/python26/lib  
ENV GPG_KEY=A74B06BF  
ENV PYTHON_VERSION=2.6.9  
RUN set -ex \  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys "$GPG_KEY" \  
&& gpg \--batch \--verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python26 \  
&& tar -xJC /usr/src/python26 \--strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& sed -i -e 's/posix_close/posix_closex/g'
/usr/src/python26/Modules/posixmodule.c \  
\  
&& cd /usr/src/python26 \  
&& ./configure \  
\--prefix=/opt/python26 \  
\--enable-shared \  
\--enable-unicode=ucs4 \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
\  
&& wget -O /tmp/get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \  
&& /opt/python26/bin/python /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION" \  
&& rm /tmp/get-pip.py \  
# we use "--force-reinstall" for the case where the version of pip we're
trying to install is the same as the version bundled with Python  
# ("Requirement already up-to-date: pip==8.1.2 in {prefix}/lib/python3.6/site-
packages")  
# https://github.com/docker-library/python/pull/143#issuecomment-241032683  
&& /opt/python26/bin/pip install \--no-cache-dir \--upgrade \--force-reinstall
"pip==$PYTHON_PIP_VERSION" \  
# then we use "pip list" to ensure we don't have more than one pip version
installed  
# https://github.com/docker-library/python/pull/100  
&& [ "$(/opt/python26/bin/pip list |tac|tac| awk -F '[ ()]+' '$1 == "pip" {
print $2; exit }')" = "$PYTHON_PIP_VERSION" ] \  
\  
&& find /opt/python26 -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /opt/python26 \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add \--virtual .python-rundeps $runDeps \  
&& rm -rf /usr/src/python26 ~/.cache \  
&& echo .  
# && apk del .build-deps  
ENV LD_LIBRARY_PATH=/opt/python27/lib  
ENV GPG_KEY C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF  
ENV PYTHON_VERSION 2.7.13  
RUN set -ex \  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys "$GPG_KEY" \  
&& gpg \--batch \--verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python27 \  
&& tar -xJC /usr/src/python27 \--strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python27 \  
&& ./configure \  
\--prefix=/opt/python27 \  
\--enable-shared \  
\--enable-unicode=ucs4 \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
\  
&& wget -O /tmp/get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \  
&& /opt/python27/bin/python /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION" \  
&& rm /tmp/get-pip.py \  
# we use "--force-reinstall" for the case where the version of pip we're
trying to install is the same as the version bundled with Python  
# ("Requirement already up-to-date: pip==8.1.2 in {prefix}/lib/python3.6/site-
packages")  
# https://github.com/docker-library/python/pull/143#issuecomment-241032683  
&& /opt/python27/bin/pip install \--no-cache-dir \--upgrade \--force-reinstall
"pip==$PYTHON_PIP_VERSION" \  
# then we use "pip list" to ensure we don't have more than one pip version
installed  
# https://github.com/docker-library/python/pull/100  
&& [ "$(/opt/python27/bin/pip list |tac|tac| awk -F '[ ()]+' '$1 == "pip" {
print $2; exit }')" = "$PYTHON_PIP_VERSION" ] \  
\  
&& find /opt/python27 -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /opt/python27 \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add \--virtual .python-rundeps $runDeps \  
&& rm -rf /usr/src/python27 ~/.cache \  
&& echo .  
# && apk del .build-deps  
ENV LD_LIBRARY_PATH=/opt/python35/lib  
ENV GPG_KEY 97FC712E4C024BBEA48A61ED3A5CA953F73C700D  
ENV PYTHON_VERSION 3.5.2  
RUN set -ex \  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys "$GPG_KEY" \  
&& gpg \--batch \--verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python35 \  
&& tar -xJC /usr/src/python35 \--strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python35 \  
&& ./configure \  
\--prefix=/opt/python35 \  
\--enable-shared \  
\--enable-unicode=ucs4 \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
\  
&& wget -O /tmp/get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \  
&& /opt/python35/bin/python3 /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION" \  
&& rm /tmp/get-pip.py \  
# we use "--force-reinstall" for the case where the version of pip we're
trying to install is the same as the version bundled with Python  
# ("Requirement already up-to-date: pip==8.1.2 in {preifx}/lib/python3.6/site-
packages")  
# https://github.com/docker-library/python/pull/143#issuecomment-241032683  
&& /opt/python35/bin/pip install \--no-cache-dir \--upgrade \--force-reinstall
"pip==$PYTHON_PIP_VERSION" \  
# then we use "pip list" to ensure we don't have more than one pip version
installed  
# https://github.com/docker-library/python/pull/100  
&& [ "$(/opt/python35/bin/pip list |tac|tac| awk -F '[ ()]+' '$1 == "pip" {
print $2; exit }')" = "$PYTHON_PIP_VERSION" ] \  
\  
&& find /opt/python35 -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /opt/python35 \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add \--virtual .python-rundeps $runDeps \  
&& rm -rf /usr/src/python35 ~/.cache \  
&& echo .  
  
  
ENV LD_LIBRARY_PATH=/opt/python36/lib  
ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D  
ENV PYTHON_VERSION 3.6.0  
RUN set -ex \  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys "$GPG_KEY" \  
&& gpg \--batch \--verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python36 \  
&& tar -xJC /usr/src/python36 \--strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python36 \  
&& ./configure \  
\--prefix=/opt/python36 \  
\--enable-shared \  
\--enable-unicode=ucs4 \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
\  
&& wget -O /tmp/get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \  
&& /opt/python36/bin/python3 /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION" \  
&& rm /tmp/get-pip.py \  
# we use "--force-reinstall" for the case where the version of pip we're
trying to install is the same as the version bundled with Python  
# ("Requirement already up-to-date: pip==8.1.2 in {prefix}/lib/python3.6/site-
packages")  
# https://github.com/docker-library/python/pull/143#issuecomment-241032683  
&& /opt/python36/bin/python3 -m pip install \--no-cache-dir \--upgrade
\--force-reinstall "pip==$PYTHON_PIP_VERSION" \  
# then we use "pip list" to ensure we don't have more than one pip version
installed  
# https://github.com/docker-library/python/pull/100  
&& [ "$(/opt/python36/bin/pip list |tac|tac| awk -F '[ ()]+' '$1 == "pip" {
print $2; exit }')" = "$PYTHON_PIP_VERSION" ] \  
\  
&& find /opt/python36 -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /opt/python36 \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add \--virtual .python-rundeps $runDeps \  
&& rm -rf /usr/src/python36 ~/.cache \  
&& echo .  
  
#other dependency for building/running python package such as lxml  
RUN apk add \--no-cache libxml2-dev libxslt-dev  
  
ENV LD_LIBRARY_PATH=""  
ENV GPG_KEY=""  
ENV PYTHON_VERSION=""  
CMD ["/bin/sh"]  

