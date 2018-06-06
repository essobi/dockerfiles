FROM alpine:3.3  
RUN apk update && \  
apk add nginx-lua lua5.1 lua5.1-sec lua5.1-socket ca-certificates && \  
apk add lua-json lua5.1-lpeg --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \  
ln -s /usr/bin/lua5.1 /usr/bin/lua && \  
apk add \--virtual build-deps make curl && \  
mkdir -p /tmp/src && \  
cd /tmp/src && \  
\  
curl --location -o lua-spore.tgz https://github.com/fperrad/lua-
Spore/archive/0.3.1.tar.gz && \  
tar xzvf lua-spore.tgz && \  
cd lua-Spore-0.3.1/ && \  
make install && \  
cd /tmp/src && \  
\  
curl --location -o nginx-crowd-lua.tgz https://github.com/Dwolla/nginx-crowd-
lua/archive/master.tar.gz && \  
tar xzvf nginx-crowd-lua.tgz && \  
mkdir -p /etc/nginx/lua /usr/local/share/lua/5.1/Spore/Middleware && \  
cp nginx-crowd-lua-master/crowd-auth.lua /etc/nginx/lua && \  
cp nginx-crowd-lua-master/Spore/Middleware/AdvancedCacheKey.lua
/usr/local/share/lua/5.1/Spore/Middleware/AdvancedCacheKey.lua && \  
\  
curl --location -o lua-json.tgz
https://github.com/harningt/luajson/archive/master.tar.gz && \  
tar xzvf lua-json.tgz && \  
cd luajson-master && \  
make install && \  
cd /tmp/src && \  
\  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
apk del build-deps && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["nginx"]  
CMD ["-g", "daemon off;"]  
  

