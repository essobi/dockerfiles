FROM frolvlad/alpine-python3  
  
EXPOSE 8000  
RUN mkdir -p /var/www/static  
VOLUME /var/www/static  
  
RUN mkdir -p /var/www/media  
VOLUME /var/www/media  
  
RUN mkdir -p /usr/django/app  
  
RUN mkdir -p /etc/gunicorn  
COPY gunicorn.conf /etc/gunicorn/  
  
RUN pip install gunicorn  
  
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev \  
ca-certificates libxml2-dev libxslt-dev jpeg-dev zlib-dev  
  
# install application dependencies  
ONBUILD COPY src/requirements.txt /usr/django/requirements.txt  
ONBUILD RUN pip install -r /usr/django/requirements.txt  
  
# add application source code  
ONBUILD COPY src /usr/django  
  
COPY start.sh /usr/django/  
WORKDIR /usr/django  
  
CMD /bin/sh start.sh

