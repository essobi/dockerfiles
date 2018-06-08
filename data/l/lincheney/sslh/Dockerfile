FROM alpine:latest  
  
RUN BUILD_DEPS="gcc pcre-dev musl-dev make libconfig-dev"; \  
VERSION=1.18; \  
apk --no-cache add pcre openssl libconfig $BUILD_DEPS && \  
cd /tmp && \  
wget -O sslh.zip https://github.com/yrutschle/sslh/archive/v$VERSION.zip && \  
unzip sslh.zip && \  
cd sslh-$VERSION && \  
sed -i 's/^USELIBPCRE=.*/USELIBPCRE=1/' Makefile && \  
make sslh && \  
cp ./sslh-fork ./sslh-select /bin && \  
cp COPYING / && \  
ln /bin/sslh-select /bin/sslh && \  
apk del $BUILD_DEPS && \  
cd / && rm -rf /tmp/sshl*  
  
ENTRYPOINT ["sslh", "-f"]  

