FROM debian:stable  
  
RUN apt-get update && apt-get install -yq nginx bundler supervisor libpq-dev
postgresql  
  
#create tmp directories  
RUN mkdir /www && mkdir /fileserver && mkdir /fileserver/tmp && mkdir
/fileserver/tmp/sockets && mkdir /fileserver/tmp/pids && mkdir /fileserver/log  
  
# configure nginx  
RUN rm /etc/nginx/sites-enabled/default  
ADD config/nginx.conf /etc/nginx/sites-enabled/nginx  
  
# run bundle install  
COPY config/Gemfile* /tmp/  
WORKDIR /tmp  
RUN bundle install  
#reset app directory  
WORKDIR /fileserver/  
  
# configure supervisor  
ADD config/supervisord.conf /fileserver/config/supervisord.conf  
  
# add startup script(s) and give executable permissions  
ADD scripts /fileserver/scripts  
RUN chmod -R 777 /fileserver/scripts  
  
#expose public volume for mounting  
VOLUME [ "/fileserver/app", "/fileserver/log", "/fileserver/config",
"/fileserver/scripts" ]  
  
#cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#start supervisor  
CMD ["/fileserver/scripts/startup.sh"]  
  
EXPOSE 8000

