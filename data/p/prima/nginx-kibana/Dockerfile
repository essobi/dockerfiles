FROM prima/nginx:1.12.2-1  
# TZ: https://github.com/primait/board/issues/1631  
ENV TZ=:/etc/localtime  
  
# aws cli  
RUN apk -Uuv add python py-pip curl zip rsync && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm -rf /var/cache/apk/* && \  
  
mkdir /code && \  
rm -f /etc/nginx/conf.d/*  
  
#COPY files/htpasswd.users /etc/nginx/htpasswd.users  
COPY files/kibana.conf /etc/nginx/conf.d/kibana.conf  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  

