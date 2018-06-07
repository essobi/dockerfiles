FROM alpine:3.5  
# Permanent dependencies (runtime)  
#RUN \  
# apk add --no-cache \  
# libpng  
# Dev & build  
ARG GUETZLI_VERSION=v1.0.1  
RUN \  
apk add --no-cache --virtual .build-deps \  
alpine-sdk \  
cmake \  
coreutils \  
git \  
libpng-dev \  
zlib-dev \  
&&\  
\  
git clone "https://github.com/google/guetzli.git" /var/tmp/guetzli &&\  
(cd /var/tmp/guetzli &&\  
git checkout "${GUETZLI_VERSION}" &&\  
make -j$(nproc) config=release \  
TARGETDIR=/usr/local/bin \  
LDFLAGS="-static -lpng -lz -lm" \  
) &&\  
\  
apk del --no-cache .build-deps &&\  
rm -rf /var/tmp/* /tmp/* /opt/build  
  
ENTRYPOINT ["guetzli"]  

