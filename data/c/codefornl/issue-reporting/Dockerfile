FROM python:3.5  
ENV PYTHONUNBUFFERED 1  
ENV MEDIA_ROOT /data  
ENV STATIC_ROOT /tmp/static  
VOLUME /data  
EXPOSE 8000  
WORKDIR /code  
RUN curl -O https://raw.githubusercontent.com/vishnubob/wait-for-
it/master/wait-for-it.sh && chmod u+x wait-for-it.sh  
RUN pip install uwsgi psycopg2  
ADD . /code/  
RUN pip install -r requirements.txt  
ENTRYPOINT \  
python manage.py collectstatic --noinput -v0 && \  
(if [ ! -z "$WAIT_FOR_IT" ]; then exec ./wait-for-it.sh "$WAIT_FOR_IT"; exec
true; fi) && \  
python manage.py migrate --noinput && \  
python manage.py cfh_init && \  
uwsgi --master --wsgi cfh.wsgi --http :8000 --enable-threads --workers 4
--logto /var/log/issue-reporting.log --die-on-term --need-app --thunder-lock
--static-map /static=/tmp/static --static-map /media=/data  

