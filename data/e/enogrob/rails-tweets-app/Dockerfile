FROM ruby:2.3.0  
MAINTAINER enogrob@gmail.com  
  
# Install MongoDB and yajl-tools.  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \  
&& echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.2.list \  
&& apt-get update \  
&& apt-get install -y build-essential nodejs mongodb-org yajl-tools --no-
install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Define mountable directories.  
VOLUME ["/data/db"]  
  
# Deploy Rails App  
WORKDIR /usr/src/app  
COPY Gemfile* ./  
RUN gem install bundler && bundle install --jobs 20 --retry 5  
COPY . ./  
  
# Expose ports.  
# - 27017: process  
# - 28017: http  
EXPOSE 27017  
EXPOSE 28017  
EXPOSE 3000  
# The main command to run when the container starts. Also  
# tell the Rails dev server to bind to all interfaces by  
# default.  
CMD service mongod start && bundle exec rails server -b 0.0.0.0  

