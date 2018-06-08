FROM alpine:3.7  
  
LABEL MAINTAINER="Back Yu <yhfszb@gamil.com>"  
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g'
/etc/apk/repositories  
  
ENV GLIBC_VERSION=2.27-r0  
  
RUN apk update \  
&& apk --no-cache add wget ca-certificates \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk \  
&& apk --no-cache add glibc-${GLIBC_VERSION}.apk \  
&& apk --no-cache add glibc-bin-${GLIBC_VERSION}.apk \  
&& apk del wget \  
&& rm -rf /glibc-${GLIBC_VERSION}.apk \  
&& rm -rf /glibc-bin-${GLIBC_VERSION}.apk  

