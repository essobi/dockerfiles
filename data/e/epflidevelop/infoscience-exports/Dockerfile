FROM python:3  
# install gettext  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gettext \  
tree \  
curl \  
&& rm -rf /var/cache/apt/ \  
&& rm -rf /var/lib/apt/lists/*  
  
# create directories  
RUN mkdir -p /usr/src/app && \  
mkdir -p /usr/src/app/staticfiles && \  
mkdir -p /usr/src/app/infoscience_exports && \  
mkdir -p /var/log/django  
  
WORKDIR /usr/src/app  
  
# install requirements  
# (asap to make cache more efficent)  
COPY ./requirements*.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements-dev.txt  
  
# copy project files  
COPY ./update_release.py /usr/src/app/update_release.py  
COPY ./infoscience_exports/exports/versions.py /usr/src/app/versions.py  
COPY ./Makefile /usr/src/app/Makefile  
COPY ./infoscience_exports /usr/src/app/infoscience_exports  
  
# collectstatic  
RUN DJANGO_SETTINGS_MODULE=settings.prod \  
SECRET_KEY="not needed to collectstaticfiles" \  
ALLOWED_HOSTS="not needed to collectstaticfiles" \  
SITE_URL="not needed to collectstaticfiles" \  
DATABASE_URL="not needed to collectstaticfiles" \  
python infoscience_exports/manage.py collectstatic  
  
# compilemessages  
RUN DJANGO_SETTINGS_MODULE=settings.prod \  
SECRET_KEY="not needed to compilemessages" \  
ALLOWED_HOSTS="not needed to compilemessages" \  
SITE_URL="not needed to compilemessages" \  
DATABASE_URL="not needed to compilemessages" \  
python infoscience_exports/manage.py compilemessages  
  
VOLUME ["/usr/src/app/staticfiles", "/var/log/django",
"/usr/src/app/coverage.xml"]  

