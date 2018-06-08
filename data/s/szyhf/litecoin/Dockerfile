FROM alpine:3.5  
  
LABEL MAINTAINER="Back Yu <yhfszb@gamil.com>"  
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g'
/etc/apk/repositories  
  
ENV LITECOIN_VERSION=0.14.2  
ENV GLIBC_VERSION=2.26-r0  
  
RUN apk update \  
&& apk --no-cache add wget ca-certificates \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk \  
&& apk --no-cache add glibc-${GLIBC_VERSION}.apk \  
&& apk --no-cache add glibc-bin-${GLIBC_VERSION}.apk \  
&& wget
https://download.litecoin.org/litecoin-${LITECOIN_VERSION}/linux/litecoin-${LITECOIN_VERSION}-x86_64-linux-
gnu.tar.gz \  
&& tar xzvf /litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz \  
&& mkdir /root/.litecoin \  
&& apk del wget ca-certificates \  
&& mv /litecoin-${LITECOIN_VERSION}/bin/* /usr/local/bin/ \  
&& rm -rf /litecoin-${LITECOIN_VERSION}/ \  
&& rm -rf /litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz \  
&& rm -rf /glibc-${GLIBC_VERSION}.apk \  
&& rm -rf /glibc-bin-${GLIBC_VERSION}.apk  
  
EXPOSE 9333 9332  
CMD litecoind

