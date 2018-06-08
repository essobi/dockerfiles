FROM zooniverse/passenger:base-passenger4  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get -y -q install build-essential
libsqlite3-dev libcurl3 libxml2 libxslt1-dev libcurl4-gnutls-dev git-core
mysql-client libmysqlclient-dev imagemagick libmagickwand-dev memcached zlib1g
zlib1g-dev wget libyaml-dev bison libssl-dev libreadline6-dev autoconf
subversion curl && \  
wget -q -O ruby-1.8.7-p370.tar.gz http://cache.ruby-
lang.org/pub/ruby/1.8/ruby-1.8.7-p370.tar.gz && \  
tar xvf ruby-1.8.7-p370.tar.gz && \  
rm ruby-1.8.7-p370.tar.gz && \  
cd ruby-1.8.7-p370 && \  
./configure && make && make install && \  
cd .. && rm -rf ruby-1.8.7-p370 && \  
update-alternatives --install /usr/bin/ruby ruby /usr/local/bin/ruby 99 && \  
wget http://production.cf.rubygems.org/rubygems/rubygems-1.8.22.tgz && \  
tar -xvzf rubygems-1.8.22.tgz && \  
cd rubygems-1.8.22 && \  
ruby setup.rb && \  
cd .. && rm -rf rubygems-1.8.22.tgz rubygems-1.8.22 && \  
update-alternatives --install /usr/bin/gem gem /usr/local/bin/gem 99 && \  
gem update \--system 1.7.2 && \  
gem install bundler  

