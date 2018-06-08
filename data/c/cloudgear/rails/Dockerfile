FROM cloudgear/rails:ruby2.2  
MAINTAINER Georg Kunz, CloudGear <contact@cloudgear.net>  
  
RUN mkdir -p /usr/src/app && \  
useradd app --home /usr/src/app && \  
chown app:app -R /usr/src/app  
  
WORKDIR /usr/src/app  
  
ENV RACK_ENV production  
ENV PORT  3000  
  
ONBUILD USER app  
ONBUILD COPY Gemfile Gemfile.lock /usr/src/app/  
ONBUILD COPY Gemfile.lock /usr/src/app/  
ONBUILD RUN bundle install --deployment --without development test  
  
ONBUILD COPY . /usr/src/app  
# Fix file permissions because COPY does not honor USER
https://github.com/docker/docker/issues/6119  
ONBUILD USER root  
ONBUILD RUN chown app:app -R /usr/src/app  
ONBUILD USER app  
ONBUILD RUN bundle exec rake assets:precompile  
  
EXPOSE 3000  
CMD bundle exec rails server -b 0.0.0.0 -p $PORT

