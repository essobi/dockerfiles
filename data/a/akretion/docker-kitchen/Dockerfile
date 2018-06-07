FROM ubuntu-debootstrap:14.04  
  
ADD Gemfile /Gemfile  
  
RUN apt-get -y update  
  
RUN apt-get -yqq install python-software-properties software-properties-common
&& \  
apt-get -yqq install build-essential && \  
apt-get -yqq install curl git libxml2-dev libgecode-dev autoconf  
  
# add brightbox's repo, for ruby2.2  
RUN apt-add-repository ppa:brightbox/ruby-ng  
RUN apt-get -y update  
  
# install ruby2.2  
RUN apt-get -y install ruby2.2 ruby2.2-dev  
  
RUN /usr/bin/gem install bundler --no-ri --no-rdoc  
RUN /usr/local/bin/bundle install  

