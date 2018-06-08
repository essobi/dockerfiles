FROM alpine:3.5  
  
MAINTAINER Peter Teich <mail@pteich.xyz>  
  
ENV GOSU_VERSION 1.10  
ENV DUMBINIT_VERSION 1.2.0  
ENV BITFAN_VERSION 29  
  
RUN addgroup -S bitfan && adduser -S -G bitfan bitfan  
  
RUN mkdir -p /opt  
  
RUN set -x \  
&& apk update && apk add \--no-cache --virtual .deps \  
openssl \  
dpkg \  
ca-certificates \  
&& update-ca-certificates \  
&& cd /opt \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-${dpkgArch}"
\  
&& chmod +x /usr/local/bin/gosu \  
&& wget -O /usr/local/bin/dumb-init "https://github.com/Yelp/dumb-
init/releases/download/v${DUMBINIT_VERSION}/dumb-
init_${DUMBINIT_VERSION}_${dpkgArch}" \  
&& chmod +x /usr/local/bin/dumb-init \  
&& wget -O bitfan.tar.gz
"https://github.com/vjeantet/bitfan/releases/download/${BITFAN_VERSION}/bitfan_v${BITFAN_VERSION}_linux_${dpkgArch}.tgz"
\  
&& tar xzvf bitfan.tar.gz \  
&& rm -f bitfan.tar.gz \  
&& mv releases/bitfan_v${BITFAN_VERSION}_linux_${dpkgArch}
/usr/local/bin/bitfan \  
&& apk del .deps  
  
RUN mkdir /config && chown bitfan:bitfan /config  
VOLUME ["/config"]  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "/usr/local/bin/gosu", "bitfan",
"/usr/local/bin/bitfan"]  
  
CMD [""]  

