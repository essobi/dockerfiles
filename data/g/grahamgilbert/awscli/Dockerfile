FROM alpine:latest  
  
RUN \  
apk -Uuv add groff less python py-pip ca-certificates && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
ENTRYPOINT ["aws"]  

