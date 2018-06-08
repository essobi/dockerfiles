# jo v1.0  
  
FROM alpine:3.4  
  
ENV GLIBC_VERSION=2.23-r3 \  
JO_VERSION=1.0  
  
RUN apk \--no-cache add \--virtual build-dependencies curl make automake
autoconf gcc g++ \  
&& curl \--location \--show-error -O https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/sgerrand.rsa.pub \  
&& mv -f sgerrand.rsa.pub /etc/apk/keys/ \  
&& curl \--location \--show-error -O https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \  
&& apk add glibc-${GLIBC_VERSION}.apk \  
&& curl \--location \--show-error -O
https://github.com/jpmens/jo/archive/v${JO_VERSION}.tar.gz \  
&& tar xvzf v${JO_VERSION}.tar.gz \  
&& cd jo-${JO_VERSION} \  
&& autoreconf -i \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf v${JO_VERSION}.tar.gz jo-${JO_VERSION} glibc-${GLIBC_VERSION}.apk
/etc/apk/keys/sgerrand.rsa.pub \  
&& apk del \--purge build-dependencies  
  
ENTRYPOINT ["/usr/local/bin/jo"]  

