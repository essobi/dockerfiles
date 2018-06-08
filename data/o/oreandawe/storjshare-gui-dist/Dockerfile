FROM debian:jessie  
ENV DEBIAN_FRONTEND="noninteractive" DISPLAY=":0"  
RUN apt-get update && apt-get install -qqy --no-install-recommends \  
ca-certificates \  
libasound2 \  
libgconf-2-4 \  
libgtk2.0-0 \  
libnss3 \  
libx11-xcb1 \  
libxss1 \  
libxtst6 \  
wget \  
x11-apps  
ENTRYPOINT ["storjshare"]  
ENV DEBFILE="storjshare-gui.amd64.deb" STORJSHAREGUI_VERSION="7.3.2"
SHA256SUM="1c648f37c08e1f5b81f9c6f4fc661b94a4c2b8a0eef917420232c583c70e9559"  
RUN wget -q "https://github.com/Storj/storjshare-
gui/releases/download/v$STORJSHAREGUI_VERSION/$DEBFILE" && \  
echo "$SHA256SUM $DEBFILE" | sha256sum -c && \  
dpkg -i "/$DEBFILE" && \  
rm -f "/$DEBFILE" && \  
ln -sf /opt/storjshare/storjshare /usr/bin/storjshare  

