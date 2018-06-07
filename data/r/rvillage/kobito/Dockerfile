# before setup  
FROM ruby:2.5-alpine3.7 AS gem  
  
WORKDIR /usr/src/app  
  
COPY Gemfile Gemfile.lock /usr/src/app/  
  
RUN apk --update add --no-cache \  
build-base \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
nodejs \  
postgresql-dev \  
tzdata \  
yarn  
RUN bundle install --jobs=4  
  
# setup docker image  
FROM ruby:2.5-alpine3.7  
ENV LANG ja_JP.UTF-8  
WORKDIR /usr/src/app  
  
RUN adduser -D rails \  
&& echo "rails ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& chown -R rails /usr/src/app  
  
COPY \--from=gem /usr/share/zoneinfo/ /usr/share/zoneinfo/  
# docker17.09から--chownが使える  
# COPY --from=gem --chown=rails /usr/local/bundle /usr/local/bundle  
COPY \--from=gem /usr/local/bundle /usr/local/bundle  
RUN chown -R rails /usr/local/bundle  
  
RUN apk --update add --no-cache \  
nodejs \  
postgresql-dev \  
sudo \  
yarn  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& echo "Asia/Tokyo" > /etc/timezone  
  
USER rails  
CMD rails -v  

