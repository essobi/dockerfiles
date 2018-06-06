FROM anapsix/alpine-java  
  
MAINTAINER TsungKang <tsungkang@163.com>  
ARG VERSION=0.4.1  
# do all in one step  
RUN set -ex && \  
apk add --no-cache --virtual .deps curl tar && \  
mkdir /cerebro && \  
cd /cerebro && \  
curl -sSL
https://github.com/lmenezes/cerebro/releases/download/v${VERSION}/cerebro-${VERSION}.tgz
| tar xz --strip 1 && \  
apk del .deps  
WORKDIR /cerebro  
EXPOSE 9000  
CMD bin/cerebro  
# EOF

