FROM ubuntu:14.04  
MAINTAINER Cogniteev <tech@cogniteev.com>  
  
ADD patches /var/src/vsftpd/patches  
WORKDIR /var/src/vsftpd  
  
# Install requirements  
RUN apt-get update && apt-get install -y \  
gnupg wget debhelper libcap2-dev libpam0g-dev \  
libssl-dev libwrap0-dev dh-apport  
  
# Download source package  
ENV VERSION=3.0.3  
RUN gpg --keyserver ha.pool.sks-keyservers.net \  
\--recv-keys 8660FD3291B184CDBC2F6418AA62EC463C0E751C && \  
wget "https://security.appspot.com/downloads/vsftpd-${VERSION}.tar.gz" && \  
wget "https://security.appspot.com/downloads/vsftpd-${VERSION}.tar.gz.asc" &&
\  
gpg --verify "vsftpd-${VERSION}.tar.gz.asc" "vsftpd-${VERSION}.tar.gz"  
  
# Extract and applies Ubuntu patches  
RUN tar zxf vsftpd-${VERSION}.tar.gz && \  
cd "vsftpd-${VERSION}" && \  
for p in `cat ../patches/series | grep -v '^#'` ; do \  
patch -p1 < "../patches/$p" ; \  
done  
  
# Build and install  
RUN cd "vsftpd-${VERSION}" && \  
CFLAGS="-O2 -fPIE -fstack-protector --param=ssp-buffer-size=4 -Wall -W
-Wshadow -Werror -Wformat-security -D_FORTIFY_SOURCE=2" \  
LDFLAGS="-fPIE -pie -Wl,-z,relro -Wl,-z,now -lwrap -lpam -lssl -lcrypto -lcap"
\  
make && \  
mkdir -p /usr/local/man/man8 /usr/local/man/man5 && \  
make install && \  
vsftpd -version  
  
EXPOSE 21  
CMD /usr/local/sbin/vsftpd  

