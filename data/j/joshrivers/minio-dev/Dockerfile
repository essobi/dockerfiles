FROM minio/minio:latest  
  
RUN apk -Uuv add groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/* && \  
mkdir /root/.aws  
  
COPY docker-entrypoint.sh /usr/bin/  
COPY fakecredentials.json /root/.aws/config  
COPY fakecredentials.json /root/.aws/credentials  
RUN chmod +x /usr/bin/docker-entrypoint.sh  

