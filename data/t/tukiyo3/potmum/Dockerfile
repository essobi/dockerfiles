FROM ruby:2.4.1-slim-jessie  
  
RUN apt-get update  
RUN apt-get install -y curl apt-transport-https gnupg git  
  
# nodejs v6  
RUN echo "deb https://deb.nodesource.com/node_6.x jessie main" >
/etc/apt/sources.list.d/nodesource.list  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
-  
RUN apt-get update  
RUN apt-get install -y nodejs  
  
# yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update  
RUN apt-get install -y yarn  
  
# build pkgs  
RUN apt-get install -y ruby-dev build-essential  
  
RUN git clone https://github.com/rutan/potmum.git /srv/potmum  
WORKDIR /srv/potmum  
  
# potmum  
RUN yarn install  
RUN gem install bundler  
RUN bundle config git.allow_insecure true  
RUN apt-get install -y libpq-dev libsqlite3-dev  
RUN bundle install --path vendor/bundle  
RUN apt-get install -y sqlite3  
RUN sed -i \  
-e "s@adapter: postgresql@<<: *default@g" \  
-e "s@url: <%= ENV\\['DATABASE_URL'\\] %>@database: db/production.sqlite3@g" \  
config/database.yml ;\  
RAILS_ENV=production bundle exec rake db:create db:migrate assets:precompile  
  
## see https://github.com/rutan/potmum  
ENV RAILS_ENV=production  
ENV COLOR_THEME="blue"  
ENV USE_ATTACHMENT_FILE=1  
#ENV ROOT_URL="http://localhost:3000"  
## see https://github.com/settings/developers  
ENV USE_GITHUB=1  
ENV GITHUB_KEY="XXXXXXXXXXXXXXXXXXXX"  
ENV GITHUB_SECRET="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  
EXPOSE 3000  
VOLUME /srv/potmum/db/  
VOLUME /srv/potmum/public/attachment_files/  
  
ENTRYPOINT SECRET_KEY_BASE=`rake secret` bundle exec puma -C config/puma.rb  

