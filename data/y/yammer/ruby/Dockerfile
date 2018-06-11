FROM ubuntu:14.04  
MAINTAINER Brian Morton "bmorton@yammer-inc.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y curl ca-certificates git build-essential libtool
autoconf libtcmalloc-minimal4  
  
# Install chruby  
ADD https://github.com/postmodern/chruby/archive/v0.3.8.tar.gz
/tmp/chruby.tar.gz  
RUN cd /tmp && tar -xzvf chruby.tar.gz  
RUN cd /tmp/chruby-0.3.8 && make install  
  
# Install ruby-install  
ADD https://github.com/postmodern/ruby-install/archive/master.tar.gz
/tmp/ruby-install.tar.gz  
RUN cd /tmp && tar -xzvf ruby-install.tar.gz  
RUN cd /tmp/ruby-install-master && make install  
  
RUN ruby-install ruby 2.3.5 -- --disable-install-rdoc --enable-shared
CFLAGS="-O3"  
  
RUN echo '[ -n "$BASH_VERSION" ] || [ -n "$ZSH_VERSION" ] || return' >>
/etc/profile.d/chruby.sh  
RUN echo 'source /usr/local/share/chruby/chruby.sh' >>
/etc/profile.d/chruby.sh  
RUN echo 'chruby ruby' >> /etc/profile.d/default_ruby.sh  
RUN echo "export LD_PRELOAD=/usr/lib/libtcmalloc_minimal.so.4:${LD_PRELOAD}"
>> /etc/profile.d/exports.sh  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN chruby-exec ruby -- gem install bundler  

