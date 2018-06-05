FROM elixir:1.6  
ENV PHOENIX_VERSION 1.3.0  
RUN mix local.hex --force  
RUN mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phx_new-$PHOENIX_VERSION.ez  
RUN mix local.rebar --force  

