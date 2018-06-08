FROM jupyter/minimal-notebook  
  
MAINTAINER Evandro Dutra <evandro.eld@gmail.com>  
  
USER root  
  
RUN apt-get update && apt-get install -yq \  
autoconf \  
libssl-dev \  
libtool \  
libffi-dev \  
libzmq-dev \  
libgdbm-dev \  
libmagickwand-dev \  
libreadline-dev \  
ruby \  
ruby-dev \  
git \  
&& apt-get clean && cd ~ \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /usr/bin/libtoolize /usr/bin/libtool  
  
RUN gem install --no-document \  
rbczmq \  
gruff \  
rmagick \  
gnuplot \  
rubyvis \  
rbczmq \  
cztop \  
iruby  
  
USER $NB_USER  
  
RUN iruby register --force  

