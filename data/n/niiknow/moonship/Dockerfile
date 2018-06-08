FROM niiknow/openresty:0.1.4  
  
MAINTAINER noogen <friends@niiknow.org>  
  
# Add additional binaries into PATH for convenience  
ENV
LUA_PATH="/app/?.lua;/app/?/?.lua;/app/?/init.lua;/app/lib/?.lua;/app/lib/?/?.lua;/usr/local/openresty/site/lualib/?.lua;/usr/local/openresty/site/lualib/?/init.lua;/usr/local/openresty/lualib/?.lua;/usr/local/openresty/lualib/?/init.lua;/usr/local/openresty/lib/?.lua;;"
\  
AWS_DEFAULT_REGION="us-east-1" \  
MOONSHIP_APP_PATH="/app" \  
MOONSHIP_APP_ENV="prd" \  
MOONSHIP_CODECACHE_SIZE=10000  
  
RUN \  
# Make info file about this build  
printf "Build of niiknow/moonship, date: %s\n" `date -u +"%Y-%m-%dT%H:%M:%SZ"`
>> /etc/BUILDS/zz-moonship && \  
# begin  
apk add --no-cache --virtual runtime \  
bash \  
coreutils \  
curl \  
diffutils \  
grep \  
nano \  
less \  
python \  
py-pip \  
rsync \  
sed \  
  
openssl-dev && \  
  
apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
git && \  
  
pip install awscli && \  
# Even though we install full pkill (via the procps package, which we do for  
# "-U" support in our tests), the /usr/bin version that symlinks BusyBox's  
# more limited pkill version takes precedence. So manually remove this  
# BusyBox symlink to the full pkill version is used.  
if [ -L /usr/bin/pkill ]; then rm /usr/bin/pkill; fi && \  
# install libs  
luarocks install lua-resty-jwt 0.1.10-1 && \  
luarocks install lua-resty-http 0.08-0 && \  
luarocks install moonscript && \  
luarocks install luacrypto 0.3.2-2 && \  
luarocks install lua-lru 1.0-1 && \  
luarocks install basexx 0.1.0-1 && \  
luarocks install lpath 0.1.0-1 && \  
luarocks install lua-log 0.1.6-1 && \  
luarocks install --server=http://luarocks.org/dev ltn12 && \  
luarocks install luasec 0.6-1 && \  
  
addgroup -S nginx && \  
adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx && \  
  
apk --purge -v del py-pip .build-deps && \  
  
rm -rf /var/cache/apk/*  
  
COPY rootfs/. /  
  
COPY lib/. /app-start/lib/  
  
EXPOSE 80 443  
  
VOLUME ["/app"]  
  

