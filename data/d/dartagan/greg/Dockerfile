FROM alpine:latest  
MAINTAINER William Weiskopf <william@weiskopf.me>  
  
RUN apk add --no-cache \  
ca-certificates \  
python3 \  
&& python3 -m ensurepip \  
&& pip3 install greg stagger  
  
COPY crontab /var/spool/cron/crontabs/root  
COPY greg.conf /usr/lib/python3.5/site-packages/greg/data/  
  
USER root  
  
ENTRYPOINT []  
  
CMD ["crond", "-l", "0", "-f"]  
  

