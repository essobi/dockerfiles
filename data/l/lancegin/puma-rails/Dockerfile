# Specify the Base Image  
FROM ubuntu  
  
# Set the Author information  
MAINTAINER Gin Lance <gin.lance.inside@hotmail.com>  
  
# Some ENV variables  
ENV RUBY_VERSION 2.3.0  
ENV RECV_KEYS 409B6B1796C275462A1703113804BB82D39DC0E3  
ENV RAILS_SERVER 4.2.6  
ENV RAILS_APP_NAME rails_demo  
ENV PUMA_GEM "gem 'puma', '~> 2.3.2'"  
  
# Install some dependenciesfor Ruby  
# && Intsall Ruby via rvm  
# && Install bundler and rails  
# && Install nginx and puma  
RUN /bin/bash -c 'apt-get update && apt-get install -y \  
git-core \  
curl \  
zlib1g-dev \  
build-essential \  
libssl-dev \  
libreadline-dev \  
libyaml-dev \  
libsqlite3-dev \  
sqlite3 \  
libxml2-dev \  
libxslt1-dev \  
libcurl4-openssl-dev \  
python-software-properties \  
libffi-dev \  
libgdbm-dev \  
libncurses5-dev \  
automake \  
libtool \  
bison \  
libffi-dev \  
nodejs \  
nginx \  
&& gpg --keyserver hkp://keys.gnupg.net --recv-keys "$RECV_KEYS" \  
&& curl -sSL https://get.rvm.io | bash -s stable \  
&& source /etc/profile.d/rvm.sh \  
&& echo "source /etc/profile.d/rvm.sh" >> ~/.bashrc \  
&& rvm install "$RUBY_VERSION" \  
&& rvm use "$RUBY_VERSION" --default \  
&& ruby -v \  
&& type ruby \  
&& gem -v \  
&& type gem \  
&& gem install bundler \  
&& gem install rails -v $RAILS_SERVER \  
&& rails -v \  
&& type rails \  
&& cd /home \  
&& rails new $RAILS_APP_NAME --skip-bundle \  
&& cd $RAILS_APP_NAME \  
&& sed -i "s/rubygems.org/gems.ruby-china.org/g" Gemfile \  
&& echo "$PUMA_GEM" >> Gemfile \  
&& bundle config build.puma --with-opt-dir=/usr/local/opt/openssl \  
&& bundle '  
  
# Create a mount point  
VOLUME ['/home']  
  
# Set the default port of container  
EXPOSE 3000  

