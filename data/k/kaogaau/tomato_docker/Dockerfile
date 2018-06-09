# Dowload Ubuntu  
FROM ubuntu:16.04  
MAINTAINER Tomato <kaogaau@gmail.com>  
  
# Set The Locale  
RUN locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  
# Use Bash，No Dash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install Libary  
RUN apt-get update \  
&& apt-get install -y git curl libcurl3 libmysqlclient-dev debconf-utils vim \  
&& echo mysql-server mysql-server/root_password password 12345 | debconf-set-
selections \  
&& echo mysql-server mysql-server/root_password_again password 12345 |
debconf-set-selections \  
&& apt-get install -y mysql-server -o pkg::Options::="--force-confdef" -o
pkg::Options::="--force-confold" \--fix-missing \  
&& apt-get install -y net-tools --fix-missing \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Ruby/Rails/Bundler  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN /bin/bash -l -c "curl -L get.rvm.io | bash -s stable --rails"  
RUN /bin/bash -l -c "echo 'gem: --no-ri --no-rdoc' > ~/.gemrc"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
RUN /bin/bash -l -c "bundle config github.https true"  
RUN /bin/bash -l -c "source /usr/local/rvm/scripts/rvm"  
  
# Copy Tomato  
RUN mkdir /Tomato  
WORKDIR /Tomato  
COPY ./Tomato /Tomato  
  
# Bundle Install  
RUN /bin/bash -l -c "bundle install"  
  
# Create Database  
RUN /bin/bash -l -c "service mysql start" \  
&& /bin/bash -l -c "rake db:create" \  
&& /bin/bash -l -c "rake db:migrate" \  
&& /bin/bash -l -c "rake db:seed"  
  
# Start Mysql  
CMD service mysql start \  
&& /bin/bash -l -c "foreman start"  

