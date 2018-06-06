FROM alpine:latest  
  
ADD backup.sh /backup.sh  
  
RUN \  
mkdir -p /source && \  
mkdir -p /aws && \  
apk -Uuv add curl groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/* && \  
chmod a+x backup.sh  
  
CMD "/backup.sh"

