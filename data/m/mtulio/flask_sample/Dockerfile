FROM python:3.5-alpine3.4  
LABEL maintainer="braga@mtulio.eng.br"  
  
WORKDIR /app  
  
COPY requirements.txt ./  
RUN apk upgrade --update \  
&& apk add --virtual \  
gcc \  
&& apk add \  
musl-dev libffi-dev openssl-dev \  
&& pip install --no-cache-dir -r requirements.txt \  
&& apk del gcc \  
&& rm -rf /var/cache/apk/* \  
&& mkdir -p /var/log/app  
  
COPY . .  
  
CMD [ "python", "./app.py" ]  
EXPOSE 5000:5000  

