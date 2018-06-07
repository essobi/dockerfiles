FROM stevedomin/erlang:17.5  
MAINTAINER Steve Domin <steve@stevedomin.com>  
  
RUN apt-get update && \  
apt-get install locales && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen  
  
ENV LC_ALL="en_US.UTF-8"  
# Erlang Solutions Jessie's repo doesn't have Elixir package :(  
RUN echo "deb http://packages.erlang-solutions.com/debian wheezy contrib" >>
/etc/apt/sources.list  
RUN wget http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc &&
apt-key add erlang_solutions.asc  
  
RUN apt-get update && apt-get install -y \  
elixir=1.0.4-1  
  
CMD ["iex"]  

