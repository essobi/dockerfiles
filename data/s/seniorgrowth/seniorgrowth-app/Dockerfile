FROM python:2.7  
RUN apt-get update  
  
RUN apt-get autoremove -y && apt-get install -y --no-install-recommends
libmemcached-dev libtiff5-dev libjpeg62-turbo-dev libzip-dev libfreetype6-dev
liblcms2-dev libwebp-dev tcl-dev gcc ruby ruby-dev postgresql-server-dev-9.4
nodejs nodejs-legacy npm && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
RUN npm install -g bower  
RUN gem install compass  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
  
#https://pip.pypa.io/en/latest/user_guide/#fast-local-installs  
RUN mkdir -p /tmp/python-pkg && pip install --download /tmp/python-pkg -r
requirements.txt  
RUN pip install --no-cache-dir --no-index --find-links=/tmp/python-pkg
--exists-action i -r requirements.txt && rm -rf /tmp/python-pkg  
  
COPY bower.json /usr/src/app/  
RUN bower install --force --production --config.interactive=false \--allow-
root  
  
ENV DJANGO_SETTINGS_MODULE seniorgrowth.settings  
  
COPY . /usr/src/app  
  
RUN compass compile --force || true  
RUN ./manage.py compress --force  
RUN ./manage.py collectstatic --noinput  
  
EXPOSE 8000  
COPY docker-entrypoint.sh /  
  
VOLUME /usr/src/app/static  
VOLUME /usr/src/app/media  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
#--workers=2-4 x $(NUM_CORES)  
#or  
#--threads=2-4 x $(NUM_CORES)  
ENV DJANGO_SETTINGS_MODULE seniorgrowth.eb_settings  
  
#for celery worker  
ENV C_FORCE_ROOT 1  
CMD ["gunicorn"]  

