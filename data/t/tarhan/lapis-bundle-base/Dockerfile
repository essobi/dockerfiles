FROM tarhan/lapis:latest  
  
RUN export LUA_SHAREDIR=/usr/local/openresty/luajit/share/lua/5.1 \  
&& apk add \--no-cache --virtual build-smtp-deps make git \  
&& cd /tmp/ \  
&& git clone https://github.com/duhoobo/lua-resty-smtp.git \  
&& cd lua-resty-smtp \  
&& make install \  
&& cd .. \  
&& rm -Rf lua-resty-smtp \  
&& apk del build-smtp-deps  
  

