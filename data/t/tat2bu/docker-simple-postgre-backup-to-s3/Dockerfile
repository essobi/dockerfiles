FROM alpine:latest  
  
ADD backup.sh /backup.sh  
  
RUN \  
apk -Uuv add gzip curl groff less postgresql python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/* && \  
chmod a+x backup.sh  
  
CMD "/backup.sh"

