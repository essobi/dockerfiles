FROM python:3.6-alpine  
  
RUN apk add --no-cache \  
bash \  
build-base \  
ca-certificates \  
cyrus-sasl-dev \  
graphviz \  
jpeg-dev \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
openldap-dev \  
openssl-dev \  
postgresql-dev \  
wget  
  
RUN pip install gunicorn  
  
WORKDIR /opt  
  
ARG BRANCH=v2.3.3  
ARG URL=https://github.com/digitalocean/netbox/archive/$BRANCH.tar.gz  
RUN wget -q -O - "${URL}" | tar xz \  
&& mv netbox* netbox  
  
RUN pip install django-auth-ldap  
  
WORKDIR /opt/netbox  
RUN pip install -r requirements.txt  
  
COPY configuration.docker.py /opt/netbox/netbox/netbox/configuration.py  
COPY gunicorn_config.py /opt/netbox/  
  
WORKDIR /opt/netbox/netbox  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  
EXPOSE 8001  
CMD ["gunicorn", "--log-level debug", "-c /opt/netbox/gunicorn_config.py",
"netbox.wsgi"]  

