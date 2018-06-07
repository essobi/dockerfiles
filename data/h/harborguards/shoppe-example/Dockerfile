FROM ruby:2.1  
MAINTAINER Matthias Neugebauer <mtneug@mailbox.org>  
  
ENV RAILS_ENV=production  
ENV DB_USER=root  
ENV DB_NAME=shoppe_prod  
  
RUN apt-get update \  
&& apt-get install -y mysql-client nodejs --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/tryshoppe/shoppe-example.git /app \  
&& cd /app \  
&& git checkout c9c6808638c0f6ac9cf673dba86f83840db44caf \  
&& rm -rf /app/.git /app/config/database.example.yml  
WORKDIR /app  
RUN bundle install  
COPY database.yml config/database.yml  
RUN rake assets:precompile  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
EXPOSE 3000  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["rails", "server", "-b", "0.0.0.0"]  

