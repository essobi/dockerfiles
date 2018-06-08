FROM revinate/ruby:2.3-ubuntu  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends build-essential git git-core \  
curl wget xvfb firefox sqlite3 unzip scrot zlib1g-dev libssl-dev \  
libreadline-dev libyaml-dev libsqlite3-dev libxml2-dev libxslt1-dev \  
libcurl4-openssl-dev libffi-dev libmysqlclient-dev  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["irb"]  

