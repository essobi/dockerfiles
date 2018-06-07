FROM phusion/baseimage:0.9.16  
  
MAINTAINER jeff@csd.uwo.ca  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Install Ruby prerequisites  
RUN apt-get update -qq && \  
sudo apt-get install -y curl zlib1g-dev build-essential libssl-dev
libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev
libcurl4-openssl-dev libffi-dev libgdbm-dev software-properties-common && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Build Ruby  
RUN cd /tmp && \  
curl -Ls http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.0.tar.gz | tar -xz
&& \  
cd ruby-2.2.0 && \  
./configure --enable-shared --disable-install-doc && \  
make && \  
make install && \  
gem install bundler && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Set Ruby-specific environment variables  
ENV GEM_HOME /usr/local/lib/ruby/gems/2.2.0  
ENV GEM_PATH /usr/local/lib/ruby/gems/2.2.0  

