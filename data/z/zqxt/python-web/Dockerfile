FROM python:3-alpine  
MAINTAINER WeizhongTu <tuweizhong@163.com>  
  
RUN echo $'[global]\n\  
timeout = 60\n\  
index-url = http://mirrors.aliyun.com/pypi/simple\n\  
[install]\n\  
trusted-host = mirrors.aliyun.com' > /etc/pip.conf && \  
sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
&& \  
apk add --no-cache libxml2-dev libxslt-dev mariadb-client-libs mariadb-dev \  
openssl-dev pcre pcre-dev libc-dev \  
libuuid mailcap linux-headers gcc g++ make \  
supervisor curl && \  
curl http://tengine.taobao.org/download/tengine-2.2.2.tar.gz -o
/tmp/tengine-2.2.2.tar.gz && \  
curl http://luajit.org/download/LuaJIT-2.0.5.tar.gz -o
/tmp/LuaJIT-2.0.5.tar.gz && \  
curl https://codeload.github.com/openresty/lua-nginx-module/tar.gz/v0.10.11 -o
/tmp/lua-nginx-module-0.10.11.tar.gz && \  
curl https://codeload.github.com/simpl/ngx_devel_kit/tar.gz/v0.3.0 -o
/tmp/ngx_devel_kit-0.3.0.tar.gz && \  
tar -xvzf /tmp/tengine-2.2.2.tar.gz -C /tmp && \  
tar -xvzf /tmp/LuaJIT-2.0.5.tar.gz -C /tmp && \  
tar -xvzf /tmp/lua-nginx-module-0.10.11.tar.gz -C /tmp && \  
tar -xvzf /tmp/ngx_devel_kit-0.3.0.tar.gz -C /tmp && \  
cd /tmp/LuaJIT-2.0.5 && make -j2 && make install && \  
cd /tmp/tengine-2.2.2 && \  
export LUAJIT_LIB=/usr/local/lib/luajit && \  
export LUAJIT_INC=/usr/local/include/luajit-2.0 && \  
export TENGINE_PREFIX=/usr/local/tengine && \  
./configure --prefix=$TENGINE_PREFIX --add-module=/tmp/lua-nginx-
module-0.10.11 --add-module=/tmp/ngx_devel_kit-0.3.0 && \  
make -j2 && make install &&\  
ln -s $TENGINE_PREFIX/sbin/nginx $TENGINE_PREFIX/sbin/tengine && \  
ln -s $TENGINE_PREFIX/sbin/nginx /usr/local/bin/tengine && \  
ln -s $TENGINE_PREFIX /etc/nginx && \  
mkdir -p /etc/supervisor.d/ && \  
echo $'\n\  
[program:tengine]\n\  
command=/usr/local/bin/tengine\n\  
' >> /etc/supervisor.d/tengine.ini && \  
pip install --no-cache-dir -I mysqlclient lxml uWSGI==2.0.17 && \  
apk del mariadb-dev openssl-dev pcre-dev libxml2-dev libxslt-dev linux-headers
gcc g++ make && \  
apk add --no-cache libxml2 openssl mariadb-client-libs libgcc pcre && \  
cd / && rm -rf /tmp/*  
  
  
EXPOSE 80  
CMD ["sh"]  

