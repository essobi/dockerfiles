FROM ruby:2.3  
# FROM ruby:2.4  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
autoconf ghostscript gsfonts imagemagick jhead jpegoptim libbz2-dev
libfreetype6-dev libjpeg-dev libjpeg-turbo-progs libtiff-dev libxml2 nodejs
npm optipng pkg-config postgresql-client \  
gifsicle pngquant \  
&& ln --symbolic /usr/bin/nodejs /usr/bin/node \  
&& npm install --global \  
svgo uglify-js \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV DISCOURSE_VERSION=1.7.2 \  
RAILS_ENV=production \  
RUBY_GC_MALLOC_LIMIT=90000000 \  
RUBY_GLOBAL_METHOD_CACHE_SIZE=131072 \  
DISCOURSE_DB_HOST=postgres \  
DISCOURSE_REDIS_HOST=redis \  
DISCOURSE_SERVE_STATIC_ASSETS=true  
  
WORKDIR /usr/src/app  
RUN curl -sfSL
https://github.com/discourse/discourse/archive/v${DISCOURSE_VERSION}.tar.gz \  
| tar -zx --strip-components=1 -C /usr/src/app \  
&& bundle config build.nokogiri --use-system-libraries  
  
# # works on ruby:2.4 with this:  
# RUN bundle config frozen 0 \  
# && echo "gem 'json', git: 'https://github.com/flori/json.git', branch:
'v1.8'" >> Gemfile \  
# && bundle update  
RUN bundle install --deployment --without test \--without development  
  
EXPOSE 3000  
CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]  

