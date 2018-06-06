FROM python:3.6-onbuild  
ENTRYPOINT ["/usr/src/app/netbox/manage.py"]  
RUN apt update -q \  
&& apt install -qy libldap2-dev libsasl2-dev libssl-dev graphviz  
RUN pip install django-auth-ldap napalm==2.3.0  
RUN cp /usr/src/app/netbox/netbox/configuration.docker.py
/usr/src/app/netbox/netbox/configuration.py  

