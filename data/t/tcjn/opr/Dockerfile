FROM openresty/openresty:xenial  
  
# Various fixes to make lapis happy  
RUN apt update && \  
apt install -y libssl-dev git wget && \  
cd /tmp && \  
git clone https://github.com/openresty/lua-cjson && \  
cd lua-cjson && \  
luarocks make && \  
apt purge --autoremove -y git && \  
mkdir /app/ && \  
cd /app/ && \  
wget https://raw.githubusercontent.com/pygy/require.lua/master/require.lua &&
\  
/usr/local/openresty/luajit/bin/luarocks install moonscript && \  
/usr/local/openresty/luajit/bin/luarocks install lapis && \  
rm /tmp/* -R  
  
ADD nginx.conf mime.types /app/  
ONBUILD ADD . /app/  
  
ENTRYPOINT ["/usr/local/openresty/bin/openresty", "-c", "/app/nginx.conf",
"-g", "daemon off;"]  

