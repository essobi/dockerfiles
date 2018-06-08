FROM python:3.5.2-alpine  
  
RUN apk add --update \  
build-base \  
python-dev \  
py-pip \  
mariadb-dev \  
jpeg-dev \  
zlib-dev \  
supervisor \  
&& pip install virtualenv \  
&& rm -rf /var/cache/apk/*  
  
ENV LIBRARY_PATH=/lib:/usr/lib  
  
RUN mkdir -p /var/www/sardegnaaccessibile \  
&& addgroup -S webapps \  
&& adduser -S -s /bin/bash -h /var/www/sardegnaaccessibile sauser webapps \  
&& chown sauser /var/www/sardegnaaccessibile \  
&& chgrp webapps /var/www/sardegnaaccessibile  
  
#USER sauser  
#RUN su - sauser  
  
RUN cd /var/www/sardegnaaccessibile \  
&& mkdir /var/www/sardegnaaccessibile/site \  
&& mkdir /var/www/sardegnaaccessibile/venv \  
&& mkdir /var/www/sardegnaaccessibile/logs \  
&& virtualenv /var/www/sardegnaaccessibile/venv  
  
COPY ./requirements.txt /var/www/sardegnaaccessibile/venv/requirements.txt  
RUN /var/www/sardegnaaccessibile/venv/bin/pip install -r
/var/www/sardegnaaccessibile/venv/requirements.txt \  
&& /var/www/sardegnaaccessibile/venv/bin/pip install gunicorn  
  
WORKDIR /var/www/sardegnaaccessibile/site  
  
CMD ["/var/www/sardegnaaccessibile/venv/bin/python", "manage.py", "runserver",
"localhost:80"]  

