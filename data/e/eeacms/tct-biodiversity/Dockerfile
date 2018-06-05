  
FROM python:2-alpine3.6  
MAINTAINER "EEA: IDM2 C-TEAM" <eea-edw-c-team-alerts@googlegroups.com>  
  
ENV PROJ_DIR=/var/local/tct/  
  
RUN runDeps="gcc musl-dev gettext postgresql-dev netcat-openbsd libressl-dev
openldap-dev" \  
&& apk add --no-cache $runDeps  
  
RUN apk add --no-cache --virtual .build-deps \  
gcc musl-dev postgresql-dev libressl-dev \  
&& apk add --no-cache \  
gettext netcat-openbsd openldap-dev \  
&& mkdir -p $PROJ_DIR  
  
# Add requirements.txt before rest of repo for caching  
COPY requirements.txt $PROJ_DIR  
WORKDIR $PROJ_DIR  
  
RUN pip install --no-cache-dir -r requirements.txt \  
&& apk del .build-deps  
  
COPY . $PROJ_DIR  
  
RUN python manage.py makemessages \  
&& python manage.py compilemessages \  
&& python manage.py collectstatic --noinput  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  
CMD ["run"]  

