FROM elixir:1.5-alpine  
LABEL maintainer Iago S. <146050u54[at]gmail[dot]com>  
  
# Installing Phoenix  
RUN set -xe \  
&& mix local.hex --force \  
&& mix local.rebar --force \  
&& mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phx_new.ez  
  
# Installing Node, NPM and Yarn  
RUN apk add --update --no-cache \  
inotify-tools \  
nodejs-current \  
nodejs-current-npm \  
yarn \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /usr/share/html  
  
EXPOSE 4000  
CMD ["mix", "phx.server"]  
  
# vim: noet ts=4 sw=4  

