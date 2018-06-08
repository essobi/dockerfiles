FROM alpine  
  
# Install language and support things  
RUN apk upgrade && apk update \  
&& apk add \  
# Basic dependencies  
build-base git \  
# Erlang Deps  
erlang-dev erlang-ssl erlang-inets \  
erlang-edoc erlang-eunit erlang-tools erlang-common-test \  
erlang-crypto erlang-syntax-tools erlang-parsetools \  
# Finally Elixir  
elixir  
  
  
# Phoenix and other mix things  
RUN mix local.hex --force && \  
mix local.rebar --force && \  
mix archive.install --force
"https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez"  
  
# Working directory  
ENV INSTALL_PATH /home/app  
WORKDIR $INSTALL_PATH  
  
# Copy files needed for configuring Mix  
COPY .coverignore ./  
  
# Copy dependencies and compile  
COPY mix.exs mix.lock ./  
RUN MIX_ENV=test mix do deps.get, compile  
  
COPY . .  
  
EXPOSE 4000  
CMD mix phoenix.server  

