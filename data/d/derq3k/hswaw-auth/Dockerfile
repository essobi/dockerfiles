FROM ubuntu:16.04  
RUN set -e -x ;\  
apt-get update; \  
apt-get -y install python-virtualenv build-essential libsasl2-dev python-dev
libldap2-dev libssl-dev  
  
RUN set -e -x ;\  
useradd -rm app ;\  
mkdir /app /venv ;\  
chown app:app /app ;\  
chown app:app /venv  
  
USER app  
WORKDIR /app  
RUN set -e -x ;\  
virtualenv /venv ;\  
/venv/bin/pip install python-ldap uwsgi flask  
  
ADD . /app  
RUN set -e -x ;\  
cp auth.cfg.from_env auth.cfg  
  
EXPOSE 8080  
CMD ["/venv/bin/uwsgi", \  
"--http", "0.0.0.0:8080", \  
"--manage-script-name", "--mount", "/=auth:app"]  

