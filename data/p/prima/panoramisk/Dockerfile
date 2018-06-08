FROM msaraiva/elixir-dev:1.2.2  
# Timezone data  
RUN apk --update add tzdata && \  
rm -rf /var/cache/apk/* && \  
cp /usr/share/zoneinfo/Europe/Rome /etc/localtime && \  
echo "Europe/Rome" > /etc/timezone && \  
date && \  
apk del tzdata  
  
# aws cli  
RUN mkdir -p /aws && \  
apk -Uuv add groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

