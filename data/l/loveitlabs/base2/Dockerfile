FROM ubuntu:14.04.3  
MAINTAINER LoveItLabs <team@loveitlabs.io>  
  
ENV TERM vt100  
RUN apt-get update --fix-missing  
RUN apt-get upgrade -y  
  
# Install ruby dependencies  
RUN apt-get install -y wget curl \  
build-essential git git-core \  
zlib1g-dev libssl-dev libreadline-dev \  
libyaml-dev \  
libsqlite3-dev sqlite3 libxml2-dev \  
libxslt1-dev \  
libmysqlclient-dev \  
libffi-dev \  
libffi6 \  
supervisor  
  
  
RUN apt-get update  
  
RUN wget -nv http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.5.tar.gz && \  
tar xfz ruby-2.1.5.tar.gz && \  
cd ruby-2.1.5 && \  
./configure --disable-install-doc && \  
make && \  
make install && \  
cd .. && \  
rm -r ruby-2.1.5 ruby-2.1.5.tar.gz  
  
RUN wget -nv http://production.cf.rubygems.org/rubygems/rubygems-2.4.6.tgz &&
\  
tar xfz rubygems-2.4.6.tgz && \  
cd rubygems-2.4.6 && \  
ruby setup.rb && \  
cd .. && \  
rm -r rubygems-2.4.6 rubygems-2.4.6.tgz  
  
RUN gem install --no-document bundler  

