FROM openresty/openresty:alpine-fat AS build  
RUN apk update  
RUN apk add ca-certificates  
RUN apk add openssl  
RUN apk add git  
RUN apk add automake  
RUN apk add autoconf  
RUN apk add libtool  
RUN apk add g++  
  
WORKDIR /tmp/gumbo  
RUN git clone https://github.com/google/gumbo-parser.git . && \  
git checkout tags/v0.10.1 -b build && \  
./autogen.sh && \  
./configure && \  
make && \  
make install  
RUN luarocks install gumbo  
  
WORKDIR /tmp/pugilua  
RUN git clone \--recursive https://github.com/d-led/pugilua.git .  
WORKDIR /tmp/pugilua/deps/pugixml  
RUN git pull origin master && \  
git checkout tags/v1.8.1 -b build  
WORKDIR /tmp/pugilua  
RUN sed -i -e 's/-llua5.1/-lluajit-5.1/g' Build/linux/gmake/pugilua.make && \  
LDFLAGS=-L/usr/local/openresty/luajit/lib
INCLUDES=-I/usr/local/openresty/luajit/include/luajit-2.1 make -C
Build/linux/gmake config=release && \  
cp bin/linux/gmake/pugilua.so /usr/local/openresty/lualib  
  
RUN luarocks install lua-resty-jwt  
RUN luarocks install luacov  
RUN luarocks install luacov-console  
###  
FROM openresty/openresty:alpine  
RUN apk update  
RUN apk add py-pip  
RUN apk add libstdc++  
RUN pip install awscli --upgrade  
COPY \--from=build /usr/local/ /usr/local/  

