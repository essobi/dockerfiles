FROM ruby:2.4-alpine  
LABEL maintainer="Christian Mehlmauer <FireFart@gmail.com>"  
  
ENV APP_USER="user"  
ENV APP_HOME="/app"  
ENV BUILD_PACKAGES="alpine-sdk cmake"  
RUN echo "gem: --no-document" > /etc/gemrc  
RUN adduser -D user  
  
COPY Gemfile $APP_HOME/  
# runtime dependencies  
RUN apk add \--no-cache --virtual build-deps $BUILD_PACKAGES && \  
gem update --system && \  
gem install bundler && \  
bundle install --system \--gemfile=$APP_HOME/Gemfile && \  
apk del --no-cache build-deps  
  
RUN chown -R $APP_USER:$APP_USER $APP_HOME  
  
WORKDIR $APP_HOME/  
USER $APP_USER  
  
VOLUME $APP_HOME  
  
EXPOSE 4000  
  
ENTRYPOINT ["jekyll"]  
  
CMD ["serve", "--host", "0.0.0.0"]  

