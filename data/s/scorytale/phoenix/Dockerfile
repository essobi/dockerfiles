FROM scorytale/elixir  
  
MAINTAINER ScoryTale <developers@sportintown.com>  
  
RUN apk add --no-cache --update \  
nodejs nodejs-npm \  
imagemagick \  
erlang-xmerl  
  
RUN mix archive.install
https://github.com/phoenixframework/archives/raw/master/phx_new.ez --force  
  
EXPOSE 4000  
CMD ["mix", "phx.server"]  

