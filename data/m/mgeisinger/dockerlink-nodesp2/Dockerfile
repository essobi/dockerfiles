FROM python:2.7-alpine  
RUN apk add --no-cache --virtual .build-deps build-base git \  
&& apk add --no-cache nodejs \  
&& pip install broadlink \  
&& npm install python-shell \  
&& npm install express \  
&& git clone https://bitbucket.org/mgeisinger/broadlink-nodesp2.git
/usr/src/app \  
&& apk del .build-deps  
WORKDIR /usr/src/app  
ENTRYPOINT [ "node", "main.js" ]  

