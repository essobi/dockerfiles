FROM python:3.6-alpine  
  
RUN apk update && \  
apk add curl bash openssl&& \  
rm -rf /var/cache/apk/*  
  
RUN curl -o /usr/bin/dehydrated
https://raw.githubusercontent.com/lukas2511/dehydrated/master/dehydrated && \  
chmod +x /usr/bin/dehydrated  
  
COPY dehydrated.conf /etc/dehydrated/config  
  
WORKDIR "/home/working"  
COPY src .  
  
RUN pip install -r requirements.txt  
  
VOLUME /etc/dehydrated/certs  
VOLUME /etc/dehydrated/accounts  
  
ENTRYPOINT ["python", "main.py"]  

