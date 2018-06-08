FROM python:3.6.3-alpine3.6  
  
LABEL company="Backupner" \  
description="Base image contains Alpine, Python and some software, tools and
utilities (see notes below). " \  
version="3.2.1" \  
maintainer="info@backupner.com" \  
notes.16="* Upgrade Alpine packages" \  
notes.17="* Add bash, yaml" \  
notes.23="* Add flake8 config" \  
notes.44="* Add arrow, coverage, docutils, flake8, lxml, mypy, psycopg2,
pylint, pynacl, PyYAML and sphinx tools. Add openssh-client. Add uWSGI
webserver"  
  
  
ENV PYTHON_UWSGI_VERSION 2.0.15  
  
RUN set -ex; \  
apk upgrade --no-cache; \  
apk add --upgrade --no-cache \  
bash \  
openssh-client \  
yaml; \  
mkdir -p "/root/.config/"; \  
echo -e "[flake8] \nmax-line-length = 180" > "/root/.config/flake8"; \  
apk add --upgrade --no-cache --virtual .build-deps \  
build-base \  
linux-headers \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
postgresql-dev; \  
apk add --upgrade --no-cache --virtual .run-deps \  
busybox \  
jansson \  
libcap \  
libffi \  
libressl2.5-libcrypto \  
libressl2.5-libssl \  
libxml2 \  
libxslt \  
mailcap \  
musl \  
pcre \  
postgresql \  
zlib; \  
python3 -m pip install --no-cache-dir --upgrade \  
arrow \  
coverage \  
docutils \  
flake8 \  
lxml \  
mypy \  
psycopg2 \  
pylint \  
pynacl \  
PyYAML \  
sphinx \  
"uwsgi==$PYTHON_UWSGI_VERSION"; \  
apk del .build-deps  
  
  
CMD ["python3"]  

