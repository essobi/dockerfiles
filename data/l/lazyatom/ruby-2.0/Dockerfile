FROM lazyatom/ubuntu:latest  
MAINTAINER james@lazyatom.com  
  
RUN add-apt-repository -y ppa:brightbox/ruby-ng-experimental  
RUN apt-get update -qq && apt-get install -y ruby2.0 ruby2.0-dev build-
essential libpq-dev git-core libxml2-dev libc6-dev libssl-dev libmysql++-dev
libsqlite3-dev libreadline6-dev zlib1g-dev libyaml-dev  
RUN gem install -v 1.5.2 bundler  

