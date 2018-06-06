FROM ruby:alpine  
RUN apk add --no-cache mercurial \  
&& gem install --no-rdoc --no-ri capistrano  
WORKDIR /app  
CMD ["cap"]  

