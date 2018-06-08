FROM ubuntu:14.04  
MAINTAINER Oliver Letterer <oliver.letterer@sparrow-labs.de>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y wget curl \  
build-essential git git-core \  
zlib1g-dev libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3
libxml2-dev libxslt1-dev \  
&& apt-get clean  
  
RUN cd /tmp &&\  
wget -O ruby-install-0.4.3.tar.gz https://github.com/postmodern/ruby-
install/archive/v0.4.3.tar.gz &&\  
tar -xzvf ruby-install-0.4.3.tar.gz &&\  
rm ruby-install-0.4.3.tar.gz && \  
cd ruby-install-0.4.3/ &&\  
make install && \  
rm -rf /tmp/ruby-install-0.4.3/  
  
RUN ruby-install ruby 2.1.2  
ENV PATH /opt/rubies/ruby-2.1.2/bin:$PATH  
RUN echo "gem: --no-document" > ~/.gemrc  
  
RUN gem install bundler  

