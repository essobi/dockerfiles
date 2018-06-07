FROM elixir:latest  
  
MAINTAINER Kenta knt01222@gmail.com  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
RUN mix archive.install
https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez --force  
RUN mix local.hex --force  
RUN apt-get install postgresql -y  
RUN apt-get install inotify-tools -y  

