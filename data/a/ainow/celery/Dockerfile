FROM python:3.6.4-alpine3.7  
MAINTAINER coolbaby "coolbaby"  
RUN \  
apk add --no-cache tzdata \  
&& cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& apk add --no-cache curl linux-headers \  
&& apk add --no-cache musl-dev gcc git \  
#&& pip install celery==4.0.2 \  
&& pip install redis auth msgpack \  
#&& pip install "celery[redis,auth,msgpack]"  
\  
&& pip install git+https://github.com/celery/librabbitmq \  
&& rm -rf librabbitmq \  
&& pip install Django==2.0.1 \  
&& python -m django --version \  
&& pip install django-celery \  
&& pip install sqlalchemy \  
&& pip install django-celery-results \  
&& pip install flower \  
&& pip install -U uwsgi \  
&& pip install django-celery-beat \  
&& pip install celery==4.0.2 \  
&& apk del musl-dev gcc linux-headers git  
  
COPY docker-entrypoint /usr/local/bin/  
COPY uwsgi.ini /etc/uwsgi.ini  
  
#fix celery beat can not auto run when add some task in django admin ui  
COPY ok_beat.py /usr/local/lib/python3.6/site-packages/celery/beat.py  
  
RUN chmod +x /usr/local/bin/docker-entrypoint  
  
ENTRYPOINT ["docker-entrypoint"]  
  
#CMD ["celery","worker"]  
WORKDIR /usr/src/celery  
  
#ENV CELERY_BROKER_URL amqp://guest@rabbit  
# flower port,uwsgi port  
EXPOSE 5555 6000  
#ENTRYPOINT ["uwsgi --socket :6000 --master --processes 4 --threads 2 --vhost
--pidfile=/var/run/uwsgi.pid --vacuum --thunder-lock"]  
#CMD ["--socket :6000 --master --processes 4 --threads 2 --vhost
--pidfile=/var/run/uwsgi.pid --vacuum --thunder-lock"]  

