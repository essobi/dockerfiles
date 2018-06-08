FROM elixir:1.6-alpine  
MAINTAINER sharils <sharils@users.noreply.github.com>  
  
RUN set -xe && \  
  
# Here’s the command to install Hex  
mix local.hex --force && \  
  
# Phoenix  
mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phx_new.ez && \  
  
# node.js (>= 5.0.0)  
apk add \--no-cache nodejs nodejs-npm && \  
  
# mix ecto.create  
mix local.rebar --force && \  
  
# inotify-tools (for linux users)  
apk add \--no-cache inotify-tools  

