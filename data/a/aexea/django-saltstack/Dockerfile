FROM aexea/django-salt-base  
MAINTAINER Aexea Carpentry  
  
ADD docker_files/saltrc /root/.saltrc  
  
VOLUME ["/etc/salt/pki", "/var/cache/salt", "/var/log/salt",
"/etc/salt/master.d", "/srv/salt"]  
  
EXPOSE 4505 4506 8000  
WORKDIR django_saltstack  

