FROM alpine:3.6  
ARG VERSION=1.0.1  
RUN cd /tmp &&\  
apk add --no-cache parallel exiftool &&\  
apk add --no-cache --virtual .build-deps \  
libpng-dev \  
alpine-sdk \  
git \  
coreutils \  
cmake \  
&&\  
\  
wget https://github.com/google/guetzli/archive/v${VERSION}.tar.gz -O
/tmp/guetzli-${VERSION}.tar.gz &&\  
(tar xpf guetzli-${VERSION}.tar.gz &&\  
cd guetzli-${VERSION} &&\  
make -j$(nproc) config=release \  
TARGETDIR=/usr/local/bin \  
) &&\  
\  
runDeps="$( \  
scanelf --needed --nobanner /usr/local/bin/guetzli \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" &&\  
apk add --no-cache --virtual .run-deps $runDeps &&\  
\  
apk del --no-cache .build-deps &&\  
rm -rf /var/tmp/* /tmp/* /opt/build &&\  
mkdir /work  
  
ENV QUALITY=90  
ENV MAX_PROCS=1  
ENV KEEP_EXIF=1  
COPY run.sh one.sh /  
VOLUME /work  
WORKDIR /work  
ENTRYPOINT ["/run.sh"]  
CMD ["all"]  

