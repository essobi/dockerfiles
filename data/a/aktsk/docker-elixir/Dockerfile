FROM elixir:1.4-slim  
  
MAINTAINER Shinta Hatatani <shinta.hatatani@aktsk.jp>  
  
# debconf のエラーを抑制する  
ARG DEBIAN_FRONTEND=noninteractive  
  
# wget と curl だと wget の方が依存が少ない  
RUN apt-get update && apt-get install -y lsb-release wget && \  
wget http://dev.mysql.com/get/mysql-apt-config_0.8.0-1_all.deb && \  
dpkg -i mysql-apt-config_0.8.0-1_all.deb && \  
wget https://deb.nodesource.com/setup_6.x -O - | bash - && \  
apt-get install -y \--no-install-recommends gcc make mysql-community-client
nodejs rsync && \  
mix local.rebar --force && \  
mix local.hex --force && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  

