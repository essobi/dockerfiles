FROM ubuntu:14.04  
MAINTAINER DROUET Frederic <dev+docker@tarpoon.org>  
  
ENV HOME /root  
  
# Install some useful or needed tools  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -qq update && apt-get -q -y upgrade  
RUN apt-get -q -y install git-core curl zlib1g-dev build-essential libssl-dev
libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev
libcurl4-openssl-dev python-software-properties  
RUN apt-get -q -y autoremove  
RUN apt-get -q -y autoclean  
  
# Install RBENV  
WORKDIR /root  
RUN git clone git://github.com/sstephenson/rbenv.git $HOME/.rbenv  
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> $HOME/.bashrc  
RUN echo 'eval "$($HOME/.rbenv/bin/rbenv init -)"' >> $HOME/.bashrc  
RUN exec $SHELL  
  
RUN git clone git://github.com/sstephenson/ruby-build.git
$HOME/.rbenv/plugins/ruby-build  
RUN echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >>
$HOME/.bashrc  
RUN exec $SHELL  
  
# Install Ruby 2.1.1  
RUN $HOME/.rbenv/bin/rbenv install 2.1.2  
RUN $HOME/.rbenv/bin/rbenv global 2.1.2  
RUN $HOME/.rbenv/shims/ruby -v  
RUN echo "gem: --no-ri --no-rdoc" > $HOME/.gemrc  
  
# Install Bundler  
RUN $HOME/.rbenv/shims/gem install bundler  
RUN $HOME/.rbenv/shims/gem update --system  
RUN $HOME/.rbenv/bin/rbenv rehash  
  
# Install Grok Debugger  
RUN git clone https://github.com/nickethier/grokdebug.git /opt/grokdebug  
WORKDIR /opt/grokdebug  
RUN $HOME/.rbenv/shims/gem update  
RUN $HOME/.rbenv/shims/bundle update  
RUN $HOME/.rbenv/bin/rbenv rehash  
  
# Start Grok Debugger  
#ENTRYPOINT cd /opt/grokdebug; nohup $HOME/.rbenv/shims/rackup -p 80  
ADD grok.sh /grok.sh  
RUN chmod 755 /grok.sh  
CMD ["/grok.sh"]  
  
EXPOSE 80  

