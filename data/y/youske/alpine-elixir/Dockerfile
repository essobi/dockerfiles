# Alpine Linux elixir  
  
FROM youske/alpine-stdmachine:base  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.stdmachine.description="alpine elixir image" \  
com.stdmachine.role="elixir image"  
  
RUN apk add elixir erlang erlang-tools erlang-stdlib erlang-ssh erlang-mnesia
erlang-crypto erlang-syntax-tools erlang-kernel erlang-compiler --no-cache &&
\  
apk add build-base musl-dev linux-headers --no-cache -t buildpack && \  
apk del buildpack --purge --no-cache && rm -rf /tmp/* /var/cache/apk/*  

