FROM ruby:2.5-alpine  
  
RUN apk --no-cache add \  
bash \  
build-base \  
gettext \  
tzdata  
  
ENV TZ=Europe/Berlin  
  
RUN gem install date  
RUN gem install twitter  
  
RUN apk del build-base  
  
RUN mkdir /app  
COPY todayis.rb /app  
COPY crontab.txt /app  
RUN /usr/bin/crontab /app/crontab.txt  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
  
COPY run.sh /app  
RUN chmod +x /app/run.sh  
  
ENTRYPOINT ["/app/run.sh"]  
  

