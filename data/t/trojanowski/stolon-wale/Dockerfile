FROM postgres:9.6  
ENV DUMB_INIT_VERSION 1.2.0  
ENV DUMB_INIT_SHA256
9af7440986893c904f24c086c50846ddc5a0f24864f5566b747b8f1a17f7fd52  
  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends ca-certificates wget &&\  
rm -rf /var/lib/apt/lists/* &&\  
wget -O dumb-init.deb "https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64.deb" &&\  
echo "$DUMB_INIT_SHA256 dumb-init.deb" | sha256sum -c &&\  
dpkg -i dumb-init.deb &&\  
rm dumb-init.deb &&\  
apt-get purge -y --auto-remove ca-certificates wget  
  
ENV BOTO_VERSION 2.47.0  
ENV WALE_VERSION 1.0.3  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends \  
build-essential \  
daemontools \  
lzop \  
pv \  
python3 \  
python3-dev \  
python3-pip &&\  
rm -rf /var/lib/apt/lists/* &&\  
pip3 install wal-e==$WALE_VERSION &&\  
pip3 install boto==$BOTO_VERSION &&\  
rm -rf /tmp/*  
  
ENV STOLON_VERSION 0.6.0  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends wget &&\  
rm -rf /var/lib/apt/lists/* &&\  
wget -O stolon.tar.gz
"https://github.com/sorintlab/stolon/releases/download/v${STOLON_VERSION}/stolon-v${STOLON_VERSION}-linux-$(dpkg
--print-architecture).tar.gz" &&\  
wget -O stolon.tar.gz.sig
"https://github.com/sorintlab/stolon/releases/download/v${STOLON_VERSION}/stolon-v${STOLON_VERSION}-linux-$(dpkg
--print-architecture).tar.gz.sig" &&\  
export GNUPGHOME="$(mktemp -d)" &&\  
gpg --keyserver keys.gnupg.net --recv-keys 1C4F0069 &&\  
gpg --verify stolon.tar.gz.sig stolon.tar.gz &&\  
rm -r "$GNUPGHOME" &&\  
apt-get purge -y --auto-remove wget &&\  
tar -xvzf stolon.tar.gz &&\  
cp stolon-v$STOLON_VERSION-linux-$(dpkg --print-architecture)/stolon*
/usr/local/bin/ &&\  
rm -r stolon-v$STOLON_VERSION-linux-$(dpkg --print-architecture) &&\  
rm stolon.tar.gz*  
  
COPY stolon-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["dumb-init", "stolon-entrypoint.sh"]  
CMD ["bash", "-c", "echo \"Please specify command\"; exit 1"]  

