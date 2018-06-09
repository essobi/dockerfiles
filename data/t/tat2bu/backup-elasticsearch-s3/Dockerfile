FROM mhart/alpine-node:8.3.0  
ADD backup.sh /backup.sh  
  
RUN apk -Uuv add curl groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/* && \  
npm install elasticdump -g && \  
chmod a+x /backup.sh  
  
CMD ["/backup.sh"]

