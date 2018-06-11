FROM elixir:1.4.5  
ENV LC_ALL=C.UTF-8  
ENV MIX_ENV=test  
ENV PGDATA=/etc/postgresql/9.4/main/  
ENV POSTGRES_HOST=127.0.0.1  
WORKDIR /tmp/dockerfile  
RUN wget https://deb.nodesource.com/gpgkey/nodesource.gpg.key -O
/tmp/dockerfile/nodesource.gpg.key && \  
wget https://github.com/ohjames/smell-baron/releases/download/v0.4.2/smell-
baron -O /usr/local/bin/smell-baron && \  
chmod +x /usr/local/bin/smell-baron && \  
echo "deb http://deb.nodesource.com/node_6.x jessie main" | tee
/etc/apt/sources.list.d/nodesource.list && \  
apt-key add nodesource.gpg.key && \  
apt-get update && \  
apt-get install -y nodejs build-essential libtool autoconf git postgresql
postgresql-contrib && \  
curl https://sh.rustup.rs -sSf | sh -s -- -y && \  
mkdir /var/run/postgresql/9.4-main.pg_stat_tmp && \  
chown postgres:postgres /var/run/postgresql/9.4-main.pg_stat_tmp && \  
mix local.hex --force && mix local.rebar --force && \  
sed -i 's:ssl = true:ssl = false:' /etc/postgresql/*/main/postgresql.conf  
WORKDIR /srv/  
ENTRYPOINT [ "/usr/local/bin/smell-baron", "runuser", "-u", "postgres",
"/usr/lib/postgresql/9.4/bin/postgres", "---", "-f" ]  
CMD [ "mix", "test" ]  

