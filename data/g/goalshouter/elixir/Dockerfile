FROM alpine:3.7  
RUN apk --update --no-cache add elixir erlang-crypto erlang-ssl erlang-syntax-
tools erlang-parsetools erlang-runtime-tools build-base git erlang-xmerl  
RUN mix local.hex --force && mix local.rebar  
  
ENV PORT=80 MIX_ENV=prod  
EXPOSE $PORT  
  
RUN mkdir /app  
WORKDIR /app  

