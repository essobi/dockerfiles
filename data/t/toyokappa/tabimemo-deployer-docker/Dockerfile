FROM toyokappa/aws-deployer-docker  
  
# ruby install  
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.4/ruby-2.4.1.tar.gz && \  
tar -zxvf ruby-2.4.1.tar.gz && \  
cd ruby-2.4.1 && \  
./configure --disable-install-doc && \  
make && \  
make install && \  
cd .. && \  
rm -r ruby-2.4.1 ruby-2.4.1.tar.gz  
  
RUN gem install bundler  

