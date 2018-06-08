FROM alpine:3.6  
RUN apk -v --update --no-cache add \  
bash \  
python \  
py-pip  
  
RUN pip install --upgrade awscli && \  
apk -v --purge del py-pip && \  
rm /var/cache/apk/*  
  

