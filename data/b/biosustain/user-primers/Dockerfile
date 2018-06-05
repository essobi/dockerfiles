FROM python:latest  
ENV PYTHONUNBUFFERED 1  
# Requirements for ldap  
RUN apt-get update && apt-get install -y libsasl2-dev python-dev libldap2-dev
libssl-dev  
  
# Copy uwsgi settings  
RUN mkdir /etc/uwsgi/  
COPY confs/uwsgi/uwsgi.ini /etc/uwsgi/  
  
# Python requirements  
RUN pip install git+https://github.com/RavensburgOP/ice-communication.git  
  
WORKDIR /var/www/  
COPY confs/requirements.txt /var/www/  
RUN pip install -r requirements.txt  
  
WORKDIR /var/www/server/  
COPY . .  
  
# Copy entrypoint script  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh

