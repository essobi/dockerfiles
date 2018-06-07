FROM alpine  
MAINTAINER miko@cafelounge.net  
  
RUN cd /tmp \  
&& apk \--update add tzdata \  
&& cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& echo "Asia/Tokyo" > /etc/timezone \  
&& apk del \--purge tzdata \  
&& apk \--update add bash curl iptables \  
&& curl -o /usr/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64" \  
&& chmod +x /usr/bin/gosu \  
&& rm -rf /var/cache/apk/* \  
&& ln -s /etc/periodic/15min /etc/cron.15min \  
&& ln -s /etc/periodic/hourly /etc/cron.hourly \  
&& ln -s /etc/periodic/daily /etc/cron.daily \  
&& ln -s /etc/periodic/weekly /etc/cron.weekly \  
&& ln -s /etc/periodic/monthly /etc/cron.monthly  
# shell  
ENV HOME=/root LANG=ja_JP.UTF-8  
WORKDIR /root  
# entry  
COPY init /boot/  
# default entry point  
ENTRYPOINT ["/boot/init"]  

