FROM alvarolizama/elixir:1.5.1-master  
MAINTAINER Alvaro Lizama Molina <contact@alvarolizama.net>  
RUN apk --no-cache add -U nodejs nodejs-npm inotify-tools libsass libsass-dev
sassc \  
&& mix archive.install
https://github.com/phoenixframework/archives/raw/master/phx_new.ez --force  

