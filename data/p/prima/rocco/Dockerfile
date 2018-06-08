FROM prima/nginx:1.12.0-1  
# aws cli  
RUN apk -Uuv add python py-pip curl && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm -rf /var/cache/apk/* && \  
  
mkdir /code && \  
rm -f /etc/nginx/conf.d/*  
  
COPY files/rocco.conf /etc/nginx/conf.d/rocco.conf  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  

