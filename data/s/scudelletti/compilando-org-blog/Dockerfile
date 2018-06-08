FROM ruby:2.4.0 as builder  
  
WORKDIR /build  
COPY ./ .  
  
RUN bundle install  
RUN bundle exec jekyll build  
  
FROM nginx:alpine  
  
COPY \--from=builder /build/_site /usr/share/nginx/html

