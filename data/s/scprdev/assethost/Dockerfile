FROM ruby:2.3.4-alpine  
MAINTAINER Ben Titcomb <btitcomb@scpr.org>  
  
RUN apk update && apk add --no-cache \  
make \  
gcc \  
libgcc \  
g++ \  
libc-dev \  
libffi-dev \  
imagemagick \  
exiftool \  
git \  
mysql-dev \  
ruby-json \  
yaml \  
zlib-dev \  
libxml2-dev \  
libxslt-dev \  
tzdata \  
yaml-dev \  
nginx \  
openrc \  
nodejs  
  
RUN addgroup -S assethost && adduser -S -g assethost assethost  
  
ENV HOME /home/assethost  
  
WORKDIR $HOME  
  
COPY . .  
  
ENV PATH="${HOME}/bin:${PATH}"  
RUN bundle install  
  
RUN cp config/templates/secrets.yml.template config/secrets.yml  
  
RUN bundle exec rake resources:precompile RAILS_ENV=production  
  
RUN cp nginx.conf /etc/nginx/nginx.conf  
  
# to work around a bug on my end  
RUN rm -rf tmp/* && rm -rf log/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& ln -sf /dev/stdout log/access.log \  
&& ln -sf /dev/stderr log/error.log \  
&& touch log/development.log \  
&& touch log/production.log \  
&& ln -sf /dev/stdout log/development.log \  
&& ln -sf /dev/stdout log/production.log  
  
RUN chown -R assethost:assethost tmp  
RUN chmod -R u+X tmp  
RUN chown -R assethost:assethost log  
RUN chmod -R u+X tmp  
RUN chown -R assethost:assethost db  
RUN chmod -R u+X db  
  
USER assethost  
  
EXPOSE 8080  
CMD server  
  

