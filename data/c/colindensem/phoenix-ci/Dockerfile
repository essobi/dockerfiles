FROM trenpixster/elixir:latest  
MAINTAINER Colin Densem @colindensem  
  
ARG NODE_MAJOR_VERSION=6  
  
  
RUN apt-get update && \  
apt-get install -y curl mysql-client && \  
  
# Add Node.js from nodesource  
curl -sL https://deb.nodesource.com/setup_${NODE_MAJOR_VERSION}.x | bash - &&
\  
apt-get install -y nodejs && \  
  
# Clean up  
apt-get purge -y curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Install local Elixir hex and rebar  
RUN /usr/local/bin/mix local.hex --force && \  
/usr/local/bin/mix local.rebar --force  

