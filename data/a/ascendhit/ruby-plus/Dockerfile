FROM ruby:2.4.1  
MAINTAINER Dru Jensen <drujensen@gmail.com>  
  
# update package manager  
RUN apt-get update -qq  
  
# developer tools  
RUN apt-get install -y build-essential git vim tmux curl netcat  
  
# install nodejs packages  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
# install yarn packages  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN echo "deb http://packages.linuxmint.com debian import" >>
/etc/apt/sources.list  
  
RUN apt-get update -qq  
  
# install other libraries  
RUN apt-get install -y libxml2-dev libxslt1-dev libssl-dev \  
libpq-dev libmysqlclient-dev libsqlite3-dev libdbus-glib-1-2  
  
# install nodejs and yarn  
RUN apt-get install -y nodejs yarn  
  
# install browsers for testing  
RUN apt-get install -y --force-yes xvfb firefox chromium imagemagick  

