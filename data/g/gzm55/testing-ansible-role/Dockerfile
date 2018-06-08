## Builder stage for copying docker cli  
FROM docker:18.01 as docker-cli  
  
RUN mkdir -p "/output$(dirname -- $(which docker))"  
RUN mkdir -p "/output$(dirname -- $(which modprobe))"  
RUN cp -- "$(which docker)" "/output$(dirname -- $(which docker))"/  
RUN cp -- "$(which modprobe)" "/output$(dirname -- $(which modprobe))"/  
  
## Main image  
FROM alpine:3.7  
## http://bugs.python.org/issue19846  
## > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
  
LABEL maintainer="James Z.M. Gao (@gzm55)" \  
readme.md="https://github.com/gzm55/docker-testing-ansible-
role/blob/master/README.md" \  
description="Docker image for testing ansible roles"  
  
COPY --from=docker-cli /output /  
## Contents  
## - config offline pip package location: /usr/local/share/pip-wheelhouse  
## - config offline easy_install package location: /usr/local/share/pip-
wheelhouse  
## - make sure /usr/local/share/pip-wheelhouse exists  
## - patches for compile python 2.6  
## - ssh pubkeys for public code host services  
ADD content /  
  
## Overrall building steps:  
## - init system  
## - fetch source for py2.6 and py 3.5  
## - install py2.7, py3.6, py2.6, py3.5  
## - install pip2.7, pip3.6, pip2.6, pip3.5  
## - pip install/wheel packages for ansible, tox, molecule  
## - cleanup  
## TODO Test cases:  
## - common molecule test cases  
## - common tox test cases  
  
RUN set -ux \  
###  
## 0. Update alpine system  
## - Apply alpine security updates  
## - Install ca-certificates so that HTTPS works consistently  
## the other runtime dependencies for Python are installed later,  
## ansible and git also depends on this package.  
&& apk upgrade --update-cache --no-progress \  
&& apk add --no-progress ca-certificates \  
###  
## 1. Fetch files for python 2.6 and 3.5  
&& apk add --no-progress --virtual .fetch-deps \  
openssl \  
gnupg \  
tar \  
xz \  
## for developping convenient, we may pre-download the python source and
signature to content/ dir  
&& { [ -f python-2.6.tar.xz ] \  
|| wget -O python-2.6.tar.xz
'https://www.python.org/ftp/python/2.6.9/Python-2.6.9.tar.xz'; \  
} \  
&& { [ -f python-2.6.tar.xz.asc ] \  
|| wget -O python-2.6.tar.xz.asc
'https://www.python.org/ftp/python/2.6.9/Python-2.6.9.tar.xz.asc'; \  
} \  
&& { [ -f python-3.5.tar.xz ] \  
|| wget -O python-3.5.tar.xz
'https://www.python.org/ftp/python/3.5.5/Python-3.5.5.tar.xz'; \  
} \  
&& { [ -f python-3.5.tar.xz.asc ] \  
|| wget -O python-3.5.tar.xz.asc
'https://www.python.org/ftp/python/3.5.5/Python-3.5.5.tar.xz.asc'; \  
} \  
&& wget -O get-pip.py "https://bootstrap.pypa.io/get-pip.py" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& : for 2.6 && gpg --keyserver keyserver.ubuntu.com --recv-keys
'8417157EDBE73D9EAC1E539B126EB563A74B06BF' \  
&& : for 3.5 && gpg --keyserver keyserver.ubuntu.com --recv-keys
'97FC712E4C024BBEA48A61ED3A5CA953F73C700D' \  
&& gpg --batch --verify python-2.6.tar.xz.asc python-2.6.tar.xz \  
&& gpg --batch --verify python-3.5.tar.xz.asc python-3.5.tar.xz \  
&& rm -rf "$GNUPGHOME" python*.tar.xz.asc \  
&& unset GNUPGHOME \  
&& mkdir -p /usr/src/python-2.6 /usr/src/python-3.5 \  
&& tar -xJC /usr/src/python-2.6 \--strip-components=1 -f python-2.6.tar.xz \  
&& tar -xJC /usr/src/python-3.5 \--strip-components=1 -f python-3.5.tar.xz \  
&& rm python*.tar.xz \  
####  
## 2. Compile python 2.6 from source  
## - ref: https://cwill.us/compiling-python2-6-for-alpine-linux-in-docker/  
## - also install python-dev-2.6 headers  
&& apk add --no-progress --virtual .build-deps-py2.6 \  
gcc \  
libc-dev \  
linux-headers \  
make \  
openssl \  
readline-dev \  
tcl-dev \  
tk \  
tk-dev \  
expat-dev \  
openssl-dev \  
zlib-dev \  
ncurses-dev \  
bzip2-dev \  
gdbm-dev \  
sqlite-dev \  
libffi-dev \  
&& apk del .fetch-deps \  
&& cd /usr/src/python-2.6 \  
&& patch -p1 < python-2.6-internal-expat.patch \  
&& patch -p1 < python-2.6-posix-module.patch \  
&& ./configure --enable-shared \  
\--with-threads \  
\--with-system-ffi \  
\--enable-unicode=ucs4 \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& cd / \  
&& rm /usr/local/bin/python /usr/local/bin/smtpd.py \  
&& mv /usr/local/bin/2to3 /usr/local/bin/2to3-2.6 \  
&& mv /usr/local/bin/idle /usr/local/bin/idle2.6 \  
&& mv /usr/local/bin/pydoc /usr/local/bin/pydoc2.6 \  
####  
## 3. Compile python 3.5 from source  
&& apk add --no-progress --virtual .build-deps-py3.5 \  
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
&& apk del .build-deps-py2.6 \  
&& cd /usr/src/python-3.5 \  
&& ./configure --build="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
\--enable-loadable-sqlite-extensions \  
\--enable-shared \  
\--with-system-expat \  
\--with-system-ffi \  
\--without-ensurepip \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& cd / \  
&& rm /usr/local/bin/2to3 \  
/usr/local/bin/idle3 \  
/usr/local/bin/pydoc3 \  
/usr/local/bin/python3 \  
/usr/local/bin/pyvenv \  
/usr/local/share/man/man1/python* \  
####  
## 4. Pin runtime dependends of python 2.6 and 3.5  
&& rm -rf /usr/src \  
&& scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
| xargs -r apk add --virtual .python-rundeps \  
####  
## 5. Install python 2.7(default) and 3.6  
&& apk add --no-progress python3 \  
&& apk add --no-progress python2 \  
####  
## 6. Install and update pip 2.6, 2.7, 3,5, 3,6  
## - install apk packages last, this can fix the default link of pip, pip2,
pip3  
## - wheel 0.30 removed support for 2.6  
## ref:
https://github.com/pypa/wheel/blob/7ca7b3552e55030b5d78cd90d53f1d99c9139f16/CHANGES.txt#L15  
## - setuptools 37.0 removed support for 2.6  
## ref: https://setuptools.readthedocs.io/en/latest/history.html#v37-0-0  
## - we use "--force-reinstall" for the case where the version of  
## pip we're trying to install is the same as the version bundled  
## with Python ("Requirement already up-to-date: pip==8.1.2 in  
## /usr/local/lib/python3.6/site-packages")  
## ref: https://github.com/docker-
library/python/pull/143#issuecomment-241032683  
## - pip2.6 will remove pip3.5, so update it first  
&& mkdir -p /usr/local/share/pip-wheelhouse \  
&& python2.6 get-pip.py --disable-pip-version-check --no-wheel --no-setuptools
'pip==9.0.1' \  
&& pip2.6 install --no-cache-dir --upgrade --force-reinstall pip
'setuptools<37dev' 'wheel<0.30' \  
&& python3.5 get-pip.py --disable-pip-version-check --no-wheel 'pip==9.0.1' \  
&& apk add --no-progress py3-pip py2-pip \  
&& pip3.5 install --no-cache-dir --upgrade --force-reinstall pip wheel \  
&& pip3.6 install --no-cache-dir --upgrade --force-reinstall pip wheel \  
&& pip2.7 install --no-cache-dir --upgrade --force-reinstall pip wheel \  
&& rm /usr/local/bin/easy_install \  
/usr/local/bin/pip \  
/usr/local/bin/pip2 \  
/usr/local/bin/pip3 \  
/usr/local/bin/wheel \  
/get-pip.py \  
####  
## 7. In python 2.7 environment  
## - wheel and install ansible: latest, 2.4, 2.3, 2.2  
## - wheel and install molecule 2.*  
## - wheel and install passlib>=1.6, for crypt/hash password in ansible  
## - wheel and install pexpect>=3.3, for ansible expect module  
## - wheel and install docker-py  
## - install tox 2.*  
## - molecule 2.* now only support python 2.7, but in most case it supports
py{2.6,3.5,3.6}  
&& apk add --no-progress --virtual .build-deps-pip2.7 \  
linux-headers \  
gcc \  
make \  
file \  
musl-dev \  
libffi-dev \  
openssl-dev \  
python2-dev \  
&& apk del .build-deps-py3.5 \  
&& pip2.7 wheel 'ansible' \  
&& pip2.7 wheel 'ansible>=2.4,<2.5' \  
&& pip2.7 wheel 'ansible>=2.3,<2.4' \  
&& pip2.7 wheel 'ansible>=2.2,<2.3' \  
&& pip2.7 wheel 'molecule>=2,<3' 'docker-py' \  
&& pip2.7 wheel 'passlib>=1.6' 'pexpect>=3.3' \  
&& pip2.7 install --no-index 'molecule>=2,<3' \  
'passlib>=1.6' \  
'pexpect>=3.3' \  
'docker-py' \  
&& pip2.7 install 'tox>=2,<3' \  
####  
## 8. In python 3.6 environment  
## - wheel ansible: 2.4, 2.3, 2.2  
## - wheel molecule 2.*  
## - wheel passlib>=1.6  
## - wheel pexpect>=3.3  
## - wheel docker-py  
&& apk add --no-progress --virtual .build-deps-pip3.6 \  
linux-headers \  
gcc \  
make \  
musl-dev \  
libffi-dev \  
openssl-dev \  
python3-dev \  
&& apk del .build-deps-pip2.7 \  
&& pip3.6 wheel 'ansible>=2.2' \  
&& pip3.6 wheel 'ansible>=2.4,<2.5' \  
&& pip3.6 wheel 'ansible>=2.3,<2.4' \  
&& pip3.6 wheel 'ansible>=2.2,<2.3' \  
&& pip3.6 wheel 'molecule>=2,<3' 'docker-py' \  
&& pip3.6 wheel 'passlib>=1.6' 'pexpect>=3.3' \  
####  
## 9. In python 2.6 environment  
## - wheel ansible: 2.4, 2.3, 2.2 (limit setuptools<37)  
## - wheel molecule 2.* (limit setuptools<37, pytest<3.3, py<1.5)  
## - wheel passlib>=1.6  
## - wheel pexpect>=3.3  
## - wheel docker-py  
##  
## Note: py 1.5 drops support of python 2.6  
&& apk add --no-progress --virtual .build-deps-pip2.6 \  
linux-headers \  
gcc \  
make \  
musl-dev \  
openssl-dev \  
libffi-dev \  
&& apk del .build-deps-pip3.6 \  
&& pip2.6 wheel 'setuptools<37dev' 'ansible' \  
&& pip2.6 wheel 'setuptools<37dev' 'ansible>=2.4,<2.5' \  
&& pip2.6 wheel 'setuptools<37dev' 'ansible>=2.3,<2.4' \  
&& pip2.6 wheel 'setuptools<37dev' 'ansible>=2.2,<2.3' \  
&& pip2.6 wheel 'setuptools<37dev' 'pytest<3.3.0' 'py<1.5' 'molecule>=2,<3'
'docker-py' \  
&& pip2.6 wheel 'passlib>=1.6' 'pexpect>=3.3' \  
&& find /usr/local/include/python2.6/ -depth \  
\\( ! -type f -o ! -name 'pyconfig.h' \\) \  
-delete \  
&& find /usr/local/bin/ -depth \  
\\( \\( -type f -o -type l \\) -a \\( -name 'python2*-config' -o -name
'python-config' \\) \\) \  
-delete \  
####  
## 10. In python 3.5 environment  
## - wheel ansible: 2.4, 2.3, 2.2  
## - wheel molecule 2.*  
## - wheel passlib>=1.6  
## - wheel pexpect>=3.3  
## - wheel docker-py  
&& apk add --no-progress --virtual .build-deps-pip3.5 \  
linux-headers \  
gcc \  
make \  
musl-dev \  
openssl-dev \  
libffi-dev \  
&& apk del .build-deps-pip2.6 \  
&& pip3.5 wheel 'ansible>=2.2' \  
&& pip3.5 wheel 'ansible>=2.4,<2.5' \  
&& pip3.5 wheel 'ansible>=2.3,<2.4' \  
&& pip3.5 wheel 'ansible>=2.2,<2.3' \  
&& pip3.5 wheel 'molecule>=2,<3' 'docker-py' \  
&& pip3.5 wheel 'passlib>=1.6' 'pexpect>=3.3' \  
&& find /usr/local/include/python3.5m/ -depth \  
\\( ! -type f -o ! -name 'pyconfig.h' \\) \  
-delete \  
&& find /usr/local/bin/ -depth \  
\\( \\( -type f -o -type l \\) -a -name 'python3*-config' \\) \  
-delete \  
####  
## 11. Install ansible runtime deps  
&& apk add --no-progress openssh-client \  
sshpass \  
git \  
&& apk del .build-deps-pip3.5 \  
####  
## 12. Cleanup  
## - remove python compiled files  
## - remove python module tests, but keep ansible `test' plugin  
## - remove system caches  
&& find /usr/ -depth \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
-delete \  
&& find /usr/ -depth \  
\\( ! -path '*/ansible/*' \  
-a \  
\\( -type d -a -name test -o -name tests \\) \  
\\) \  
-exec rm -rf '{}' \+ \  
&& rm -rf ~/.cache ~/.ash_history /var/cache/apk/* \  
####  
## Done  
;  

