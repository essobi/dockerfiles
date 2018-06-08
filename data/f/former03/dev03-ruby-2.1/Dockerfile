FROM former03/dev03-debian-wheezy  
MAINTAINER Christian Simon <simon@swine.de>  
# Install dependecies  
RUN apt-get -y install gawk libreadline6-dev zlib1g-dev libssl-dev libyaml-dev
libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev automake libtool
bison pkg-config libffi-dev  
# Download/Install Ruby  
RUN cd /usr/local/ && curl
https://rvm.io/binaries/debian/7/x86_64/ruby-2.1.0.tar.bz2 | tar xfvj -
--strip-components=1  
# Install bundler  
RUN gem install bundler  

