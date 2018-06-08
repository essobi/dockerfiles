FROM python:2-alpine  
MAINTAINER "gp3t1@openmailbox.org"  
# ENVIRONMENT VARIABLES  
ENV SCRAPYD_USER "scrapyd"  
# VOLUMES  
VOLUME ["/etc/scrapyd/", "/var/lib/scrapyd/", "/var/log/supervisor/"]  
  
# INSTALL SYSTEM DEPENDENCIES  
RUN apk add --no-cache \  
build-base \  
busybox-suid \  
git \  
libffi-dev \  
libxml2 \  
libxml2-dev \  
libxslt \  
libxslt-dev \  
openssl-dev  
# INSTALL PYTHON DEPENDENCIES  
RUN pip install \  
functools32 \  
gitpython \  
python-crontab \  
python-scrapyd-api \  
requests \  
runp \  
scrapy \  
scrapyd \  
scrapyd-client \  
supervisor  
  
# COPY FILES & SET PERMISSIONS  
COPY etc/* /etc/  
COPY bin/* /usr/local/bin/  
RUN chmod 640 /etc/supervisord.conf  
RUN chmod +x,go-w /usr/local/bin/*  
  
WORKDIR "/var/lib/scrapyd"  
  
EXPOSE 6800 8000  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint"]  
CMD ["help"]

