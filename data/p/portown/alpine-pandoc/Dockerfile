FROM alpine:3.6  
  
ENV PANDOC_VERSION 2.0.2  
ENV PANDOC_DOWNLOAD_URL
https://github.com/jgm/pandoc/archive/$PANDOC_VERSION.tar.gz  
ENV PANDOC_DOWNLOAD_SHA512
5830e0d8670a0bf80d9e8a84412d9f3782d5a6d9cf384fc7a853ad7f4e41a94ed51322ca73b86ad93528a7ec82eaf343704db811ece3455e68f1049761544a88  
ENV PANDOC_ROOT /usr/local/pandoc  
  
RUN apk add --no-cache \  
gmp \  
libffi \  
&& apk add --no-cache --virtual build-dependencies \  
\--repository "http://nl.alpinelinux.org/alpine/edge/community" \  
ghc \  
cabal \  
linux-headers \  
musl-dev \  
zlib-dev \  
curl \  
&& mkdir -p /pandoc-build && cd /pandoc-build \  
&& curl -fsSL "$PANDOC_DOWNLOAD_URL" -o pandoc.tar.gz \  
&& echo "$PANDOC_DOWNLOAD_SHA512 pandoc.tar.gz" | sha512sum -c - \  
&& tar -xzf pandoc.tar.gz && rm -f pandoc.tar.gz \  
&& ( cd pandoc-$PANDOC_VERSION && cabal update && cabal install --only-
dependencies \  
&& cabal configure --prefix=$PANDOC_ROOT \  
&& cabal build \  
&& cabal copy \  
&& cd .. ) \  
&& rm -Rf pandoc-$PANDOC_VERSION/ \  
&& apk del --purge build-dependencies \  
&& rm -Rf /root/.cabal/ /root/.ghc/ \  
&& cd / && rm -Rf /pandoc-build  
  
ENV PATH $PATH:$PANDOC_ROOT/bin  

