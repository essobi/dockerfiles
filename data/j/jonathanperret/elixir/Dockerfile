FROM buildpack-deps:jessie  
  
MAINTAINER Jonathan Perret <jonathan@ut7.fr>  
  
ENV LC_ALL C.UTF-8  
RUN curl -sSL https://packages.erlang-solutions.com/erlang-
solutions_1.0_all.deb -o erlang-solutions_1.0_all.deb \  
&& DEBIAN_FRONTEND=noninteractive dpkg -i erlang-solutions_1.0_all.deb \  
&& rm -f erlang-solutions_1.0_all.deb  
  
COPY elixir-pins /etc/apt/preferences.d/  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
erlang-dev \  
erlang-nox \  
erlang-src \  
elixir  
  
RUN mix local.hex --force && \  
mix local.rebar --force  
  
CMD ["iex"]  

