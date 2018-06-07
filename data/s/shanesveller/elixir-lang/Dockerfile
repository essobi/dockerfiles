FROM gliderlabs/alpine:3.3  
  
MAINTAINER Shane Sveller <shane@shanesveller.com>  
  
RUN apk-install \  
ca-certificates \  
erlang-asn1 \  
erlang-crypto \  
erlang-dev \  
erlang-eunit \  
erlang-inets \  
erlang-parsetools \  
erlang-public-key \  
erlang-ssl \  
erlang-syntax-tools \  
erlang-xmerl \  
g++ \  
gcc \  
make  
  
RUN wget -O /tmp/elixir.zip https://github.com/elixir-
lang/elixir/releases/download/v1.2.3/Precompiled.zip && \  
mkdir -p /opt/elixir && \  
unzip -d /opt/elixir /tmp/elixir.zip && \  
rm -f /tmp/elixir.zip  
  
ENV LANG=en_US.UTF-8
PATH=/opt/elixir/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN mix local.hex --force && \  
mix local.rebar --force  
  
WORKDIR /usr/src/app  

