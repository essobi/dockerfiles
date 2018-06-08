FROM node:4.4.4  
MAINTAINER serenader xyslive@gmail.com  
  
ENV THIMBLE_DB_PUBLISH publish  
ENV THIMBLE_DB_OAUTH webmaker_oauth_test  
ENV THIMBLE_DB_USER thimble  
ENV THIMBLE_DB_PASSWORD password  
ENV THIMBLE_DB_PORT 5432  
ENV THIMBLE_DB_HOST 127.0.0.1  
RUN apt-get update && apt-get install -y build-essential postgresql-9.4
postgresql-client-9.4 nginx \  
&& apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& service postgresql start \  
&& su - postgres -c "psql -c \"CREATE USER $THIMBLE_DB_USER WITH PASSWORD
'$THIMBLE_DB_PASSWORD'\"" \  
&& su - postgres -c "psql -c \"CREATE DATABASE $THIMBLE_DB_PUBLISH OWNER
$THIMBLE_DB_USER\"" \  
&& su - postgres -c "psql -c \"CREATE DATABASE $THIMBLE_DB_OAUTH OWNER
$THIMBLE_DB_USER\"" \  
&& su - postgres -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE
$THIMBLE_DB_PUBLISH to $THIMBLE_DB_USER\"" \  
&& su - postgres -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE
$THIMBLE_DB_OAUTH to $THIMBLE_DB_USER\""  
  
WORKDIR /var/thimble  
  
RUN git clone \--depth 1 https://github.com/mozilla/brackets.git \  
&& cd brackets && git submodule update --init \  
&& npm install && npm run build  
  
RUN git clone \--depth 1 https://github.com/mozilla/thimble.mozilla.org.git \  
&& cd thimble.mozilla.org && cp env.dist .env \  
&& npm install && npm run localize  
  
RUN git clone \--depth 1 https://github.com/mozilla/id.webmaker.org.git \  
&& cd id.webmaker.org && cp sample.env .env \  
&& npm install  
  
RUN git clone \--depth 1 https://github.com/mozilla/login.webmaker.org.git \  
&& cd login.webmaker.org && npm install && cp env.sample .env  
  
RUN git clone \--depth 1 https://github.com/mozilla/publish.webmaker.org.git \  
&& cd publish.webmaker.org && npm install && npm run env \  
&& npm install -g knex  
  
COPY start.sh /var/thimble/start.sh  
COPY default /etc/nginx/sites-enabled  
  
CMD ["/bin/bash", "/var/thimble/start.sh"]  

