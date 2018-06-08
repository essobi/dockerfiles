FROM python:2.7-wheezy  
  
LABEL maintainer='George Svachulay @ opsforge.io' \  
email='george.svachulay@opsforge.io' \  
version='v0.1' \  
name='netbox'  
  
WORKDIR /opt/netbox  
  
ENV release='v1.8.4'  
RUN git clone \--depth 1 https://github.com/digitalocean/netbox.git -b master
. && \  
git checkout tags/${release} && \  
apt-get update -qq && \  
apt-get install -y libldap2-dev libsasl2-dev libssl-dev graphviz && \  
pip install gunicorn==17.5 && \  
pip install django-auth-ldap && \  
pip install -r requirements.txt && \  
# mkdir -p /tmp/static && \  
# cp -r /opt/netbox/netbox/static /tmp/static && \  
apt-get clean  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
ADD configuration.docker.py /opt/netbox/netbox/netbox/configuration.py  
ADD gunicorn_config.py /opt/netbox/  
ADD nginx.conf /tmp/netbox-nginx/  
  
SHELL ["/bin/bash","-c"]  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  
EXPOSE 8001  
VOLUME /etc/netbox-nginx/  
VOLUME /opt/netbox/netbox/static/  

