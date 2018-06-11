FROM turfmedia/ruby  
  
ENV POSTGRESQL_VERSION 9.4  
RUN mkdir -p /app  
WORKDIR /app  
  
# Add PostgreSQL Global Development Group apt source  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
RUN curl --silent http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-
key add -  
  
RUN packages=" \  
nodejs \  
postgresql-client-$POSTGRESQL_VERSION \  
libpq-dev libxml2-dev libxslt-dev \  
" \  
&& curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh &&
bash nodesource_setup.sh \  
&& apt-get update && apt-get install -y --no-install-recommends $packages \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV BUNDLE_GEMFILE=/app/Gemfile  
ONBUILD COPY Gemfile /app/  
ONBUILD COPY Gemfile.lock /app/  
ONBUILD RUN bundle install  
  
ONBUILD ADD . /app  
VOLUME /app  
EXPOSE 3000  
CMD ["rails", "server", "-b", "0.0.0.0"]  

