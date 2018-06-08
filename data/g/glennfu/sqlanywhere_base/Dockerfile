# https://hub.docker.com/r/danpmelo/sqlanywhere/  
FROM danpmelo/sqlanywhere:17.0  
EXPOSE 80  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install software-properties-
common  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install build-essential
libsqlite3-dev libcurl3 libxml2 libxslt1-dev libcurl4-gnutls-dev git-core
mysql-client libmysqlclient-dev imagemagick libmagickwand-dev memcached libpq-
dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install wget libreadline-dev  
  
# Install our specified version of Ruby  
RUN wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.3.tar.gz  
RUN tar xvzf ruby-2.3.3.tar.gz  
WORKDIR ruby-2.3.3  
RUN ./configure  
RUN make  
RUN make install  
  
RUN gem install bundler --no-ri --no-rdoc  

