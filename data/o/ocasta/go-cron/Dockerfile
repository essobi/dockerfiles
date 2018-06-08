FROM ubuntu:trusty  
  
RUN apt-get update && apt-get -y install curl bash \  
&& curl -SL https://github.com/odise/go-cron/releases/download/v0.0.7/go-cron-
linux.gz \  
| zcat > /usr/local/bin/go-cron \  
&& chmod u+x /usr/local/bin/go-cron \  
&& apt-get -y autoremove  
  
COPY go-cron.sh /usr/local/bin/  
  
EXPOSE 18080  
CMD ["go-cron.sh"]  

