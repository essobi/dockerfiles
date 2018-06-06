FROM ubuntu:15.04  
MAINTAINER Linki <linki+docker.com@posteo.de>  
  
# update the package list  
RUN apt-get update  
  
# install build-essential because we need to compile some native extensions  
RUN apt-get install -y build-essential  
  
# install zlib development headers for nokogiri to build  
#  
# http://www.nokogiri.org/tutorials/installing_nokogiri.html  
#  
RUN apt-get install -y zlib1g-dev  
  
# we use a database for our backend, so let's add a couple of them  
RUN apt-get -y install libpq-dev libmysql++-dev sqlite3 libsqlite3-dev  
  
# newer versions of openproject use angular-js, so we want node and npm  
RUN apt-get -y install nodejs npm  
  
# allow the nodejs binary to be called via node (this should be fixed somehow)  
RUN ln -s nodejs /usr/bin/node  
  
# install git in order to checkout gems defined by git urls  
RUN apt-get -y install git-core  
  
# install ruby 2.1 with development extensions  
RUN apt-get install -y ruby2.1 ruby2.1-dev  
  
# install our beloved bundler  
RUN gem install bundler  
  
# install foreman to run our app server at the end  
RUN gem install foreman  
  
# clone openproject's default branch  
RUN git clone \--depth 1 https://github.com/opf/openproject.git /app  
  
# set the working directory to the app  
WORKDIR /app  
  
# use a database.yml that takes its values from an environment variables  
COPY ./files/database.yml /app/config/database.yml  
  
# add some gems specific to this image build  
COPY ./files/Gemfile.local /app/Gemfile.local  
  
# a helper script to create/seed or migrate the database  
COPY ./files/setup_database /app/bin/setup_database  
  
# create an unprivileged user that owns the code and will run the app server  
RUN useradd -m app  
RUN chown -R app:app /app  
  
# switch to the openproject user from now on  
USER app  
  
# install all ruby dependencies via bundler into a local path  
RUN bundle install --path ./vendor/bundle  
  
# install all node dependencies via npm  
RUN npm install  
  
# precompile all assets  
#  
# openproject currently requires a database when compiling assets  
# we fake one by providing an sqlite db location for this command only  
#  
# note, asset precompilation needs to be done in production, otherwise icon
images are missing  
#  
RUN RAILS_ENV=production SECRET_TOKEN=foobar
DATABASE_URL=sqlite3://db/ignore_me.sqlite3 \  
bundle exec rake assets:precompile  
  
# expose the app server's port  
EXPOSE 3000  
# setup the database and launch the rails server unless another command is
given  
CMD bin/setup_database && HOST=0.0.0.0 PORT=3000 foreman start web  

