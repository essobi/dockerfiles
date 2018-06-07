FROM ubuntu:13.10  
MAINTAINER Bert Chang "https://github.com/lazywei"  
# We use bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update  
RUN apt-get install -y git curl zlib1g-dev build-essential libssl-dev
libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev
libcurl4-openssl-dev python-software-properties autoconf ruby bison  
  
RUN git clone https://github.com/sstephenson/rbenv.git .rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
.rbenv/plugins/ruby-build  
  
RUN echo 'export PATH="/.rbenv/bin:$PATH"' >> /.bashrc  
RUN echo 'eval "$(rbenv init -)"' >> /.bashrc  

