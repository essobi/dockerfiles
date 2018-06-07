FROM ubuntu:14.04  
ENV LANG en_US.utf8  
ENV MIX_ENV test  
  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y wget  
  
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb &&
sudo dpkg -i erlang-solutions_1.0_all.deb  
  
RUN apt-get update -y && \  
apt-get install -y erlang elixir rebar nodejs sqlite3 && \  
apt-get clean  
  
RUN mix local.hex --force  

