FROM ruby:2.3.4-slim  
  
ADD pgdg.list /etc/apt/sources.list.d/  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y wget \--no-install-recommends && \  
wget -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add \-
&& \  
apt-get update && \  
apt-get install -y postgresql-client-9.6 libpq-dev \--no-install-recommends &&
\  
apt-get install -y imagemagick libmagic-dev file \--no-install-recommends && \  
apt-get remove \--purge -y wget && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  

