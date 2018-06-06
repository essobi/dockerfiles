FROM python:3.5-alpine  
  
RUN apk add --no-cache openssl ca-certificates  
  
ADD app /usr/src/app  
WORKDIR /usr/src/app  
  
RUN pip3 install --no-cache-dir -r requirements.txt  
  
VOLUME /usr/src/app/config  
  
CMD python3 -u main.py --daemon  

