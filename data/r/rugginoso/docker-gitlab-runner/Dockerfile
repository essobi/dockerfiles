FROM ubuntu:14.04  
MAINTAINER Cantiere Creativo Team <info@cantierecreativo.net>  
ENV PATH /root/.rbenv/bin:/root/.rbenv/shims:$PATH  
ENV CONFIGURE_OPTS --disable-install-doc  
  
# bash as default shell  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# system packages  
RUN apt-get update  
RUN apt-get install -y --force-yes build-essential git curl zlib1g-dev libssl-
dev libreadline-dev libyaml-dev libxml2-dev libxslt-dev libffi-dev xvfb
libqt4-dev libqt4-webkit default-jre  
RUN apt-get clean  
  
# rbenv  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN echo 'export PATH="$HOME/.rbenv/bin:$HOME/.rbenv/shims:$PATH"' >>
/root/.bashrc  
RUN echo 'eval "$(rbenv init -)"' >> /root/.bashrc  
RUN echo 'gem: --no-rdoc --no-ri' >> /root/.gemrc  
ADD ./ruby-versions.txt /root/ruby-versions.txt  
RUN bash -l -c 'for version in $(cat /root/ruby-versions.txt); do rbenv
install $version && rbenv global $version && rbenv rehash && gem install
bundler; done'  
  
# nvm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.25.3/install.sh | bash  
ADD ./node-versions.txt /root/node-versions.txt  
RUN bash -l -c 'for version in $(cat /root/node-versions.txt); do source
/root/.nvm/nvm.sh && nvm install $version; done'  
  

