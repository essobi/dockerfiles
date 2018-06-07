FROM ruby:2.4.0-alpine  
  
ARG app_path=/usr/src/app/  
  
RUN mkdir -p $app_path  
WORKDIR $app_path  
  
COPY gems.rb $app_path  
COPY gems.locked $app_path  
RUN apk add --update-cache build-base \  
&& bundle install --frozen \  
&& apk del build-base  
  
COPY . $app_path  
CMD [ "bundle", "exec", "puma" ]  

