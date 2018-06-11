FROM elixir:1.6.4  
RUN mkdir /wallet_ms  
COPY . /wallet_ms  
WORKDIR /wallet_ms  
  
# Install hex package manager  
RUN mix local.hex --force  
RUN mix archive.install
https://github.com/phoenixframework/archives/raw/master/phx_new.ez --force  
RUN mix local.rebar --force  
  
# getting dependencies  
RUN mix deps.get  
  
EXPOSE 4004  

