FROM nginx:stable  
  
WORKDIR /app  
  
RUN apt-get update  
RUN apt-get install -y git ruby rubygems-integration inotify-tools ruby-dev  
  
RUN mkdir -p /var/www/cache/temp  
  
RUN gem --version  
RUN gem install sass -v 3.3.14  
  
RUN rm /etc/nginx/conf.d/default.conf  
  
COPY sass.conf /etc/nginx/conf.d/default.conf  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
  
RUN chmod +x /usr/bin/entrypoint.sh  
  
ENTRYPOINT ["su", "-c", "/usr/bin/entrypoint.sh"]

