#  
# Fulcrum, project management tool.  
#  
# Commit used for the build:  
#
https://github.com/malclocke/fulcrum/commit/e0f2e2b1e6176685f7981407f36b9d5271dd6627  
#  
# See README.md to understand why this file ends up this way!  
#  
FROM ubuntu:saucy  
  
MAINTAINER Eric Platon <eplaton@gmx.com>  
  
RUN apt-get update  
RUN apt-get install -y git ruby2.0 ruby2.0-dev build-essential libpq-dev
libsqlite3-dev  
  
RUN git clone git://github.com/malclocke/fulcrum.git  
RUN cd fulcrum && \  
git checkout e0f2e2b1e6176685f7981407f36b9d5271dd6627 && \  
echo "gem 'therubyracer'" >> Gemfile && \  
echo "gem 'sqlite3'" >> Gemfile && \  
gem install bundler sqlite3 --no-rdoc --no-ri && \  
bundle install --no-cache --without development test travis  
RUN cd fulcrum && \  
bundle install --deployment --no-cache --without development test travis  
RUN cd fulcrum && \  
DB=sqlite bundle exec rake fulcrum:setup db:setup  
  
VOLUME ["/fulcrum/db"]  
  
EXPOSE 3000  
WORKDIR /fulcrum  
CMD bundle exec rails server -e production  
  

