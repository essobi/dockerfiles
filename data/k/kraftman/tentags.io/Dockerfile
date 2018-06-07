FROM ubuntu:16.04  
# install build dependencies  
RUN apt-get -qq update && apt-get -qqy install libreadline-dev libncurses5-dev
libpcre3-dev libssl-dev perl make curl git-core luarocks software-properties-
common python-software-properties  
  
RUN add-apt-repository ppa:maxmind/ppa && \  
apt-get update && \  
apt-get -y install libgeoip1 libgeoip-dev geoip-bin  
  
# build/install OpenResty  
ENV SRC_DIR /opt  
ENV OPENRESTY_VERSION 1.13.6.1  
ENV OPENRESTY_PREFIX /usr/local/openresty/  
ENV LAPIS_VERSION 1.7.0  
RUN cd $SRC_DIR && curl -LOs
https://openresty.org/download/openresty-$OPENRESTY_VERSION.tar.gz \  
&& tar xzf openresty-$OPENRESTY_VERSION.tar.gz && cd
openresty-$OPENRESTY_VERSION \  
&& ./configure --prefix=$OPENRESTY_PREFIX \  
\--with-luajit \  
\--with-http_realip_module \  
\--with-http_stub_status_module \  
\--with-http_geoip_module \  
&& make -j4 && make install && rm -rf openresty-$OPENRESTY_VERSION*  
  
RUN luarocks install --server=http://rocks.moonscript.org/manifests/leafo
lapis $LAPIS_VERSION && \  
luarocks install moonscript && \  
luarocks install lapis-console  
  
WORKDIR $OPENRESTY_PREFIX/nginx/conf  
  
ENV LAPIS_OPENRESTY $OPENRESTY_PREFIX/nginx/sbin/nginx  
  
#my stuff  
RUN apt-get update && apt-get install -y autossh uuid-dev #dnsmasq  
  
RUN wget http://luarocks.github.io/luarocks/releases/luarocks-2.4.2.tar.gz  
RUN tar -xvzf luarocks-2.4.2.tar.gz  
RUN cd luarocks-2.4.2 && \  
./configure && \  
make build &&\  
make install  
  
RUN luarocks install date  
#RUN echo "\n\n# Docker extra config \nuser=root\naddn-hosts=/etc/hosts\n" >>
/etc/dnsmasq.conf  
COPY GeoIP /geoip  
  
RUN git clone https://github.com/duhoobo/lua-resty-smtp.git && \  
cd lua-resty-smtp && \  
make install  
  
RUN apt-get update && apt-get install -y ca-certificates stunnel4  
  
RUN luarocks install https://raw.githubusercontent.com/woothee/lua-resty-
woothee/master/lua-resty-woothee-1.7.0-1.rockspec && \  
luarocks install web_sanitize && \  
luarocks install https://raw.githubusercontent.com/kraftman/lua-resty-
busted/master/lua-resty-busted-0.0.1-0.rockspec && \  
luarocks install luacov-cobertura  
  
ENV PATH "/usr/local/openresty/bin:${PATH}"  
ENTRYPOINT ["/opt/openresty/nginx/conf/start.sh"]  

