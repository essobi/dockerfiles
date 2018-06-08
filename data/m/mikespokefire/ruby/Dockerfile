FROM mikespokefire/ruby-install:v0.5.0  
MAINTAINER Michael Smith <mike@spokefire.co.uk>  
  
RUN ruby-install ruby 2.1.6 -- --disable-install-rdoc  
  
ENV PATH /opt/rubies/ruby-2.1.6/bin:$PATH  
RUN gem install bundler --no-ri --no-rdoc  

