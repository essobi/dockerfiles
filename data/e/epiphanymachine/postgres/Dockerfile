# Run postgres server for local development  
# docker volume create -d local hint-pg-data  
# docker run -d \  
# --restart always \  
# -v hint-pg-data:/var/lib/postgresql \  
# -p 5555:5432 \  
# --name hint-pg \  
# epiphanymachine/postgres  
FROM ubuntu:16.04  
MAINTAINER EpiphanyMachine@gmail.com  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl \  
apt-transport-https \  
python-software-properties \  
software-properties-common  
  
# Add PGP keys to verify packages (psql, heroku)  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 \  
&& (curl -L https://cli-assets.heroku.com/apt/release.key | apt-key add -)  
  
# Add repositories  
RUN add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt
./" \  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
# Add install PostgreSQL 9.3 and heroku  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
postgresql-9.3 \  
postgresql-client-9.3 \  
postgresql-contrib-9.3 \  
heroku  
  
# Install the aptible toolbelt
https://www.aptible.com/support/toolbelt/#download-ubuntu  
RUN curl -o aptible-cli.deb https://omnibus-aptible-
toolbelt.s3.amazonaws.com/aptible/omnibus-aptible-
toolbelt/master/132/pkg/aptible-
toolbelt_0.8.4%2B20170125114552%7Eubuntu.16.04-1_amd64.deb \  
&& dpkg -i aptible-cli.deb \  
&& apt-get install -f \  
&& rm aptible-cli.deb  
  
# Run the rest of the commands as the `postgres` user created by the
`postgres-9.3` package  
USER postgres  
  
# Create a PostgreSQL role named `docker` with `docker` as the password  
# and then create a database `docker` owned by the `docker` role.  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\  
createdb -O docker docker  
  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
  
# And add `listen_addresses` to `/etc/postgresql/9.3/main/postgresql.conf`  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
# Expose the PostgreSQL port  
EXPOSE 5432  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
# Set the default command to run when starting the container  
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D",
"/var/lib/postgresql/9.3/main", "-c",
"config_file=/etc/postgresql/9.3/main/postgresql.conf"]  

