FROM former03/dev03-debian-wheezy  
MAINTAINER Christian Simon <simon@swine.de>  
# Install dependecies  
RUN apt-get -y install gawk libreadline6-dev zlib1g-dev libssl-dev libyaml-dev
libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev automake libtool
bison pkg-config libffi-dev  
# Download/Compile/Install/Remove_Sources Ruby  
RUN mkdir -p /usr/src/ruby/ && cd /usr/src/ruby/ && curl http://cache.ruby-
lang.org/pub/ruby/1.8/ruby-1.8.7-p374.tar.gz | tar xfz - --strip-components=1
&& ./configure --enable-shared && make && make install && rm -rf /usr/src/ruby  
# Install Rubygems  
RUN mkdir -p /usr/src/rubygems/ && cd /usr/src/rubygems/ && curl
http://production.cf.rubygems.org/rubygems/rubygems-2.0.14.tgz | tar xfz -
--strip-components=1 && ruby setup.rb && rm -r /usr/src/rubygems  
# Install bundler  
RUN gem install bundler  

