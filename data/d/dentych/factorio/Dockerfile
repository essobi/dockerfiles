FROM alpine:3.6  
ARG GLIBC_VERSION=2.25-r0  
  
RUN \  
# Install build dependencies \  
apk --no-cache add \  
ca-certificates \  
openssl \  
\  
# Adding public keys to allow install of glibc \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
\  
# Downloading apk packages \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk \  
\  
# Installing glibc \  
&& apk --no-cache add \  
glibc-${GLIBC_VERSION}.apk \  
glibc-bin-${GLIBC_VERSION}.apk \  
\  
# Removing the downloaded packages \  
&& rm -f glibc-${GLIBC_VERSION}.apk \  
&& rm -f glibc-bin-${GLIBC_VERSION}.apk \  
\  
# Removing build dependencies  
&& apk --no-cache del \  
ca-certificates \  
openssl  
  
ARG FACTORIO_VERSION=0.15.34  
RUN \  
# Install build dependencies \  
apk --no-cache add \  
ca-certificates \  
openssl \  
tar \  
xz \  
\  
# Creating opt \  
&& mkdir /opt \  
\  
# Install Factorio into opt \  
&& wget -qO- https://www.factorio.com/get-
download/${FACTORIO_VERSION}/headless/linux64 | tar xvJ -C /opt \  
\  
# Remove build dependencies \  
&& apk --no-cache del \  
ca-certificates \  
openssl \  
tar \  
xz  
  
RUN \  
# Touch savegame \  
mkdir -p /opt/factorio/saves  
  
WORKDIR /opt/factorio/saves  
  
VOLUME ["/opt/factorio/saves"]  
  
ENTRYPOINT ["/opt/factorio/bin/x64/factorio"]  
  
CMD ["--start-server", "savegame.zip"]  
  
EXPOSE 34197/udp  

