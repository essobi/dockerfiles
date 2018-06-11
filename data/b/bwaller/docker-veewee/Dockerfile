FROM ubuntu:14.04  
MAINTAINER Björn Waller bjorn@waller.nu  
  
RUN apt-get update && apt-get install -y \  
libxslt1-dev \  
libxml2-dev \  
zlib1g-dev \  
build-essential \  
ruby \  
ruby-dev \  
libvirt-dev \  
curl \  
git  
  
RUN export LC_CTYPE=en_US.UTF-8  
  
#Install RVM  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -sSL https://get.rvm.io | bash -s stable --ruby  
RUN . /etc/profile && \  
/usr/local/rvm/scripts/rvm install ruby  
  
RUN /usr/local/rvm/scripts/rvm use ruby@veewee --create  
  
RUN gem install bundler \  
ruby-libvirt  
  
RUN git clone https://github.com/jedi4ever/veewee.git  
  
#Fix bug in veewee.gemspec  
RUN sed -i -e '59,61d' /veewee/veewee.gemspec  
  
RUN cd /veewee && \  
bundle install  
  
CMD ["gem", "server"]  

