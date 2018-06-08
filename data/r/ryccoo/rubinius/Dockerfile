FROM ryccoo/rvm:latest  
MAINTAINER Richard Ludvigh "https://github.com/Ryccoo  
  
# WELL THERE ARE STILL TROUBLES INSTALLING RBX THROUGH RVM, SO LETS JUST DO IT
MANUALLY  
  
ENV RBX_VERSION 2.3.0  
ENV SHELL /bin/bash  
ENV HOME /root  
  
# Generate and set UTF-8 locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get update  
RUN apt-get install -y wget ruby-dev make automake  
RUN apt-get install -y gcc g++ flex bison llvm-dev zlib1g-dev libyaml-dev \  
libssl-dev libgdbm-dev libreadline-dev libncurses5-dev  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN gem install bundler  
RUN wget -O rubinius-release-$RBX_VERSION.tar.bz2
https://s3.amazonaws.com/releases.rubini.us/rubinius-$RBX_VERSION.tar.bz2  
RUN tar -xjf rubinius-release-$RBX_VERSION.tar.bz2  
RUN rm rubinius-release-$RBX_VERSION.tar.bz2  
RUN cd rubinius-$RBX_VERSION && \  
bundle install && \  
./configure --prefix=/opt/rubies/rubinius-$RBX_VERSION && \  
rake build && \  
sudo rake install  
  
ENV PATH /opt/rubies/rubinius-$RBX_VERSION/bin:$PATH  
RUN rm -rf /tmp/* /var/tmp/*

