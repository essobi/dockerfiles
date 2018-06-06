FROM ruby:2.4.1-slim  
  
# Install basic packages  
RUN apt-get update && apt-get install -y apt-utils curl apt-transport-https
build-essential git wget  
  
# Add NodeJS Repo  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
# Add Yarn Repo  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# Install Our Application Deps  
RUN apt-get update && apt-get install -y postgresql-client libpq-dev sqlite3
libsqlite3-dev yarn nodejs fontconfig imagemagick cron  
  
RUN npm install -g phantomjs-prebuilt  
  
ENV app /app  
RUN mkdir $app  
WORKDIR $app  
  
CMD bundle exec puma -p 3000 -C config/puma.rb  
EXPOSE 3000  

