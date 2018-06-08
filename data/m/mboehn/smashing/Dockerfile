FROM mboehn/noderuby  
  
ARG dir=/srv/dash  
WORKDIR $dir  
  
RUN apk add --no-cache g++ musl-dev make --virtual .gems-deps  
RUN gem install bundler smashing --no-ri --no-rdoc  
RUN smashing new $dir  
RUN bundle  
RUN apk del --no-cache .gems-deps  
  
CMD sed -i "s/YOUR_AUTH_TOKEN/${TOKEN}/" config.ru && smashing start -p $PORT  
  
EXPOSE 8080  

