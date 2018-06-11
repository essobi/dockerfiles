FROM ruby:2.5-alpine3.7  
WORKDIR /app  
  
COPY Gemfile Gemfile.lock /app/  
RUN apk add --no-cache --virtual=.run-deps libcurl libffi &&\  
apk add --no-cache --virtual=.build-deps build-base libffi-dev &&\  
bundle install --system --no-cache &&\  
apk del .build-deps  
  
COPY . /app/  
RUN jekyll build --destination /build  
  
CMD [ "jekyll", "serve", "--host", "0.0.0.0", "--skip-initial-build", "--no-
watch", "--destination", "/build" ]  
EXPOSE 4000  

