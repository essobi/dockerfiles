FROM ubuntu:16.04  
MAINTAINER kevthehermit (https://github.com/kevthehermit/mollusc)  
  
# Set some User variables  
ENV MONGO_URI mongodb://localhost  
ENV AUTH True  
ENV MAP_KEY enter key here  
ENV ADMIN_PASS password  
  
# Switch to root user  
USER root  
  
# Install OS dependancies  
RUN apt-get update && apt-get install -yq \  
git \  
curl \  
libjpeg-dev \  
python-dev \  
python-pip \  
python-numpy \  
python-matplotlib \  
geoip-database \  
apache2 \  
libapache2-mod-wsgi  
  
# Get the maxmind database for ip lookup  
RUN cd /tmp && \  
curl -sSL
http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz >
GeoLite2-City.mmdb.gz && \  
gzip -d GeoLite2-City.mmdb.gz && \  
mv GeoLite2-City.mmdb /usr/share/GeoIP/  
  
# Get Mollusc  
RUN cd /opt/ && \  
git clone https://github.com/kevthehermit/mollusc.git  
  
# Python requirements  
RUN cd /opt/mollusc && \  
pip install -r requirements.txt  
  
# Create first user  
RUN cd /opt/mollusc && \  
python manage.py migrate && \  
echo "from django.contrib.auth.models import User;
User.objects.create_superuser('admin', 'admin@example.com', '$ADMIN_PASS')" |
python manage.py shell && \  
python manage.py collectstatic --noinput  
  
# Vhost  
RUN chown -R www-data:www-data /opt/mollusc  
ADD mollusc_apache.conf /etc/apache2/sites-available/  
  
RUN cd /etc/apache2/sites-available/ && \  
a2dissite 000-default.conf && \  
a2ensite mollusc_apache.conf && \  
service apache2 restart  
  
# Setup and RUN  
EXPOSE 80  
WORKDIR /opt/mollusc  
ADD start.sh start.sh  
CMD /bin/bash /opt/mollusc/start.sh

