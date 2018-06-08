FROM alpine:3.6  
LABEL author='Minimum'  
LABEL email='s5550055@yahoo.com.tw'  
ENV CRON='/etc/crontabs'  
ENV PERIOD='/etc/periodic'  
ENV WORKSPACE='/usr/local/cron'  
RUN apk add --no-cache bash curl jq python3 \  
&& mkdir -p $CRON $WORKSPACE \  
&& rm -fr $CRON/* $PERIOD/*  
  
COPY cron $CRON/root  
COPY docker-entrypoint.sh /  
  
SHELL ["/bin/bash", "-c"]  
  
RUN mkdir -p
$PERIOD/{1min,5min,10min,15min,30min,1hour,12hour,1day,1week,1month}  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

