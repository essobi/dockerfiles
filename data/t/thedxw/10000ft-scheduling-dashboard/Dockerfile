FROM ruby:2.4.2  
MAINTAINER dxw <rails@dxw.com>  
  
# install base packages  
RUN apt-get update -y -q2 \  
&& apt-get upgrade -y -q2 \  
&& apt-get -y -q2 install \  
nodejs \  
&& apt-get -y -q2 clean  
  
# create application user  
RUN addgroup --gid 999 --quiet app \  
&& adduser --gid 999 --uid 999 --quiet --disabled-password app  
  
# set rails environment  
ARG RAILS_ENV  
ENV RAILS_ENV=${RAILS_ENV:-production}  
ENV RACK_ENV=${RAILS_ENV:-production}  
# create and use application home  
ENV APP_NAME scheduling-dashboard  
ENV APP_PATH /srv/scheduling-dashboard  
RUN mkdir -p $APP_PATH  
WORKDIR $APP_PATH  
# bundle ruby gems to create a static dependency tree  
USER app  
ENV GEM_PATH /usr/local/bundle  
RUN gem install --quiet bundler  
  
USER root  
COPY Gemfile $APP_PATH/Gemfile  
COPY Gemfile.lock $APP_PATH/Gemfile.lock  
RUN chown -R app:app $APP_PATH  
  
USER app  
# bundle ruby gems based on the current environment, default to production  
RUN \  
if [ "$RAILS_ENV" = "production" ]; then \  
bundle install --without development test --jobs 25 --retry 3; \  
else \  
bundle install --jobs 25 --retry 3; \  
fi  
  
USER root  
  
# add project files  
COPY . $APP_PATH  
# compile assets for production  
RUN bundle exec rake assets:precompile  
  
# make app own the project files  
RUN chown -R app:app $APP_PATH  
# run application as the app user  
USER app  
  
# expose public assets as a volume, this needs to happen after any changes to
the filesystem  
VOLUME ["/srv/scheduling-dashboard/public"]  
  
EXPOSE 3000  
CMD ["bundle", "exec", "puma"]  

