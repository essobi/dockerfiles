FROM alpine:latest  
# IMAGE yukoff/alpine-bdb48  
# ENV BUILDER DOCKERHUB  
#ADD http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz /tmp/  
# RUN cd /tmp && \  
# (echo '12edc0df75bf9abd7f82f821795bcee50f42cb2e5f76a6a281b85732798364ef
db-4.8.30.NC.tar.gz' | sha256sum -c) && \  
RUN apk \--no-cache upgrade && \  
apk \--no-cache add \  
build-base \  
autoconf \  
automake \  
libtool && \  
wget -P /tmp/ http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz && \  
cd /tmp && \  
(echo '12edc0df75bf9abd7f82f821795bcee50f42cb2e5f76a6a281b85732798364ef
db-4.8.30.NC.tar.gz' | sha256sum -c) && \  
tar -xvf /tmp/db-*.tar.gz -C /tmp/ && \  
cd /tmp/db-4.8.30.NC/build_unix && \  
../dist/configure \--prefix=/usr \  
\--includedir=/usr/include/db4 \  
\--enable-cxx \  
\--enable-compat185 \  
\--disable-shared \  
\--with-pic && \  
make -j `grep -c ^processor /proc/cpuinfo` && \  
make strip=true install && \  
rm -rf /usr/docs && \  
cd \- && \  
apk del \  
libtool \  
automake \  
autoconf \  
build-base && \  
rm -rf /tmp/db*  
# mkdir -p /usr/include/db4 && \  
# mv /usr/include/*.h /usr/include/db4 && \  
# echo "#include <db4/db.h>" > /usr/include/db.h && \  
# echo "#include <db4/db_185.h>" > /usr/include/db_185.h && \  
# echo "#include <db4/db_cxx.h>" > /usr/include/db_cxx.h  

