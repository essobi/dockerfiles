FROM neonproject/lua  
  
MAINTAINER Charles Heywood <charles@hashbang.sh>  
  
## Dependencies  
RUN \  
echo '-- Adding cqueues dependencies via apk --' && \  
apk add --update openssl-dev m4 bsd-compat-headers && \  
echo '-- Installing "http" via luarocks-5.2 --' && \  
luarocks-5.2 install --server=http://luarocks.org/dev http \  
CFLAGS='-O2 -fPIC -I/usr/include -I/usr/include/lua5.2 \  
-DHAVE_SYS_SYSCTL_H=0 -DHAVE_RANDOM_UUID=0'  
  
# software  
RUN git clone https://github.com/ProjectNeon/NeonConfig.git /app/neonconfig  
WORKDIR /app/neonconfig  
  
# startup  
ENTRYPOINT lua main.lua  

