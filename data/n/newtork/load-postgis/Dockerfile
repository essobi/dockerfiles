FROM debian:jessie  
  
MAINTAINER newtork / Alexander Dümont <alexander_duemont@web.de>  
  
  
##########################################  
# #  
# Docker Build #  
# #  
##########################################  
  
#  
# USAGE  
# -----  
# docker pull newtork/load-postgis  
# docker build -t newtork/load-postgis .  
# docker run --rm --it newtork/load-postgis  
#  
# docker run -p 5432:5432 \--rm -it -v /local/database/dumps/:/restore
newtork/load-postgis  
  
  
##########################################  
# #  
# Build Settings / Environment #  
# #  
##########################################  
  
EXPOSE 5432  
  
  
WORKDIR /root/  
COPY run.sh /root/  
  
ARG POSTGRES_PW  
ENV POSTGRES_PW ${POSTGRES_PW:-postgres}  
  
  
##########################################  
# #  
# BUILD #  
# #  
##########################################  
  
  
#  
# Build-Process:  
# --------------  
#  
# 1) Update, download and install required packages, clear repo data
afterwards:  
# - postgis  
#  
# 2.1) Determine Version,  
# fix missing stat directory,  
# start postgres server.  
#  
# 2.2) Wait a second for the server being up and running,  
# set custom password for "postgres" user,  
# save custom password to local path and set security,  
# shutdown postgres server and wait another second.  
#  
# 2.3) Determine version again,  
# change authentication method of "postgres" from "peer" to "md5"  
# (making it possible for the user to connect from outside),  
# generally allow password based authentication of external connections,  
# make the server listen on all addresses - not only localhost.  
#  
#  
  
  
RUN echo "Updating and Download Dependencies..." && \  
apt-get -qqy update && \  
apt-get -qqy install postgis > /dev/null 2>&1 && \  
echo "Download Complete." && \  
rm -rf /var/lib/apt/lists/* && \  
echo "Cleared temporary data."  
  
RUN v="$(ls /etc/postgresql/)" && \  
echo "First start of PostgreSQL $v..." && \  
/bin/su - postgres -c "mkdir -p \"/var/run/postgresql/$v-main.pg_stat_tmp/\""
&& \  
/bin/su - postgres -c "/usr/lib/postgresql/$v/bin/postgres -D
/etc/postgresql/$v/main/" & \  
\  
sleep 1 && \  
/bin/su - postgres -c "pg_isready && psql -c \"ALTER USER postgres WITH
ENCRYPTED PASSWORD '$POSTGRES_PW';\"" && \  
echo "*:*:*:postgres:$POSTGRES_PW" > ~/.pgpass && chmod 600 ~/.pgpass && \  
pkill -SIGINT postgres && sleep 1 && \  
\  
v="$(ls /etc/postgresql/)" && \  
sed -i "s/^local\s*all\s*postgres\s*peer/local\tall\tpostgres\tmd5/"
/etc/postgresql/$v/main/pg_hba.conf && \  
printf "host\tall\tall\tall\tmd5\n" >> /etc/postgresql/$v/main/pg_hba.conf &&
\  
sed -i "s/^#listen_addresses = 'localhost'/listen_addresses = '*'/"
/etc/postgresql/$v/main/postgresql.conf  
  
  
ENTRYPOINT /root/run.sh  

