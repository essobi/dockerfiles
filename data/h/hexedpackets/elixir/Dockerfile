FROM debian:jessie  
MAINTAINER William Huba <hexedpackets@gmail.com>  
  
RUN apt-get update && apt-get install -y curl wget locales git build-essential  
  
# Set the locale  
RUN echo "en_US UTF-8" > /etc/locale.gen && \  
locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8  
# Setup the erlang apt source  
RUN echo "deb http://packages.erlang-solutions.com/debian jessie contrib" >>
/etc/apt/sources.list && \  
wget http://packages.erlang-solutions.com/debian/erlang_solutions.asc && \  
apt-key add erlang_solutions.asc && \  
rm erlang_solutions.asc  
  
RUN apt-get update && \  
apt-get install -y erlang erlang-tools erlang-parsetools erlang-dev erlang-
eunit && \  
apt-get clean  
  
# Install Elixir  
ENV ELIXIR_VERSION 1.0.5  
RUN git clone https://github.com/elixir-lang/elixir.git && \  
cd elixir && \  
git checkout tags/v${ELIXIR_VERSION} && \  
make && make install && \  
cd .. && rm -rf elixir  
  
RUN mix local.hex --force && mix local.rebar --force  
CMD iex  

