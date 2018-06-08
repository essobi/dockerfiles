FROM perrystallings/ubuntu-python3.5.2:latest  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
memcached \  
postgresql \  
postgresql-contrib && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /etc/redis && \  
mkdir /var/redis && \  
mkdir /var/log/redis && \  
mkdir /setup && \  
mkdir /apps && \  
mkdir /apps/logs && \  
mkdir /apps/files  
  
COPY ./setup/redis.conf /etc/init.d/redis_6379  
COPY ./setup/redis-supervisor.conf /etc/supervisor/conf.d/  
COPY ./setup/create_user.sql /setup/  
  
RUN service postgresql start && \  
sudo -u postgres createuser --superuser root && \  
psql -U root -d postgres -a -f /setup/create_user.sql

