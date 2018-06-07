FROM ruby:2.5-alpine  
  
RUN apk --no-cache add \  
bash \  
build-base \  
gettext \  
tzdata  
  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN gem install twitter_ebooks  
RUN ebooks new ebooks  
  
RUN apk del build-base  
  
RUN mkdir template \  
&& mkdir app  
  
COPY ebooksrc /template/ebooksrc  
COPY bots.rb /template/bots.rb  
  
COPY import.sh /template/import.sh  
  
COPY crontab.txt /template  
RUN /usr/bin/crontab /template/crontab.txt  
  
COPY run.sh /  
RUN chmod +x /run.sh \  
&& touch /var/log/cron.log  
  
WORKDIR /ebooks  
  
ENTRYPOINT ["/run.sh"]  

