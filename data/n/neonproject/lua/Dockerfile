##################  
# Lua Dockerfile #  
# Alpine-based #  
##################  
FROM alpine  
  
MAINTAINER Adrian "vifino" Pistol  
  
# Add a volume to store the application in.  
VOLUME ["/app"]  
WORKDIR /app  
  
# Normally, this would add vifino's repo too, but temporarily, the server is
down.  
# As a fix, the repo is disabled.  
# TODO: Add it again once server is back up.  
# Adding the repo:  
# echo "http://repo.i0i0.me/alpine/edge" >> /etc/apk/repositories && \  
# wget http://repo.i0i0.me/alpine/adinator1999@gmail.com-5675c1f0.rsa.pub -O
/etc/apk/keys/adinator1999@gmail.com-5675c1f0.rsa.pub && \  
RUN \  
echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
&& \  
apk update && \  
apk upgrade && \  
apk add \  
lua5.2-dev luarocks5.2 \  
unzip alpine-sdk \  
&& \  
ln -s lua5.2 /usr/bin/lua && \  
ln -s luarocks-5.2 /usr/bin/luarocks && \  
rm -rf /var/cache/apk/*  

