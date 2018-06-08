FROM elixir:1.6  
ENV PHOENIX_VERSION 1.3.0  
RUN apt-get update  
RUN apt-get install -y erlang-dev erlang-parsetools  
  
RUN mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phx_new-1.3.0.ez  
  
RUN elixir -v  

