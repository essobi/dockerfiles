FROM python:3.6-alpine  
  
ENV APP_CALLABLE=app \  
GUNICORN_SOCKET_LOCATION=/tmp/app.sock \  
GUNICORN_WORKER_TYPE=eventlet \  
GUNICORN_WORKERS=4 \  
GUNICORN_TIMEOUT=300 \  
GUNICORN_CLI_EXTEND=  
  
ONBUILD COPY . /code/  
ONBUILD WORKDIR /code  
ONBUILD RUN \  
apk add --no-cache --virtual .build-deps \  
# Pull alpine-sdk in so most stuff _probably_ builds  
# if it requires external libs  
alpine-sdk \  
&& pip install flask greenlet eventlet gevent gunicorn \  
&& if [ -e /code/apk_packages.txt ]; then while IFS='' read line; do apk add
\--no-cache $line; done < /code/apk_packages.txt; fi \  
&& if [ -e requirements.txt ]; then pip install -r requirements.txt; fi \  
&& python /code/setup.py install \  
&& rm -rf /var/cache/apk/* \  
&& apk del .build-deps  
  
CMD gunicorn $APP_NAME:$APP_CALLABLE -k $GUNICORN_WORKER_TYPE -w
$GUNICORN_WORKERS -t $GUNICORN_TIMEOUT -b unix:$GUNICORN_SOCKET_LOCATION
\--pid=$PID $GUNICORN_CLI_EXTEND  

