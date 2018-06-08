FROM alpine:3.3  
MAINTAINER @VITIMan https://github.com/VITIMan  
  
# 036A9C25BF357DD4 - Tianon Gravi <tianon@tianon.xyz>  
# http://pgp.mit.edu/pks/lookup?op=vindex&search=0x036A9C25BF357DD4  
ENV GOSU_VERSION="1.7" \  
GOSU_ARCHITECTURE="amd64"  
ENV
GOSU_DOWNLOAD_URL="https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$GOSU_ARCHITECTURE"
\  
GOSU_DOWNLOAD_SIG="https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$GOSU_ARCHITECTURE.asc"
\  
GOSU_DOWNLOAD_KEY="0x036A9C25BF357DD4"  
# Download and install gosu  
# https://github.com/tianon/gosu/releases  
RUN buildDeps='curl gnupg' HOME='/root' \  
&& set -x \  
&& apk add --update $buildDeps \  
&& gpg-agent --daemon \  
&& gpg --keyserver pgp.mit.edu --recv-keys $GOSU_DOWNLOAD_KEY \  
&& echo "trusted-key $GOSU_DOWNLOAD_KEY" >> /root/.gnupg/gpg.conf \  
&& curl -sSL "$GOSU_DOWNLOAD_URL" > gosu-$GOSU_ARCHITECTURE \  
&& curl -sSL "$GOSU_DOWNLOAD_SIG" > gosu-$GOSU_ARCHITECTURE.asc \  
&& gpg --verify gosu-$GOSU_ARCHITECTURE.asc \  
&& rm -f gosu-$GOSU_ARCHITECTURE.asc \  
&& mv gosu-$GOSU_ARCHITECTURE /usr/bin/gosu \  
&& chmod +x /usr/bin/gosu \  
&& apk del --purge $buildDeps \  
&& rm -rf /root/.gnupg \  
&& rm -rf /var/cache/apk/* \  
;  

