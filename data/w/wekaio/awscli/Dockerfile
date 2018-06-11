FROM alpine:3.6  
RUN apk -Uuv add groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
ENTRYPOINT ["aws"]  

