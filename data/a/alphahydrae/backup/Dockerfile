FROM ruby:2.5.1-slim  
  
WORKDIR /usr/src/app  
  
COPY Gemfile Gemfile.lock /usr/src/app/  
  
RUN apt-get update && \  
apt-get install -y build-essential cron && \  
apt-get install -y wget && \  
echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' >>
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add \- && \  
apt-get update && \  
apt-get install -y postgresql-client-9.6 && \  
apt-get remove -y wget && \  
bundle install && \  
apt-get remove -y build-essential && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
COPY fs/ /  
  
ENV BACKUP_DATA_PATH="/var/lib/backups" \  
BACKUP_TMP_PATH="/tmp/backup"  
  
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]  

