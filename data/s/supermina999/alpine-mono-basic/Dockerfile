FROM frolvlad/alpine-mono  
  
RUN apk add --no-cache --virtual=.build-dependencies wget ca-certificates tar
xz && \  
wget "https://www.archlinux.org/packages/extra/x86_64/mono-basic/download/" -O
"/tmp/mono-basic.pkg.tar.xz" && \  
tar -xJf "/tmp/mono-basic.pkg.tar.xz" && \  
cert-sync /etc/ssl/certs/ca-certificates.crt && \  
apk del .build-dependencies && \  
rm /tmp/*  

