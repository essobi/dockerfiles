FROM tiredofit/nodejs:8-latest  
LABEL maintainer="Dave Conroy (dave at tiredofit dot ca)"  
  
### Disable Features From Base Image  
ENV ENABLE_SMTP=false  
  
### Create User  
RUN addgroup haraka && \  
adduser -S \  
-D -G haraka \  
-h /data/ \  
haraka && \  
  
  
### Install Build Dependencies  
apk upgrade && \  
apk add --virtual haraka-build-dependencies \  
gcc \  
g++ \  
libpcap-dev \  
libtool \  
make \  
musl-dev \  
&& \  
  
### Install Runtime Dependencies  
apk add \  
curl \  
libpcap \  
libressl \  
python \  
tar \  
wget \  
&& \  
  
### Build Iconv  
mkdir -p /usr/src/iconv && \  
curl http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.15.tar.gz | tar xfz -
--strip 1 -C /usr/src/iconv && \  
cd /usr/src/iconv && \  
sed -i 's/_GL_WARN_ON_USE (gets, "gets is a security hole - use fgets
instead");/#if HAVE_RAW_DECL_GETS\n_GL_WARN_ON_USE (gets, "gets is a security
hole - use fgets instead");\n#endif/g' srclib/stdio.in.h && \  
./configure --prefix=/usr/local && \  
make && \  
make install && \  
libtool --finish /usr/local/lib && \  
  
#### Install Haraka  
cd /usr/src && \  
npm -g install --unsafe-perm --production \  
express \  
Haraka \  
haraka-plugin-geoip \  
haraka-plugin-ldap \  
haraka-plugin-limit \  
haraka-plugin-p0f \  
iconv \  
maxmind-geolite-mirror \  
mkdirp \  
sqlite3 \  
toobusy-js \  
tmp \  
&& \  
  
  
#### Install p0f  
mkdir -p /usr/src/p0f && \  
curl http://lcamtuf.coredump.cx/p0f3/releases/p0f-3.09b.tgz | tar xzf -
--strip 1 -C /usr/src/p0f && \  
cd /usr/src/p0f && \  
./build.sh && \  
cp p0f /usr/sbin/ && \  
cp p0f.fp /etc/p0f.fp && \  
  
### Misc & Cleanup  
ln -s /data/geoip /usr/local/share/GeoIP && \  
apk del --purge haraka-build-dependencies && \  
rm -rf /var/cache/apk/* /usr/src/*  
  
### Add Files  
ADD install /  
  
### Networking Configuration  
EXPOSE 25 587  

