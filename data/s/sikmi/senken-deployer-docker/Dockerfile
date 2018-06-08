FROM sikmi/awseb-deployer-docker  
  
# ruby install  
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz && \  
tar -zxvf ruby-2.3.1.tar.gz && \  
cd ruby-2.3.1 && \  
./configure --disable-install-doc && \  
make && \  
make install && \  
cd .. && \  
rm -r ruby-2.3.1 ruby-2.3.1.tar.gz  
  
RUN gem install bundler  

