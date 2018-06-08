ARG DOCKER_REGISTRY=docker.io  
ARG DOCKER_IMG_TAG=":2018-04-25"  
ARG
DOCKER_IMG_HASH="@sha256:2074c4a688a1544f3e937403cd08e71b3380927e9ff12284f400f789d17700a0"  
FROM ${DOCKER_REGISTRY}/qnib/alplain-
openjre8${DOCKER_IMG_TAG}${DOCKER_IMG_HASH}  
  
  
ARG GLIBC_VER=2.27-r0  
  
RUN apk --no-cache add curl ca-certificates bash \  
&& curl -sLo /tmp/glibc.apk "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VER}/glibc-${GLIBC_VER}.apk" \  
&& apk --no-cache --allow-untrusted add /tmp/glibc.apk \  
&& curl -sLo /tmp/glibc-bin.apk "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VER}/glibc-bin-${GLIBC_VER}.apk" \  
&& apk --no-cache --allow-untrusted add /tmp/glibc-bin.apk \  
&& ldconfig /lib /usr/glibc/usr/lib \  
&& rm -f /tmp/glibc.apk /tmp/glibc-bin.apk  

