FROM debian:jessie  
MAINTAINER Loïc Frering <loic.frering@gmail.com>  
  
# Configure sources  
RUN echo "deb http://packages.erlang-solutions.com/debian wheezy contrib" >
/etc/apt/sources.list.d/erlang-solutions.list  
RUN apt-key adv --fetch-keys http://packages.erlang-
solutions.com/debian/erlang_solutions.asc  
  
# Install common packages  
RUN apt-get update && apt-get install -y \  
curl \  
locales  
  
# Install Elixir  
RUN apt-get install -y \  
elixir=1.0.5-2 \  
erlang-dev  
  
# Install hex  
RUN mix local.hex --force  
RUN mix local.rebar --force  
  
# Set the locale  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
# Working directory  
WORKDIR /work  
  
# Default command  
CMD ["bash"]  

