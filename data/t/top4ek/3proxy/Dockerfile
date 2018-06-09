FROM alpine  
  
ENV VERSION 0.8.11  
  
RUN apk add --no-cache --virtual .build-deps gcc linux-headers make musl-dev
tar openssl && \  
wget -O 3proxy.tar.gz
"https://github.com/z3APA3A/3proxy/archive/${VERSION}.tar.gz" && \  
mkdir -p /usr/src/3proxy && \  
tar -xzf 3proxy.tar.gz -C /usr/src/3proxy --strip-components=1 && \  
rm 3proxy.tar.gz && \  
make -C /usr/src/3proxy -f Makefile.Linux && \  
make -C /usr/src/3proxy -f Makefile.Linux install && \  
rm -r /usr/src/3proxy && \  
apk del .build-deps  
  
COPY 3proxy.cfg /etc  
EXPOSE 27005  
ENTRYPOINT ["3proxy", "/etc/3proxy.cfg"]  

