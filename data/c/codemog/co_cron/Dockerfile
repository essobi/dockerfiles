FROM ubuntu:14.04  
MAINTAINER Daniel Trone "daniel.trone@state.co.us"  
ADD . .  
  
RUN apt-get update && apt-get install -y wget curl && \  
curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash - && \  
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt trusty-pgdg main" >>
/etc/apt/sources.list' && \  
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo
apt-key add - && \  
apt-get update && \  
apt-get install -y nodejs postgresql-9.4-postgis-2.1 postgis zip php5
php5-pgsql  
  
# If you need npm, don't use a base tag  
RUN npm install  
  
CMD ["nodejs", "index.js"]

