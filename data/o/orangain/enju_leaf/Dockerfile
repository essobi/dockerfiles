FROM ubuntu:xenial  
  
# See: https://github.com/next-l/enju_leaf/wiki/Install  
RUN apt-get update && apt-get install -y \  
ruby ruby-dev \  
imagemagick libicu-dev zlib1g-dev unzip \  
openjdk-8-jre-headless git libxslt1-dev build-essential nodejs redis-server \  
libpq-dev file cron \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'gem: --no-rdoc --no-ri' >> ~/.gemrc  
RUN gem install bundler  
  
COPY enju_leaf/Gemfile* /enju_leaf/  
  
WORKDIR /enju_leaf  
  
RUN bundle config without test development doc  
RUN bundle install  
  
ENV DB_HOST=db  
ENV DB_USERNAME=postgres  
ENV DB_PASSWORD=password  
ENV DB_DATABASE=enju_production  
ENV RAILS_ENV=production  
ENV RAILS_SERVE_STATIC_FILES=true  
  
COPY enju_leaf/ /enju_leaf/  
  
RUN rake assets:precompile  
  
RUN mv config/schedule.rb config/schedule.rb.orig && \  
echo "env :PATH, ENV['PATH']" > config/schedule.rb && \  
echo "env :DB_HOST, ENV['DB_HOST']" >> config/schedule.rb && \  
echo "env :DB_USERNAME, ENV['DB_USERNAME']" >> config/schedule.rb && \  
echo "env :DB_PASSWORD, ENV['DB_PASSWORD']" >> config/schedule.rb && \  
echo "env :DB_DATABASE, ENV['DB_DATABASE']" >> config/schedule.rb && \  
cat config/schedule.rb.orig >> config/schedule.rb && \  
rm config/schedule.rb.orig  
  
RUN bundle exec whenever --update-crontab  
  
COPY Procfile docker-entrypoint.sh is_db_empty.rb password_reset.patch ./  
  
RUN (cd `bundle show enju_leaf`/app/views/devise/mailer && \  
patch -p1 < /enju_leaf/password_reset.patch)  
  
VOLUME ["/enju_leaf/log", "/enju_leaf/config"]  
EXPOSE 3000  
ENTRYPOINT ["./docker-entrypoint.sh"]  
CMD ["bundle", "exec", "foreman", "start"]  

