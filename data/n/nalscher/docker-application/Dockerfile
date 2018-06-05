FROM alpine  
  
ENV PUID 1000  
ENV GUID 1000  
# Install needed library  
RUN apk add -v --update \  
# supervisor \  
bash \  
zip \  
python \  
py-pip && \  
# mkdir -p /var/log/supervisor && \  
pip install --upgrade awscli s3cmd && \  
apk -v --purge del py-pip && \  
rm /var/cache/apk/*  
  
ENV APP_ROOT /var/www/html  
  
VOLUME $APP_ROOT  
WORKDIR $APP_ROOT  
  
# ADD conf/supervisord.conf /etc/supervisord.conf  
ADD start.sh /start.sh  
RUN chmod 755 /start.sh  
  
CMD ["/start.sh"]

