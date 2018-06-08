FROM ubuntu:latest  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && apt-get dist-upgrade -y \  
&& apt-get install -y build-essential curl git postgresql-client \  
&& curl -o /tmp/erlang.deb http://packages.erlang-solutions.com/erlang-
solutions_1.0_all.deb \  
&& dpkg -i /tmp/erlang.deb \  
&& rm /tmp/erlang.deb \  
&& (curl -sL https://deb.nodesource.com/setup_7.x | bash) \  
&& apt-get update \  
&& apt-get install -y elixir erlang-dev erlang-parsetools nodejs \  
&& apt-get clean -y \  
&& rm -rf /var/cache/apt/*  
  
RUN mix local.hex --force \  
&& mix local.rebar --force  
  
ENV PHOENIX_VERSION 1.2.1  
RUN mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phoenix_new-$PHOENIX_VERSION.ez  
  
WORKDIR /code  

