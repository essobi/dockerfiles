FROM ruby:2.3.1  
MAINTAINER Sergei O. Udalov <sergei.udalov@gmail.com>  
  
ENV HOME /root  
  
RUN apt-get update -qq && apt-get install -y --force-yes build-essential \  
# Postgres \  
libpq-dev \  
# Nokogiri \  
libxml2-dev libxslt1-dev nodejs  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn nodejs unzip  
  
RUN mkdir -p /app  
WORKDIR /app  
  
ADD Gemfile* ./  
RUN bundle install --deployment --without development test  
  
ADD package.json ./  
ADD yarn.lock ./  
  
RUN yarn install  
  
ADD . ./  
  
ENV RAILS_ENV=production  
ENV DATABASE_URL=sqlite3:///db/production.sqlite3  
ENV SECRET_KEY_BASE=abc123  
RUN rake assets:precompile  
  
EXPOSE 80  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["web"]  

