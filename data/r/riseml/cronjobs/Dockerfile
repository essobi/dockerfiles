FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install apache2 libapache2-mod-wsgi-py3 \  
build-essential python3 python3-dev \  
curl libpq-dev git  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  
  
RUN mkdir /app && \  
chown www-data:www-data /app  
  
COPY requirements.lock /app/requirements.lock  
RUN pip install -r /app/requirements.lock  
  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_SERVERADMIN admin@localhost  
ENV APACHE_SERVERNAME localhost  
ENV PYTHONPATH=/app  
ENV SSL 1  
ENV PORT 443  
EXPOSE 80  
EXPOSE 443  
# configure apache  
RUN a2enmod ssl rewrite && \  
a2dismod mpm_*  
COPY apache2.conf /etc/apache2/apache2.conf  
  
COPY . /app  
  
CMD python3 -m api.cronjobs.run

