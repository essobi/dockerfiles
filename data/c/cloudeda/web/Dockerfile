# MAINTAINER pinewong <pinewong@163.com>  
# DOCKER-VERSION 1.12.6  
#  
# Dockerfile for the auroraWS of Aurora Platform.  
# Usage: docker pull cloudeda/web  
  
FROM ruby:2.3.0  
MAINTAINER pinewong <pinewong@163.com>  
  
# see update.sh for why all "apt-get install"s have to stay as one long line  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
# see http://guides.rubyonrails.org/command_line.html#rails-dbconsole  
RUN apt-get update && apt-get install -y mysql-client postgresql-client
sqlite3 --no-install-recommends && rm -rf /var/lib/apt/lists/*  
# Libzmq3-dev, for MySQL  
RUN apt-get update && apt-get install -y libzmq3-dev --no-install-recommends
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install bundler --no-doc --no-ri  
  
# Workspace  
RUN \  
mkdir -p /app/source && \  
mkdir -p /app/design && \  
mkdir -p /app/log && \  
mkdir -p /app/local && \  
mkdir -p /app/local/cache && \  
mkdir -p /app/local/pids && \  
mkdir -p /app/local/sessions && \  
mkdir -p /app/local/sockets  

