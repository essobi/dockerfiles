FROM sgn0/uwsgi  
MAINTAINER Jesus Lopez, jesus@sgn.com  
  
COPY requirements.txt /  
RUN set -ex; \  
sed -i -e 's/.*community//g' /etc/apk/repositories; \  
apk add \--no-cache -q libstdc++; \  
apk add \--no-cache -qt .buildDeps \  
py-pip \  
python-dev \  
g++ \  
musl-dev \  
openssl \  
openssl-dev \  
libffi-dev \  
perl \  
cmake \  
make \  
; \  
mkdir /usr/src; \  
wget -qO- https://github.com/couchbase/libcouchbase/archive/2.6.1.tar.gz |tar
xzf - -C /usr/src; \  
cd /usr/src/libcouchbase-2.6.1; \  
mkdir build; \  
cd build; \  
../cmake/configure \--prefix=/usr \--disable-tools \--disable-tests
\--disable-plugins \--disable-cxx \--disable-couchbasemock; \  
make -j8 install; \  
strip /usr/lib/libcouchbase.so.2.0.36; \  
pip install -qr /requirements.txt; \  
rm /requirements.txt; \  
apk del \--no-cache -q .buildDeps; \  
find /usr/bin /usr/lib/python2.7 -name '*.py[co]' -print0 |xargs -0 rm; \  
rm -fr /root/.cache /usr/src /usr/share/man /usr/lib/pkgconfig /usr/include  
# App  
COPY src /var/www/app  

