FROM ubuntu:16.04  
  
LABEL maintainer "Florian Kinder <florian.kinder@fankserver.com>"  
  
COPY ./prosody.cfg.lua.patch /usr/src/prosody.cfg.lua.patch  
  
RUN apt-get update -qq \  
&& apt-get install mercurial -yqqq \  
&& hg clone https://hg.prosody.im/0.9 /usr/src/prosody \  
&& hg clone https://hg.prosody.im/prosody-modules /usr/src/prosody_modules \  
  
&& cd /usr/src/prosody \  
&& apt-get install lua5.1 liblua5.1-0-dev luarocks libexpat1-dev libssl-dev
bsdmainutils git libidn11-dev libevent1-dev libmysqlclient-dev libpq-dev
libsqlite3-dev -yqqq \  
&& luarocks install luasec \  
&& luarocks install luaevent \  
&& luarocks install luaexpat \  
&& luarocks install luasocket \  
&& luarocks install luafilesystem \  
&& luarocks install luabitop \  
&& luarocks install lua-zlib \  
&& luarocks install luadbi-mysql MYSQL_INCDIR=/usr/include/mysql \  
&& luarocks install luadbi-postgresql POSTGRES_INCDIR=/usr/include/postgresql
\  
&& luarocks install luadbi-sqlite3 \  
&& ./configure --prefix=/ \--with-lua-include=/usr/include/lua5.1 \  
&& make \  
&& make install \  
&& patch -p1 /etc/prosody/prosody.cfg.lua < /usr/src/prosody.cfg.lua.patch \  
&& mkdir -p /etc/prosody/conf.d \  
  
&& cd /usr/src/prosody/tools/migration \  
&& make \  
&& make install \  
  
&& useradd -ms /bin/bash prosody \  
&& chown -R prosody /etc/prosody \  
&& chown -R prosody /var/lib/prosody \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80 443 5222 5269 5347 5280 5281  
USER prosody  
ENV __FLUSH_LOG yes  
CMD ["prosody"]  

