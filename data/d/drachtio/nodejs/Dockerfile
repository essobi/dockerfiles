FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get -y --quiet --force-yes upgrade \  
&& apt-get install -y --no-install-recommends ca-certificates gcc g++ make
build-essential git autoconf automake wget curl libtool libtool-bin python
libssl-dev libkrb5-dev \  
&& cd /usr/local/src \  
&& wget http://nodejs.org/dist/v6.10.2/node-v6.10.2.tar.gz \  
&& tar xvf node-v6.10.2.tar.gz && cd node-v6.10.2 && ./configure && make &&
make install \  
&& npm install npm -g \  
&& apt-get purge -y --quiet --force-yes --auto-remove ca-certificates gcc g++
make build-essential autoconf automake curl libtool libtool-bin python \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ \  
&& rm -Rf /var/log/* \  
&& rm -Rf /var/lib/apt/lists/* \  
&& cd /usr/local/src \  
&& rm -Rf * \  
&& mkdir /app  

