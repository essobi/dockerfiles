FROM ruby:2.2.2  
  
RUN mkdir -p /usr/src/app /var/geminabox && \  
chown -R daemon:daemon /usr/src/app /var/geminabox && \  
usermod -d /usr/src/app daemon  
USER daemon  
WORKDIR /usr/src/app  
  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config \--global bin vendor/bin && \  
bundle config \--global path vendor/bundle && \  
bundle config \--global frozen 1  
ENV BUNDLE_APP_CONFIG vendor/bundle  
  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install --deployment  
COPY . /usr/src/app  
  
VOLUME /var/geminabox  
USER daemon  
EXPOSE 4567  
CMD ["bundle", "exec", "puma", "-p", "4567", "-e", "production"]

