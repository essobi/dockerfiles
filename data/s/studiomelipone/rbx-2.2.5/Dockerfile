FROM phusion/baseimage:0.9.8  
MAINTAINER Loïc Guitaut <loic@studiomelipone.eu>  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Install tools & libs to compile everything  
RUN apt-get update && apt-get install -y build-essential libssl-dev
libreadline-dev wget && apt-get clean  
  
# Install imagemagick  
RUN apt-get install -y imagemagick libmagick++-dev libmagic-dev && apt-get
clean  
  
# Install nodejs  
RUN apt-get install -y python-software-properties  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y nodejs && apt-get clean  
  
# Install ruby-install  
RUN apt-get install -y git-core && apt-get clean  
RUN wget -O - https://github.com/postmodern/ruby-install/archive/v0.4.0.tar.gz
| tar xvzf - && cd ruby-install-0.4.0 && make install && cd .. && rm ruby-
install-0.4.0 -rf  
  
# Install rubinius 2.2.5  
RUN ruby-install rbx 2.2.5 && apt-get clean  
ENV PATH /opt/rubies/rbx-2.2.5/bin:/opt/rubies/rbx-2.2.5/gems/bin:$PATH  
RUN gem install --no-rdoc --no-ri rubysl-tracer rake bundler  
RUN sed -i
'1s/^/PATH=\/opt\/rubies\/rbx-2.2.5\/bin:\/opt\/rubies\/rbx-2.2.5\/gems\/bin:$PATH\n/'
/root/.bashrc  
  
# Install memcached  
RUN apt-get install -y memcached && apt-get clean  
ADD memcached.sh /etc/my_init.d/  
  
# Install Redis  
RUN apt-get install -y redis-server && apt-get clean  
ADD redis.sh /etc/my_init.d/  
  
# Install PG  
RUN apt-get install -y postgresql libpq-dev && apt-get clean  
ADD postgresql.sh /etc/my_init.d/  
  
# custom rc.local to setup env at runtime  
ADD rc.local /etc/rc.local  
  
# Enable insecure key to easily use ssh  
RUN /usr/sbin/enable_insecure_key  
  
# Pry config file to have a good looking console  
ADD pryrc /root/.pryrc  
  
WORKDIR /rails_app  
ADD rails.sh /root/  
CMD ["/sbin/my_init", "/root/rails.sh"]  
  
# Clean up downloaded packages  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

