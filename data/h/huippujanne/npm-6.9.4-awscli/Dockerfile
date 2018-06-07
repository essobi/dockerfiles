FROM node:6.9.4-alpine  
RUN apk -Uuv add libxml2-utils libxml2 bash py-pip &&\  
pip install awscli &&\  
#apk --purge -v del py-pip &&\  
rm /var/cache/apk/*  

