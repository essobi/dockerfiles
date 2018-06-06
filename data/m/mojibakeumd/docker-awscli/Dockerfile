FROM alpine:3.4  
  
RUN \  
mkdir -p /aws && \  
apk -Uuv add groff less python py-pip perl openssh bash && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  

