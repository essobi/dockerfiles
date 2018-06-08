FROM python:3.6.3-alpine  
  
RUN apk add --update --no-cache tzdata postgresql-dev libc-dev gcc \  
&& cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime \  
&& echo "Europe/Moscow" > /etc/timezone \  
&& pip install --no-cache-dir psycopg2 \  
&& apk del tzdata libc-dev gcc  
  
CMD ["python"]  

