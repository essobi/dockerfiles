FROM debian:wheezy  
RUN apt-get update -qq  
RUN apt-get install wget -qqy  
RUN apt-get autoremove  
  
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999
postgres  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
RUN gpg --keyserver keys.gnupg.net --recv-keys ACCC4CF8  
RUN gpg --export \--armor ACCC4CF8|apt-key add -  
  
RUN apt-get install -y postgresql postgresql-contrib postgresql-common  
RUN apt-get clean  
  
RUN echo "/etc/init.d/postgresql start && exit 0" > /etc/rc.local  
  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
  
USER postgres  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.1/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.1/main/postgresql.conf  
  
EXPOSE 5432  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
CMD ["/usr/lib/postgresql/9.1/bin/postgres", "-D",
"/var/lib/postgresql/9.1/main", "-c",
"config_file=/etc/postgresql/9.1/main/postgresql.conf"]

