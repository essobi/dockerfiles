FROM ruby:2.4.2-jessie  
  
MAINTAINER df1228@gmail.com  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get update -qq && apt-get install -y --no-install-recommends build-
essential nodejs libpq-dev && \  
curl -o- -L https://yarnpkg.com/install.sh | bash  
  
RUN mkdir -p /app  
  
WORKDIR /app  
  
COPY Gemfile Gemfile.lock ./  
RUN gem install bundler && \  
bundle config mirror.https://rubygems.org https://gems.ruby-china.org && \  
bundle install --jobs 4 --retry 5 --deployment --no-cache --without
development test  
  
ENV PATH /root/.yarn/bin:$PATH  
  
# Copy dependencies for Node.js and instance the packages.  
# Again, being separate means this will cache.  
COPY package.json yarn.lock ./  
RUN yarn install  
RUN npm rebuild node-sass --force  
  
# Set Rails to run in production  
ENV RAILS_ENV production  
ENV RACK_ENV production  
  
  
# Copy the main application.  
COPY . ./  
  
COPY docker/database.yml ./config/database.yml  
  
# Precompile Rails assets (plus Webpack)  
RUN bundle exec rake assets:precompile  
  
EXPOSE 5000  
ENV PORT 5000  
VOLUME /app/public  
  
# ENTRYPOINT ['bin/rails']  
CMD bundle exec puma -C config/puma.rb  

