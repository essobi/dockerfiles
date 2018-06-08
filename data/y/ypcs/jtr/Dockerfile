FROM ypcs/debian:jessie  
  
ENV JOHN_VERSION 1.8.0-jumbo-1  
ENV JOHN_SHA256 XX  
  
VOLUME /data  
ENV WORDLIST_DIR /wordlists  
  
RUN mkdir -p "${WORDLIST_DIR}"  
  
RUN \  
/usr/local/sbin/docker-upgrade && \  
apt-get --assume-yes install \  
build-essential \  
libssl-dev \  
libssl1.0.0 \  
libkrb5-3 \  
libgmp10 \  
libgmp-dev \  
zlib1g-dev \  
libnss3-dev \  
libkrb5-dev \  
libgomp1 \  
curl && \  
cd /usr/src && \  
curl -fSL "http://www.openwall.com/john/j/john-${JOHN_VERSION}.tar.xz" -o
"john-${JOHN_VERSION}.tar.xz" && \  
tar xJf "john-${JOHN_VERSION}.tar.xz" && \  
cd john-* && \  
cd src && \  
./configure && \  
make && \  
cd .. && \  
cp -R run /usr/local/john && \  
cd ../.. && \  
rm -rf john-* && \  
apt-get --assume-yes remove \  
build-essential \  
libssl-dev \  
libgmp-dev \  
zlib1g-dev \  
libkrb5-dev \  
gcc \  
gcc-4.9 \  
dpkg-dev \  
libicu52 \  
libnss3-dev && \  
echo '#!/bin/sh\nset -e\n/usr/local/john/john $@' > /usr/bin/john && \  
chmod +x /usr/bin/john && \  
/usr/local/sbin/docker-cleanup  
  
RUN \  
mkdir -p "${WORDLIST_DIR}" && \  
cd /usr/src && \  
curl -fSL "http://kaino.kotus.fi/sanat/nykysuomi/kotus-sanalista-v1.tar.gz" -o
"kotus-sanalista-v1.tar.gz" && \  
tar xzf kotus-sanalista-v1.tar.gz && \  
sed -ne 's,.*<s>\\(.*\\)</s>.*,\1,p' kotus-sanalista_v1/kotus-sanalista_v1.xml
> "${WORDLIST_DIR}/finnish.txt" && \  
rm -rf kotus-sanalista*  
  
RUN \  
mkdir -p "${WORDLIST_DIR}/passwords" && \  
cd /usr/src && \  
curl -fSL "https://github.com/danielmiessler/SecLists/archive/master.tar.gz"
-o "seclists.tar.gz" && \  
tar xzf "seclists.tar.gz" && \  
cp -R SecLists-master/Passwords/* "${WORDLIST_DIR}/passwords/" && \  
rm -rf SecLists-master seclists.tar.gz  
  
RUN \  
mkdir -p "${WORDLIST_DIR}/rules"  
  
COPY rules.d/* "${WORDLIST_DIR}/rules/"  
  
WORKDIR /usr/local/john  

