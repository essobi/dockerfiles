FROM python:3-alpine  
  
WORKDIR /usr/src/app  
  
RUN apk --update add openssl ca-certificates py-openssl  
RUN apk --update add --virtual .build-dependencies libffi-dev openssl-dev
python-dev build-base  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
RUN apk del .build-dependencies  
  
COPY . .  
  
CMD [ "python", "./main.py" ]  

