FROM ruby:2.2  
RUN apt-get update && \  
apt-get -y install libpq-dev nginx nodejs  
  
ENV PORT 5000  
COPY bin/web /app/bin/web  
COPY conf/convox.rb /app/config/initializers/convox.rb  
COPY conf/nginx.conf /etc/nginx/nginx.conf  
  
CMD ["bin/web"]  

