FROM python:3.6-alpine  
  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache \  
git \  
zlib-dev \  
jpeg-dev \  
gcc \  
musl-dev \  
postgresql-dev \  
mariadb-dev \  
&& pip install gunicorn  
  
COPY . /app/  
RUN cd /app \  
&& pip install -r .requirements.txt  
  
RUN apk del \  
git \  
gcc \  
musl-dev \  
&& rm -rf /var/lib/apk/* /var/cache/apk/*  
  
WORKDIR /app  
  
EXPOSE 8080  
VOLUME /app/data  
CMD [ "gunicorn", "zombieproductions.wsgi", "-b", "0.0.0.0:8080" ]  

