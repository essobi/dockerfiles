FROM python:3.6  
LABEL version="0.0.5"  
LABEL maintainer="loposk@yandex.ru"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
postgresql-client \  
libsasl2-dev \  
python-dev \  
libldap2-dev \  
libssl-dev && \  
mkdir /usr/src/app && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install \  
psycopg2-binary \  
python-memcached \  
requests \  
py-postgresql \  
pyyaml \  
ua-parser \  
user-agents \  
django-user-agents \  
django-python3-ldap  
  
COPY ./app /usr/src/app  
  
WORKDIR /usr/src/app  
  
EXPOSE 80  
CMD ["python3", "start.py"]

