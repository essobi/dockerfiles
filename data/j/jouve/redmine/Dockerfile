FROM redmine:3.4.5  
COPY Gemfile.local .  
  
RUN buildDeps=' \  
gcc \  
g++ \  
make \  
uuid-dev \  
xz-utils \  
' \  
&& set -ex \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo "$RAILS_ENV:" > ./config/database.yml \  
&& echo " adapter: mysql2" >> ./config/database.yml \  
&& mv Gemfile.lock.mysql2 Gemfile.lock \  
&& bundle install --without development test \  
&& mv Gemfile.lock Gemfile.lock.mysql2 \  
&& rm ./config/database.yml \  
&& apt-get purge -y --auto-remove $buildDeps  
  
COPY additional_environment.rb config/  
  
COPY config.ru ./  
  
RUN sed -i -e 's/passenger)/passenger|puma)/' /docker-entrypoint.sh  
  
CMD ["puma", "--workers", "2", "--threads", "0:8", "--port", "3000"]  

