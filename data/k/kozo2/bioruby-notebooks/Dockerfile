FROM andrewosh/binder-base  
  
MAINTAINER Kozo Nishida <knishida@riken.jp>  
  
USER root  
  
# Add IRuby dependencies  
RUN apt-get update  
RUN apt-get install -y build-essential ruby ruby-dev libzmq3 libzmq3-dev
libtool autoconf automake && apt-get clean  
RUN ln -s /usr/bin/libtoolize /usr/bin/libtool # See
https://github.com/zeromq/libzmq/issues/1385  
  
RUN gem update --no-document --system && gem install --no-document iruby
rbczmq pry bio  
  
USER main  
  
RUN iruby register  

