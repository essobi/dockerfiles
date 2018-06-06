FROM ericraio/ruby:latest  
  
ENV RAILS_ENV production  
  
RUN apt-get update -qq -y  
  
#################################  
# Symlinking Nodejs for ubuntu  
# -- http://stackoverflow.com/questions/26320901/cannot-install-nodejs-usr-
bin-env-node-no-such-file-or-directory  
#################################  
RUN apt-get install -qq -y nodejs  
RUN apt-get install -qq -y npm  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
#################################  
# Rails  
#################################  
  
  
  
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release
-cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'  
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key
add -  
RUN apt-get update  
  
RUN apt-get install -qq -y imagemagick libmagickcore-dev libmagickwand-dev
libjpeg-dev libpng-dev libtiff-dev libwebp-dev libpq-dev postgresql
postgresql-contrib  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ONBUILD RUN mkdir /app  
ONBUILD WORKDIR /app  
  
ONBUILD ADD Gemfile /app/Gemfile  
ONBUILD ADD Gemfile.lock /app/Gemfile.lock  
  
ONBUILD RUN bundle install --deployment  
  
ONBUILD ADD . /app  
  
ONBUILD RUN mkdir tmp/sockets -p  
ONBUILD RUN mkdir tmp/pids -p  
ONBUILD RUN mkdir tmp/cache -p  

