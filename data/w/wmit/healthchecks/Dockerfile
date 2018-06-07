FROM python:3.6-alpine  
  
LABEL org.label-schema.name="Healthchecks" \  
org.label-schema.description="Basic intallation of Healthchecks" \  
org.label-schema.schema-version="1.0"  
  
HEALTHCHECK CMD curl -f http://localhost:8080/ || exit 1  
ENV PYTHONUNBUFFERED=1  
ADD . /healthchecks  
  
WORKDIR /healthchecks  
  
RUN apk add --no-cache tzdata \  
&& rm /etc/localtime \  
&& ln -s /usr/share/zoneinfo/US/Eastern /etc/localtime  
  
RUN apk add --no-cache mariadb-libs mariadb-client-libs postgresql-libs curl \  
&& apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev mariadb-
dev postgresql-dev\  
&& pip install --no-cache-dir -r requirements.txt \  
&& pip install --no-cache-dir gunicorn==19.7.1 \  
&& apk del .build-deps \  
&& cp docker/local_settings.py hc/. \  
&& python manage.py collectstatic --noinput \  
&& python manage.py compress  
  
EXPOSE 8080  
CMD ["gunicorn", "-b", "0.0.0.0:8080", "hc.wsgi:application", "--log-config",
"docker/gunicorn-logging.conf"]  

