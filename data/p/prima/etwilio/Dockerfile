FROM prima/elixir:1.3.2-3  
# Timezone data  
RUN apk --update add tzdata mysql-client && \  
rm -rf /var/cache/apk/* && \  
cp /usr/share/zoneinfo/Europe/Rome /etc/localtime && \  
echo "Europe/Rome" > /etc/timezone && \  
date && \  
apk del --purge tzdata  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

