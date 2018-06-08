FROM alpine:latest  
MAINTAINER Ushio Shugo <ushio.s@gmail.com>  
  
ENV ACCOUNT=dummy \  
DOMAIN=dip.jp \  
PASSWORD=dummy  
  
ENV REMOTE_ADDR_CHK=https://ieserver.net/ipcheck.shtml \  
DDNS_UPDATE=https://ieserver.net/cgi-bin/dip.cgi \  
MINUTE=17,38,52 \  
SCRIPT_PATH=/usr/local/bin/cron.sh \  
CRON_LOG=/var/log/cron \  
CRON_ERR_LOG=/var/log/cron.err  
  
RUN apk --no-cache add curl  
  
ADD ./cron.sh $SCRIPT_PATH  
RUN echo -e "$MINUTE * * * * /bin/sh $SCRIPT_PATH 1> $CRON_LOG 2>
$CRON_ERR_LOG" > /etc/crontabs/root  
  
ENTRYPOINT ["crond", "-l", "2", "-f"]  

