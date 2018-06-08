FROM alpine:3.2  
MAINTAINER Marco Schirrmeister <marco@schirrmeister.net>  
  
# https://github.com/mendsley/docker-alpine-gosu/blob/master/Dockerfile  
ENV GOSU_VERSION="1.10" \  
GOSU_DOWNLOAD_URL="https://github.com/tianon/gosu/releases/download/1.10/gosu-
amd64" \  
GOSU_DOWNLOAD_SIG="https://github.com/tianon/gosu/releases/download/1.10/gosu-
amd64.asc" \  
GOSU_DOWNLOAD_KEY="0x036A9C25BF357DD4" \  
DUMBINIT_VERSION="1.2.0" \  
DUMBINIT_SHA256="81231da1cd074fdc81af62789fead8641ef3f24b6b07366a1c34e5b059faf363"  
  
RUN buildDeps='gnupg' HOME='/root' \  
&& set -x \  
&& apk --update add nodejs git openssh ca-certificates \  
&& apk add --update $buildDeps \  
&& gpg-agent --daemon \  
&& gpg --keyserver pgp.mit.edu --recv-keys $GOSU_DOWNLOAD_KEY \  
&& echo "trusted-key $GOSU_DOWNLOAD_KEY" >> /root/.gnupg/gpg.conf \  
&& curl -sSL "$GOSU_DOWNLOAD_URL" > gosu-amd64 \  
&& curl -sSL "$GOSU_DOWNLOAD_SIG" > gosu-amd64.asc \  
&& gpg --verify gosu-amd64.asc \  
&& rm -f gosu-amd64.asc \  
&& mv gosu-amd64 /usr/bin/gosu \  
&& chmod +x /usr/bin/gosu \  
&& apk del --purge $buildDeps \  
&& rm -rf /root/.gnupg \  
&& rm -rf /var/cache/apk/* \  
&& npm install git2consul@0.12.13 \--global \  
&& mkdir -p /git2consul/config \  
&& curl -sfSL https://github.com/Yelp/dumb-
init/releases/download/v${DUMBINIT_VERSION}/dumb-
init_${DUMBINIT_VERSION}_amd64 -o /bin/dumb-init \  
&& echo "$DUMBINIT_SHA256 */bin/dumb-init" | sha256sum -c - \  
&& chmod +x /bin/dumb-init \  
;  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
  

