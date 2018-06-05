FROM alpine:latest  
  
COPY backup.sh /usr/local/bin/s3-backup.sh  
  
# Use dl-4, as the main repo is down (23.08.2016)  
RUN sed -i -e 's/dl-cdn/dl-4/' /etc/apk/repositories && \  
apk add -v --update --no-cache mysql-client \  
python \  
py-pip \  
groff \  
less \  
mailcap \  
bash \  
&& \  
pip install --upgrade awscli && \  
apk -v --purge del py-pip && \  
rm /var/cache/apk/*  
  
RUN touch crontab.tmp && \  
echo '0 23 * * * /usr/local/bin/s3-backup.sh > /dev/null 2>&1' > crontab.tmp
&& \  
crontab crontab.tmp && \  
rm -rf crontab.tmp && \  
mkdir -p /var/www/html && \  
mkdir -p /var/www/_backups && \  
chmod +x /usr/local/bin/s3-backup.sh  
  
VOLUME /var/www/html  
  
CMD /usr/sbin/crond -f -d 0  

