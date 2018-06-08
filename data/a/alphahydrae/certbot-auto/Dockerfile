FROM alphahydrae/certbot:0.1.0  
LABEL maintainer="docker@alphahydrae.com"  
  
ENV DUMB_INIT_VERSION="1.2.0"  
RUN apt-get update -qq && \  
apt-get install -q -y cron  
  
ADD https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
RUN mkdir -p /etc/cron.d /etc/cron.hourly /etc/cron.daily /etc/cron.weekly
/etc/cron.monthly /var/log && \  
rm -f /etc/cron.d/* && \  
rm -f /etc/cron.hourly/* && \  
rm -f /etc/cron.daily/* && \  
rm -f /etc/cron.weekly/* && \  
rm -f /etc/cron.monthly/*  
  
ADD cron.sh /usr/local/bin/cron  
ADD crontab /etc/cron.d/crontab  
ADD auto.sh /usr/local/bin/auto  
  
ENTRYPOINT [ "/usr/local/bin/dumb-init" ]  
CMD [ "/usr/local/bin/cron" ]  

