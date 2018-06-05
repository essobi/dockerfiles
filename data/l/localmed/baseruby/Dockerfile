FROM localmed/baseimage:1.1  
MAINTAINER LocalMed <developers@localmed.com>  
  
# Ruby  
RUN cd /tmp && \  
wget -q http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.3.tar.gz && \  
tar xzf ruby-2.2.3.tar.gz && \  
cd ruby-2.2.3 && \  
./configure --enable-shared --prefix=/usr && \  
make && \  
make install && \  
cd .. && \  
rm -rf ruby-2.2.3* && \  
cd ..  

