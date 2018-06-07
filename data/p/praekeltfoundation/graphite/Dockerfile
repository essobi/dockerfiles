FROM praekeltfoundation/supervisor  
MAINTAINER Praekelt Foundation <dev@praekeltfoundation.org>  
  
# See http://graphite.readthedocs.org/en/0.9.15/install-pip.html  
ENV GRAPHITE_VERSION "0.9.15"  
RUN apt-get-install.sh libcairo2 libpq-dev  
# Install graphite-web dependencies  
# graphite-web as of version 0.9.15 doesn't set any `install_requires` in its  
# setup.py so we have to install these manually.  
# http://graphite.readthedocs.org/en/0.9.15/install.html#dependencies  
# https://github.com/graphite-project/graphite-
web/blob/0.9.15/requirements.txt  
RUN pip install cairocffi \  
Django==1.4 \  
django-tagging==0.3.1 \  
gunicorn \  
pytz \  
txAMQP \  
dj-database-url \  
psycopg2  
  
RUN pip install "whisper==${GRAPHITE_VERSION}" \  
"carbon==${GRAPHITE_VERSION}" \  
"graphite-web==${GRAPHITE_VERSION}"  
  
# Graphite installs into /opt somehow  
ENV GRAPHITE_ROOT "/opt/graphite"  
ENV PYTHONPATH="$GRAPHITE_ROOT/lib:$GRAPHITE_ROOT/webapp" \  
DJANGO_SETTINGS_MODULE="graphite.settings" \  
PATH="$PATH:$GRAPHITE_ROOT/bin"  
WORKDIR $GRAPHITE_ROOT  
RUN mkdir /var/run/graphite  
  
COPY ./carbon.conf.example conf/carbon.conf.example  
COPY ./storage-aggregation.conf conf/storage-aggregation.conf  
COPY ./storage-schemas.conf conf/storage-schemas.conf  
  
# Set up basic config  
RUN cp conf/graphite.wsgi.example webapp/graphite/wsgi.py  
  
COPY ./local_settings.py /opt/graphite/webapp/graphite  
  
# Copy in supervisor configs  
COPY ./supervisor /etc/supervisor/conf.d  
  
EXPOSE 8000  
VOLUME /opt/graphite/storage  
  
COPY ./bootstrap.sh /scripts  
CMD ["bootstrap.sh"]  

