FROM beevelop/base  
  
MAINTAINER Maik Hummel <m@ikhummel.com>  
  
WORKDIR /opt/  
  
COPY requirements.txt start conf.env createAdminOnce.py ./  
  
RUN apt-get -qq update && \  
apt-get -qq install python-psycopg2 python-lxml python-wheel python-pillow gcc
libxml2-dev libxslt-dev zlib1g-dev python-dev python python-dev python-pip
python-virtualenv python-setuptools libjpeg8-dev -y --no-install-recommends &&
\  
apt-get -qq install curl git mercurial ssh gettext netcat -y && \  
pip install -r requirements.txt && \  
chmod +x start createAdminOnce.py  
  
COPY settings.py /usr/local/lib/python2.7/dist-packages/weblate/  
  
ENV DJANGO_SETTINGS_MODULE=weblate.settings  
  
VOLUME ["/app/etc", "/app/data"]  
  
CMD ./start  
  
EXPOSE 8000  

