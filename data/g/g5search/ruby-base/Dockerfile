FROM ruby:2.5.1  
  
MAINTAINER G5 DevOps <devops@getg5.com>  
  
# otherwise can see some encoding issues:  
# https://oncletom.io/2015/docker-encoding/  
ENV LANG=C.UTF-8  
  
RUN \  
# For newer version of Node, since the official Debian packaged version is too
old to run Yarn.  
# source: https://github.com/nodesource/distributions#installation-
instructions  
curl -sL https://deb.nodesource.com/setup_10.x | bash - && \  
# Add apt source for Yarn, which is too new to have a useful version in apt  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
# Download latest manifests from official and custom sources  
apt-get update && \  
apt-get install -y \  
# ffi gem, which you might need if you use something that calls C  
libffi-dev \  
# for postgres gem  
libpq-dev \  
# pretty much no asset pipeline without this. Note this is from a custom  
# source, not from the official Debian pacakages (too old for yarn).  
nodejs \  
# required for rails 5 asset pipeline  
yarn && \  
# clean up apt cache  
rm -rf /var/lib/apt/lists/*  
  
# updated SSL root certs. The CACHE_BUSTER is to allow us to re-generate these  
# images periodically and have them correctly pull new certificates even when  
# there are no meaningful changes in the Dockerfile. You have to bump the  
# CACHE_BUSTER if you haven't changed anything in this file above this line.  
RUN CACHE_BUSTER=1 apt-get install -y ca-certificates  
  
ENV RACK_ENV="production" \  
RAILS_ENV="production" \  
RAILS_LOG_TO_STDOUT="true" \  
RAILS_SERVE_STATIC_FILES="true"  

