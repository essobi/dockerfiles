FROM debian:wheezy  
MAINTAINER 'CenturyLink Labs'  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
libreadline6-dev \  
zlib1g-dev \  
libssl-dev \  
libffi-dev \  
libyaml-dev \  
libgdbm-dev \  
wget  
  
RUN wget -nv http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz && \  
tar xfz ruby-2.1.2.tar.gz && \  
cd ruby-2.1.2 && \  
./configure --disable-install-doc && \  
make && \  
make install && \  
cd .. && \  
rm -r ruby-2.1.2 ruby-2.1.2.tar.gz  
  
RUN echo 'gem: --no-document' >> /.gemrc  
  
RUN wget -nv http://production.cf.rubygems.org/rubygems/rubygems-2.3.0.tgz &&
\  
tar xfz rubygems-2.3.0.tgz && \  
cd rubygems-2.3.0 && \  
ruby setup.rb && \  
cd .. && \  
rm -r rubygems-2.3.0 rubygems-2.3.0.tgz  
  
RUN gem install --no-document bundler  

