FROM ruby:2.3-alpine  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile .  
  
RUN \  
apk add --no-cache --virtual .build-deps \  
g++ \  
linux-headers \  
make \  
&& apk add --no-cache nodejs \  
&& bundle install --system \  
&& rm Gemfile* \  
&& apk del .build-deps  
  
VOLUME [/usr/src/app]  
EXPOSE 4000  
CMD ["jekyll", "serve", "--watch", "--force_polling", "--host", "0.0.0.0", "--
port", "4000"]  

