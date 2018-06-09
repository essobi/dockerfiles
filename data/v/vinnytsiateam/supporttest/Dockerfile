FROM ubuntu:14.04  
MAINTAINER Yuriy Grigortsevich <GrigortsevichYuriy@gmail.com>  
  
# Install Deps  
RUN apt-get update \  
&& apt-get install -y \  
postgresql-9.3 \  
postgresql-contrib \  
php5-fpm \  
php5-pgsql \  
nginx  
  
# Copy files  
COPY dumps/countries.sql /tmp  
COPY etc/postgresql/9.3/main/* /etc/postgresql/9.3/main/  
COPY entrypoint.sh /  
COPY phppgadmin /usr/share/nginx/html/phppgadmin  
COPY etc/nginx/sites-available/* /etc/nginx/sites-available/  
  
# Configure postgres  
RUN service postgresql start \  
&& psql -U postgres -c "CREATE USER support WITH SUPERUSER PASSWORD
'support';" \  
&& psql -U postgres -c "CREATE DATABASE application WITH OWNER=support;" \  
&& psql -U postgres "application" < /tmp/countries.sql  
  
# Configure nginx  
RUN rm -rf /etc/nginx/sites-enabled/* \  
&& ln -s /etc/nginx/sites-available/phppgadmin /etc/nginx/sites-enabled/  
  
# Define ports  
# EXPOSE 80  
CMD /entrypoint.sh  

