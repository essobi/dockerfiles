FROM quirky/baseimage  
MAINTAINER Micah Martin <micahlmartin@gmail.com>  
  
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz && \  
tar -zxvf ruby-2.1.2.tar.gz && \  
cd ruby-2.1.2 && \  
./configure --disable-install-doc && \  
make && \  
make install && \  
cd .. && \  
rm -r ruby-2.1.2 ruby-2.1.2.tar.gz && \  
echo 'gem: --no-document' > /usr/local/etc/gemrcdoc  

