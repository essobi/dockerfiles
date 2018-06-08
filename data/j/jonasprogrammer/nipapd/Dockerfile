FROM python:2-stretch  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libpq-dev \  
postgresql-client \  
libsqlite3-dev \  
libldap2-dev \  
libsasl2-dev \  
&& pip --no-input install envtpl python-ldap \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo '#!/bin/sh' >/usr/bin/rst2man \  
&& echo 'touch $2' >>/usr/bin/rst2man \  
&& chmod +x /usr/bin/rst2man  
  
COPY nipap/nipap /nipap  
WORKDIR /nipap  
RUN pip --no-input install -r requirements.txt \  
&& python setup.py install  
  
EXPOSE 1337  
ENV LISTEN_ADDRESS=0.0.0.0 LISTEN_PORT=1337 \  
SYSLOG=false \  
DB_PORT=5432 DB_SSLMODE=disable \  
AUTH_DEFAULT=true AUTH_BACKEND=local AUTH_CACHE=3600 \  
AUTH_BACKEND_local_type=SqliteAuth
AUTH_BACKEND_local_db_path=/etc/nipap/local_auth.db  
  
COPY entrypoint-nipapd.sh backend-config-generator.sh nipap.conf.dist /nipap/  
  
ENTRYPOINT ["/nipap/entrypoint-nipapd.sh"]  
CMD ["/usr/sbin/nipapd", "--debug", "--foreground", "--auto-install-db", "--
auto-upgrade-db", "--no-pid-file"]  

