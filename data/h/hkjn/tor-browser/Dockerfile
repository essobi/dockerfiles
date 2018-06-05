FROM debian  
  
ENV TOR_VERSION=8.0a5  
# Via https://dist.torproject.org/torbrowser/$TOR_VERSION/sha256sums-signed-
build.txt  
ENV
SHA256_CHECKSUM=53fe3fc01de04eb9337cfea2299f390b47130f9ac7a9507d0e3f2d86728f5319  
ENV LANG=C.UTF-8  
ENV RELEASE_FILE=tor-browser-linux64-${TOR_VERSION}_en-US.tar.xz  
ENV RELEASE_KEY=0x4E2C6E8793298290  
ENV
RELEASE_URL=https://dist.torproject.org/torbrowser/${TOR_VERSION}/${RELEASE_FILE}  
ENV PATH=$PATH:/usr/local/bin/Browser  
  
RUN apt-get update && \  
apt-get install -y \  
ca-certificates \  
curl \  
file \  
gpg \  
libx11-xcb1 \  
libasound2 \  
libdbus-glib-1-2 \  
libgtk2.0-0 \  
libxrender1 \  
libxt6 \  
xz-utils && \  
rm -rf /var/lib/apt/lists/* && \  
useradd --create-home --home-dir /home/user user && \  
chown -R user:user /home/user  
  
WORKDIR /usr/local/bin  
# TODO(hkjn): Stop having gpg import key command separate layer, if we  
# can figure out why it's flaky and commonly gives "keys: key  
# 4E2C6E8793298290 can't be retrieved, gpg: no valid OpenPGP data  
# found."  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys ${RELEASE_KEY}  
  
RUN curl --fail -O -sSL ${RELEASE_URL} && \  
curl --fail -O -sSL ${RELEASE_URL}.asc && \  
gpg --verify ${RELEASE_FILE}.asc && \  
echo "$SHA256_CHECKSUM $RELEASE_FILE" > sha256sums.txt && \  
sha256sum -c sha256sums.txt && \  
tar --strip-components=1 -vxJf ${RELEASE_FILE} && \  
rm -v ${RELEASE_FILE}* sha256sums.txt && \  
mkdir -p /usr/local/bin/Browser/Downloads && \  
chown -R user:user /usr/local/bin  
  
WORKDIR /usr/local/bin/Browser/Downloads  
USER user  
COPY ["start", "/usr/local/bin/"]  
ENTRYPOINT ["start"]  
CMD [""]  

