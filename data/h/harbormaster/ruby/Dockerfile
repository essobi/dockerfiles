FROM stackbrew/ubuntu:saucy  
MAINTAINER Sebastian Korfmann <korfmann.sebastian@gmail.com>  
  
ENV PATH /opt/rubies/ruby-2.1.1/bin/:$PATH  
  
RUN apt-get update && apt-get install -y \  
git \  
wget \  
make  
  
RUN wget -O ruby-install-0.4.1.tar.gz https://github.com/postmodern/ruby-
install/archive/v0.4.1.tar.gz && \  
tar -xzvf ruby-install-0.4.1.tar.gz && \  
cd ruby-install-0.4.1 && \  
make install && \  
rm -rf /ruby-install-0.4.1*  
  
RUN ruby-install ruby 2.1 \-- --disable-install-rdoc && \  
rm -rf /usr/local/src/ && \  
gem install bundler --no-rdoc --no-ri  

