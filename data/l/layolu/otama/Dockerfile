FROM debian:jessie  
MAINTAINER layolu <layolulayole@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y gcc g++ make autoconf automake libtool \  
libpng-dev libjpeg-dev libgif-dev \  
libssl-dev libyaml-dev libsqlite3-dev libleveldb-dev \  
libmysqlclient-dev \  
ruby ruby-dev curl && \  
EIIO_VER=0.5.6; \  
NV_VER=2.2.0; \  
OTAMA_VER=0.7.5; \  
curl -L https://github.com/nagadomi/eiio/archive/v${EIIO_VER}.tar.gz | tar zxv
-C /tmp && \  
cd /tmp/eiio-${EIIO_VER}; \  
./autogen.sh && ./configure && make && make install && ldconfig && \  
cd ..; rm -rf eiio-${EIIO_VER} && \  
curl -L https://github.com/nagadomi/nv/archive/v${NV_VER}.tar.gz | tar zxv -C
/tmp && \  
cd /tmp/nv-${NV_VER}; \  
./autogen.sh && ./configure && make && make install && ldconfig && \  
cd ..; rm -rf nv-${NV_VER} && \  
curl -L https://github.com/nagadomi/otama/archive/v${OTAMA_VER}.tar.gz | tar
zxv -C /tmp && \  
cd /tmp/otama-${OTAMA_VER}; \  
./autogen.sh && ./configure \--enable-mysql && make && make install &&
ldconfig && \  
cp -pr examples/rpc/ /opt/otamarpc && \  
cd ..; rm -rf otama-${OTAMA_VER} && \  
gem install bundler && \  
cd /opt/otamarpc && bundle install && \  
apt-mark manual libpng3 libjpeg62-turbo libgif4 libssl1.0.0 libyaml-0-2
libsqlite3-0 libleveldb1 libmysqlclient18 libgomp1 && \  
apt-get purge -y \--auto-remove gcc g++ make autoconf automake libtool \  
libpng-dev libjpeg-dev libgif-dev \  
libssl-dev libyaml-dev libsqlite3-dev libleveldb-dev \  
libmysqlclient-dev \  
ruby-dev && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 4568  
WORKDIR /opt/otamarpc  
CMD ["/usr/local/bin/thin", "start", "-p", "4568", "-P", "./thin.pid"]  

