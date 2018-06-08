# jq v1.5  
  
FROM alpine:3.4  
  
ENV GLIBC_VERSION=2.23-r3 \  
JQ_VERSION=1.5  
  
RUN apk --no-cache add --virtual build-dependencies curl make gcc g++ \  
&& curl --location --show-error -O https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/sgerrand.rsa.pub \  
&& mv -f sgerrand.rsa.pub /etc/apk/keys/ \  
&& curl --location --show-error -O https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \  
&& apk add glibc-${GLIBC_VERSION}.apk \  
&& rm -f glibc-${GLIBC_VERSION}.apk /etc/apk/keys/sgerrand.rsa.pub \  
&& curl --location --show-error -O
https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-${JQ_VERSION}.tar.gz
\  
&& tar xvzf jq-${JQ_VERSION}.tar.gz \  
&& cd jq-${JQ_VERSION} \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf jq-${JQ_VERSION}.tar.gz jq-${JQ_VERSION} glibc-${GLIBC_VERSION}.apk
/etc/apk/keys/sgerrand.rsa.pub \  
&& apk del --purge build-dependencies  

