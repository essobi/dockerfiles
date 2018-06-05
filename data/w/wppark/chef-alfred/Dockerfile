FROM lemonsqueeze/scala-sbt-java  
  
MAINTAINER rainist <rainist@rainist.com>  
  
ENV ALFRED_ENV prod  
  
RUN mkdir -p /var/www  
  
ADD . /var/www  
  
WORKDIR /var/www  
RUN cp database.conf src/main/resources/database.conf  
RUN sbt compile  
RUN sbt assembly  
  
RUN rm /etc/nginx/sites-enabled/default  
ADD conf/nginx.conf /etc/nginx/sites-enabled/  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
ADD conf/supervisor.conf /etc/supervisor/conf.d/  
  
EXPOSE 80  
CMD ["supervisord", "-n"]  

