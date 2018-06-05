# Asterisk with Lua support  
#  
# VERSION 0.0.2  
#  
# Contain  
# - Asterisk 13  
# - Lua 5.1  
# - LuaRocks  
# - mongodb driver & luamongo  
# - g729  
  
FROM ubuntu:14.04.4  
  
MAINTAINER Sergey Dmitriev <serge.dmitriev@gmail.com>  
  
  
## update ubuntu & install reqs  
  
RUN apt-get check && \  
apt-get update && \  
apt-get install -y \  
build-essential zip unzip libreadline-dev curl libncurses-dev mc aptitude \  
tcsh scons libpcre++-dev libboost-dev libboost-all-dev libreadline-dev \  
libboost-program-options-dev libboost-thread-dev libboost-filesystem-dev \  
libboost-date-time-dev gcc g++ git lua5.1-dev make libmongo-client-dev \  
dh-autoreconf lame sox libzmq3-dev libzmqpp-dev libtiff-tools perl5 && \  
apt-get clean  
  
  
## Asterisk  
  
RUN curl -sf \  
-o /tmp/asterisk.tar.gz \  
-L http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-13.18.5.tar.gz && \  
mkdir /tmp/asterisk && \  
tar -xzf /tmp/asterisk.tar.gz -C /tmp/asterisk --strip-components=1 && \  
cd /tmp/asterisk && \  
contrib/scripts/install_prereq install  
  
RUN cd /tmp/asterisk && \  
./configure --with-pjproject-bundled  
  
RUN cd /tmp/asterisk && \  
make menuselect.makeopts && \  
menuselect/menuselect \  
\--disable BUILD_NATIVE \  
\--enable chan_pjsip \  
menuselect.makeopts && \  
make && make install && \  
apt-get clean  
  
  
## Lua  
  
ENV LUA_HASH 2e115fe26e435e33b0d5c022e4490567  
ENV LUA_MAJOR_VERSION 5.1  
ENV LUA_MINOR_VERSION 5  
ENV LUA_VERSION ${LUA_MAJOR_VERSION}.${LUA_MINOR_VERSION}  
  
RUN mkdir /tmp/lua && \  
cd /tmp/lua && \  
echo "${LUA_HASH} lua-${LUA_VERSION}.tar.gz" > lua-${LUA_VERSION}.md5 && \  
curl -R -O http://www.lua.org/ftp/lua-${LUA_VERSION}.tar.gz && \  
md5sum -c lua-${LUA_VERSION}.md5 && \  
tar -zxf lua-${LUA_VERSION}.tar.gz && \  
cd /tmp/lua/lua-${LUA_VERSION} && \  
make linux && make linux test && make install && \  
cd .. && rm -rf *.tar.gz *.md5 lua-${LUA_VERSION}  
  
  
## Install lua mongo driver  
  
RUN mkdir /tmp/mongo-cxx-driver && \  
curl -sf -o /tmp/mongo-cxx-driver.tar.gz -L https://github.com/mongodb/mongo-
cxx-driver/archive/legacy-0.0-26compat-2.6.11.tar.gz && \  
tar -zxf /tmp/mongo-cxx-driver.tar.gz -C /tmp/mongo-cxx-driver --strip-
components=1 && \  
cd /tmp/mongo-cxx-driver && \  
scons --prefix=/usr --full --use-system-boost install-mongoclient  
  
  
RUN mkdir /tmp/luamongo && \  
curl -sf -o /tmp/luamongo.tar.gz -L
https://github.com/moai/luamongo/archive/v0.4.5.tar.gz && \  
tar -zxf /tmp/luamongo.tar.gz -C /tmp/luamongo --strip-components=1 && \  
cd /tmp/luamongo && \  
make Linux LUAPKG=lua5.1 && \  
cp /tmp/luamongo/mongo.so /usr/local/lib/lua/5.1/mongo.so  
  
  
## Install luarocks  
  
RUN mkdir /tmp/luarocks && \  
curl -sf -o /tmp/luarocks.tar.gz -L
http://luarocks.org/releases/luarocks-2.4.3.tar.gz && \  
tar -zxf /tmp/luarocks.tar.gz -C /tmp/luarocks --strip-components=1 && \  
cd /tmp/luarocks && \  
./configure && \  
make bootstrap  
  
  
## Install luasec  
  
RUN git clone https://github.com/antirek/luasec.git /tmp/luasec && \  
cd /tmp/luasec && \  
luarocks install luasec-0.6-1.rockspec  
  
## Install rocks  
  
RUN luarocks install luasocket && \  
luarocks install inspect && \  
luarocks install redis-lua && \  
luarocks install luafilesystem && \  
luarocks install sendmail && \  
luarocks install lzmq && \  
luarocks install json-lua && \  
luarocks install lua-cjson && \  
luarocks install busted && \  
luarocks install luacov && \  
luarocks install uuid && \  
luarocks install moses && \  
luarocks install luacrypto && \  
luarocks install httpclient && \  
luarocks install lualogging  
  
## g729  
  
RUN mkdir /usr/codecs && \  
cd /usr/codecs && \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-athlon-
sse.so && \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-atom.so &&
\  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-
barcelona.so && \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-
core2-sse4.so && \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-core2.so
&& \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-debug.so
&& \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-geode.so
&& \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-opteron-
sse3.so && \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-opteron.so
&& \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-
pentium-m.so && \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-pentium.so
&& \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-
pentium2.so && \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-
pentium3-no-sse.so && \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-
pentium3.so && \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-
pentium4-no-sse.so && \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-
pentium4-sse3.so && \  
curl -O http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-
pentium4.so && \  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-x86_64-barcelona.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-x86_64-core2-sse4.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-x86_64-core2.so &&
\  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-x86_64-opteron-
sse3.so && \  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-x86_64-opteron.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-x86_64-pentium4.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g723-ast130-gcc4-glibc2.2-x86_64-barcelona.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g723-ast130-gcc4-glibc2.2-x86_64-core2-sse4.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g723-ast130-gcc4-glibc2.2-x86_64-core2.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g723-ast130-gcc4-glibc2.2-x86_64-opteron-
sse3.so && \  
curl -O
http://asterisk.hosting.lv/bin/codec_g723-ast130-gcc4-glibc2.2-x86_64-opteron.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g723-ast130-gcc4-glibc2.2-x86_64-pentium4.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc2.2-x86_64-barcelona.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc2.2-x86_64-core2-sse4.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc2.2-x86_64-core2.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc2.2-x86_64-opteron-
sse3.so && \  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc2.2-x86_64-opteron.so
&& \  
curl -O
http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc2.2-x86_64-pentium4.so

