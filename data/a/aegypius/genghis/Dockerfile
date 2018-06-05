FROM ruby:2-slim  
  
RUN buildDeps=' \  
autoconf \  
bison \  
gcc \  
make \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& gem install --no-ri --no-rdoc \  
bson_ext:1.9.2 \  
genghisapp:2.3.11 \  
&& apt-get purge --yes --auto-remove $buildDeps  
  
EXPOSE 5000  
CMD /usr/local/bundle/bin/genghisapp --no-launch --foreground --port=5000
--servers ${DB_PORT_27017_TCP_ADDR}:${DB_PORT_27017_TCP_PORT}/${DB_NAME}  

