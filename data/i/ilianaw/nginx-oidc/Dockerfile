FROM alpine:edge as lua-builder  
RUN apk update && apk upgrade && apk add git gcc luajit-dev make musl-dev  
RUN mkdir -p /buildroot/usr/lib/lua/5.1 /buildroot/usr/share/lua/5.1  
WORKDIR /usr/src  
RUN git clone https://github.com/openresty/lua-cjson && cd lua-cjson \  
&& git reset --hard a03094c5473d9a9764bb486fbe5e99a62d166dae # 2.1.0.6  
RUN make -C lua-cjson LUA_INCLUDE_DIR=/usr/include/luajit-2.1 \  
&& cp -v lua-cjson/cjson.so /buildroot/usr/lib/lua/5.1/  
RUN git clone https://github.com/openresty/lua-resty-string && cd lua-resty-
string \  
&& git reset --hard 2ac7c3bdba55e06bbfd8d76aa981611ffb2cb321 # v0.11  
RUN git clone https://github.com/pintsized/lua-resty-http && cd lua-resty-http
\  
&& git reset --hard 607ef6b2fbff5112b9acc47d9163635c2fbd8f59 # v0.12  
RUN git clone https://github.com/bungle/lua-resty-session && cd lua-resty-
session \  
&& git reset --hard 4429a06ffac1724a056fafa954c0394d437b261f # v2.22  
RUN git clone https://github.com/SkyLothar/lua-resty-jwt && cd lua-resty-jwt \  
&& git reset --hard ee1d024071f872e2b5a66eaaf9aeaf86c5bab3ed # v0.1.11  
RUN git clone https://github.com/jkeys089/lua-resty-hmac && cd lua-resty-hmac
\  
&& git reset --hard 989f601acbe74dee71c1a48f3e140a427f2d03ae  
RUN git clone https://github.com/pingidentity/lua-resty-openidc && cd lua-
resty-openidc \  
&& git reset --hard a119260cce1e63774e9c0ad118b2c843b9a9cad2 # v1.5.4  
RUN cp -rv \  
lua-resty-string/lib/* \  
lua-resty-http/lib/* \  
lua-resty-session/lib/* \  
lua-resty-jwt/lib/* \  
lua-resty-hmac/lib/* \  
lua-resty-openidc/lib/* \  
/buildroot/usr/share/lua/5.1/  
  
FROM ilianaw/nginx  
COPY --from=lua-builder /buildroot/ /  

