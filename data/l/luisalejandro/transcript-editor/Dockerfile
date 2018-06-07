FROM dockershelf/debian:sid  
MAINTAINER Luis Alejandro Martínez Faneyth <luis@huntingbears.com.ve>  
  
ENV APPUSER="transuser" APPPROJECT="transproject" APPDBNAME="transdb"
APPDBPASS="transpass"  
RUN useradd -ms /bin/bash ${APPUSER}  
RUN apt-get update && apt-get install postgresql ruby ruby-dev make \  
gcc g++ bundler libc6-dev libpq-dev zlib1g-dev \  
patch git rails  
  
USER ${APPUSER}  
WORKDIR /home/${APPUSER}  
RUN git clone \--depth 1 https://github.com/LuisAlejandro/transcript-editor  
  
WORKDIR /home/${APPUSER}/transcript-editor  
RUN mkdir -p vendor/bundle  
RUN bundle install --path vendor/bundle  
  
RUN mv config/application.sample.yml config/application.yml  
RUN mv config/database.sample.yml config/database.yml  
RUN mv project/sample-project project/${APPPROJECT}  
  
RUN APPSECRET="$( rake secret )" \  
&& sed -i 's/SECRET_KEY_BASE:.*/SECRET_KEY_BASE: '${APPSECRET}'/g'
config/application.yml \  
&& sed -i 's/PROJECT_ID:.*/PROJECT_ID: '${APPPROJECT}'/g'
config/application.yml  
  
RUN sed -i 's/username: postgres/username: '${APPUSER}'/g' config/database.yml
\  
&& sed -i 's/password: password/password: '${APPDBPASS}'/g'
config/database.yml \  
&& sed -i 's/database: app_name/database: '${APPDBNAME}'/g'
config/database.yml \  
&& sed -i 's/username: user/username: '${APPUSER}'/g' config/database.yml  
  
USER postgres  
RUN service postgresql start \  
&& psql -c "CREATE ROLE ${APPUSER} LOGIN SUPERUSER INHERIT CREATEDB
CREATEROLE;" \  
&& psql -c "CREATE DATABASE ${APPDBNAME};" \  
&& psql -c "GRANT ALL PRIVILEGES ON DATABASE ${APPDBNAME} to ${APPUSER};" \  
&& psql -c "ALTER USER ${APPUSER} WITH PASSWORD '${APPDBPASS}';" \  
&& service postgresql stop  
  
USER root  
RUN service postgresql start && rake db:setup && service postgresql stop  
RUN service postgresql start && rake project:load["${APPPROJECT}"] && service
postgresql stop  
  
CMD service postgresql start && rails server -b 0.0.0.0

