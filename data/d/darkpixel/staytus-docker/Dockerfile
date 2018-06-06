FROM ruby:alpine  
RUN apk add --update --no-cache libc-dev make g++ nodejs tzdata curl mariadb-
dev gettext  
RUN gem install bundler  
WORKDIR /  
RUN curl https://codeload.github.com/adamcooke/staytus/zip/master --output
master.zip; unzip master.zip && mv staytus-master app; rm master.zip  
WORKDIR /app  
RUN bundle install --deployment --without development:test  
  
COPY docker-start-v2.sh /app/docker-start-v2.sh  
COPY config/database.example.yml /app/config/database.example.yml  
COPY config/environment.example.yml /app/config/environment.example.yml  
ENTRYPOINT /app/docker-start-v2.sh  
EXPOSE 5000  

