FROM openresty/openresty:alpine  
  
MAINTAINER Dmitriy Lekomtsev <lekomtsev@gmail.com>  
  
ENV LAPIS_VERSION 1.6.0-1  
ENV RESTY_LUAROCKS_VERSION="2.4.3"  
  
ENV SRC_DIR /opt  
ENV OPENRESTY_PREFIX /opt/openresty  
ENV LAPIS_ENVIRONMENT docker  
ENV LAPIS_OPENRESTY $OPENRESTY_PREFIX/nginx/sbin/nginx  
  
RUN mkdir -p /app/src \  
&& cd tmp/ \  
# Installing build dependencies for Lapis and luarocks  
&& apk \--no-cache add \  
openssl \  
yaml \  
&& echo "#### Installing build dependencies" \  
&& apk \--no-cache add \--virtual build-deps \  
curl \  
build-base \  
cmake \  
git \  
unzip \  
openssl-dev \  
yaml-dev \  
# Installing luarocks  
&& echo "#### Installing luarocks" \  
&& curl -fSL
http://luarocks.github.io/luarocks/releases/luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz
\  
-o luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& tar xzf luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& cd luarocks-${RESTY_LUAROCKS_VERSION} \  
&& ./configure \--prefix=/usr/local/openresty/luajit \  
\--with-lua=/usr/local/openresty/luajit \  
\--lua-suffix=jit-2.1.0-beta3 \  
\--with-lua-include=/usr/local/openresty/luajit/include/luajit-2.1 \  
&& make build \  
&& make install \  
&& cd /tmp \  
&& rm -rf luarocks-${RESTY_LUAROCKS_VERSION} \  
luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& echo "#### Installing lua-cjson" \  
# Installing lua-cjson from master branch of its git repo  
&& git clone https://github.com/openresty/lua-cjson.git \  
&& cd lua-cjson \  
&& luarocks make \  
&& cd /tmp \  
&& rm -rf lua-cjson \  
&& echo "#### Installing YAML" \  
&& luarocks \--server=http://rocks.moonscript.org install lyaml \  
# Installing Lapis via luarocks  
&& echo "#### Testing YAML" \  
&& echo "#### Installing Moonscript" \  
&& luarocks install moonscript \  
&& echo "#### Installing Lapis" \  
&& luarocks install lapis \  
&& echo "#### Removing dev dependencies" \  
&& apk del build-deps  
  
COPY preinstall*.moon /app/  
  
WORKDIR /app/src  
  
EXPOSE 8080  
  
ENTRYPOINT ["lapis"]  
ONBUILD ADD app.yml /app/  
ONBUILD RUN cd /tmp \  
# Installing luarocks  
&& echo "#### Installing runtime dependencies before any dev dependencies" \  
&& moon /app/preinstall_runtime.moon /app/app.yml \  
&& echo "#### Installing luarocks common buildtime deps" \  
&& apk \--no-cache add \--virtual build-deps \  
curl \  
build-base \  
cmake \  
git \  
unzip \  
tar \  
yaml \  
&& echo "#### Launch Preinstall" \  
&& moon /app/preinstall.moon /app/app.yml \  
&& echo "#### Finishing Preinstall" \  
&& apk del build-deps  
ONBUILD ADD . /app/src  
ONBUILD RUN moonc /app/src  
  
CMD ["server", "production"]  

