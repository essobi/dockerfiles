FROM phusion/baseimage  
MAINTAINER catenthusiast <rahul@keeranoor.com>  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV SHELL /bin/bash  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y wget make  
RUN apt-get install -y git gcc g++ automake flex bison ruby1.9.1-dev llvm-dev
zlib1g-dev libyaml-dev libssl-dev libgdbm-dev libreadline-dev libncurses5-dev  
  
#Install chruby  
RUN wget -O chruby-0.3.8.tar.gz
https://github.com/postmodern/chruby/archive/v0.3.8.tar.gz  
RUN tar -xzvf chruby-0.3.8.tar.gz  
RUN cd chruby-0.3.8/ && make install  
RUN echo 'source /usr/local/share/chruby/chruby.sh' >> ~/.bashrc  
RUN echo 'source /usr/local/share/chruby/auto.sh' >> ~/.bashrc  
  
#Install Rubinius  
RUN gem install bundler  
RUN wget -O rubinius-release-2.2.10.tar.bz2
http://releases.rubini.us/rubinius-2.2.10.tar.bz2  
RUN tar -xjf rubinius-release-2.2.10.tar.bz2  
RUN cd rubinius-2.2.10 && bundle install && ./configure
--prefix=/opt/rubies/rubinius-2.2.10 && rake build && rake install  
  
#Add Rubinius to path as default Ruby  
ENV PATH
/opt/rubies/rubinius-2.2.10/bin/:/opt/rubies/rubinius-2.2.10/gems/bin/:$PATH  

