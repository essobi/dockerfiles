FROM elixir:1.4  
# Install MySQL client from Debian repos  
# -> https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 5072E1F5 && \  
echo 'deb http://repo.mysql.com/apt/debian/ jessie mysql-5.7' >
/etc/apt/sources.list.d/mysql.list && \  
apt-get update && \  
apt-get install -y git rsync openssh-client mysql-client && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mix local.hex --force && \  
mix local.rebar --force  
  

