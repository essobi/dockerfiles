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
  
# Install ruby-build  
RUN apt-get install -y git-core && apt-get clean  
RUN git clone https://github.com/sstephenson/ruby-build.git && cd ruby-build
&& ./install.sh  
  
# Install ruby 2.1.0  
ENV CONFIGURE_OPTS --disable-install-rdoc  
RUN ruby-build 2.1.0 /usr/local  
RUN gem install bundler  
  
# Install memcached  
RUN apt-get install -y memcached && apt-get clean  
ADD memcached.sh /etc/my_init.d/  
  
# Install Redis and make sure to not run it daemonized  
RUN apt-get install -y redis-server && apt-get clean  
ADD redis.sh /etc/my_init.d/  
  
# Install PG  
RUN apt-get install -y postgresql libpq-dev && apt-get clean  
ADD postgresql.sh /etc/my_init.d/  
  
# custom rc.local to setup env at runtime  
ADD rc.local /etc/rc.local  
  
# Enable insecure key to easily use ssh  
RUN /usr/sbin/enable_insecure_key  
  
WORKDIR /rails_app  
ADD rails.sh /root/  
CMD ["/sbin/my_init", "/root/rails.sh"]  
  
# Clean up downloaded packages  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

