FROM docku/uwsgi-python2  
MAINTAINER Jon Chen <bsd@voltaire.sh>  
  
VOLUME ["/etc/nginx/enabled-sites/"]  
  
ADD etc/nginx/mc-voltaire-sh.conf /etc/nginx/enabled-sites/  
ADD etc/uwsgi/voltairemc.ini /etc/uwsgi/voltairemc.ini  
ADD app /srv/http/  
  
RUN pacman -Syu --needed --noconfirm python2-pip  
RUN /usr/bin/pip2 install -r /srv/http/requirements.txt --upgrade  
  
ADD run.sh /service/uwsgi-voltairemc/run  

