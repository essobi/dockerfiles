FROM yellowblackandwhite/alpine-base  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
  
USER root  
COPY requirements.txt /tmp/  
  
RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
apk add --update build-base python3-dev gmp-dev musl git curl perl libgcc
libbz2 \  
libffi libgcrypt ncurses5-libs libc6-compat gfortran openblas openblas-dev \  
\--update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/
--allow-untrusted  
  
RUN ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.23-r3" && \  
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \  
wget "https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
-O "/etc/apk/keys/sgerrand.rsa.pub" && \  
wget
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
&& \  
apk add --no-cache "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
apk del glibc-i18n && \  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
ENV PYTHONIOENCODING 'utf8'  
ENV LANG=C.UTF-8  
ENV PYPY pypy3-2.4-linux_x86_64-portable  
ADD https://bitbucket.org/squeaky/portable-pypy/downloads/${PYPY}.tar.bz2
/tmp/${PYPY}.tar.bz2  
ADD https://bootstrap.pypa.io/get-pip.py /tmp/get-pip.py  
RUN cd /tmp/ && \  
tar -xjf ${PYPY}.tar.bz2 && \  
cp -rp ${PYPY} /usr/lib/pypy && \  
ldd /usr/lib/pypy/bin/pypy && \  
ln -s /usr/lib/pypy/bin/pypy /usr/local/bin/pypy && \  
ln -s /usr/lib/pypy/bin/pypy /usr/local/bin/pypy3 && \  
ln -s /usr/lib/pypy/bin/pypy /usr/local/bin/python && \  
ln -s /usr/lib/pypy/bin/pypy /usr/local/bin/python3 && \  
pypy3 get-pip.py && \  
ln -s /usr/lib/pypy/bin/pip /usr/local/bin/pip && \  
ln -s /usr/lib/pypy/bin/pip /usr/local/bin/pip3 && \  
ln -s -f /usr/lib/libncurses.so.5.9 /usr/lib/libtinfo.so.5 && \  
ln -s -f /usr/lib/libbz2.so.1 /usr/lib/libbz2.so.1.0 && \  
ln -s -f /usr/lib/libgcrypt.so.20 /usr/lib/libcrypt.so.1 && \  
# pypy3 -m pip install git+https://bitbucket.org/pypy/numpy.git && \  
rm get-pip.py && \  
rm -rf /tmp/${PYPY}.tar.bz2 && \  
rm -rf /tmp/${PYPY}  
  
RUN pip3 install --upgrade pip && \  
pip3 install --upgrade -r /tmp/requirements.txt && \  
apk del build-base python3-dev gmp-dev openblas-dev gfortran && \  
rm -rf /root/.cache/pip/* && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
COPY pip_entry_point.sh /  
ENTRYPOINT ["/pip_entry_point.sh"]  
  
USER alpine  

