FROM ubuntu:15.04  
MAINTAINER david@codegram.com  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev \  
libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev \  
libxslt1-dev libcurl4-openssl-dev python-software-properties \  
libffi-dev wget libmysqlclient-dev imagemagick libmagickwand-dev \  
libpq-dev ghostscript && \  
rm -rf /var/lib/apt/lists*  
  
# Install ruby 2.2.4  
RUN cd && wget http://ftp.ruby-lang.org/pub/ruby/2.2/ruby-2.2.4.tar.gz && \  
tar -xzvf ruby-2.2.4.tar.gz && cd ruby-2.2.4/ && \  
./configure && make && make install && rm -rf ruby-2.2.4  
  
# Install node 5  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash && \  
apt-get install -y nodejs  
  
# Install phantomjs 2.1.1  
RUN curl -OLk
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN mv phantomjs-2.1.1-linux-x86_64 /usr/local/share  
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/local/bin  
  
# Install bundler  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc && gem install bundler  
  

