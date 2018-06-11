FROM extvos/python  
MAINTAINER "Mingcai SHEN <archsh@gmail.com>"  
RUN apk update && apk add --no-cache build-base linux-headers python-dev
postgresql-client postgresql-libs \  
postgresql-dev git mysql-client mariadb-libs mariadb-dev supervisor \  
&& /usr/bin/echo_supervisord_conf > /etc/supervisord.conf \  
&& echo "[include]" >> /etc/supervisord.conf && echo "files =
/etc/supervisor.d/*.ini" >> /etc/supervisord.conf \  
&& mkdir /root/.pip /root/works /etc/circus.d  
  
COPY circus.ini /etc/circus.ini  
  
RUN pip install --upgrade pip virtualenv circus \  
&& mkdir -p /root/works && cd /root/works \  
&& virtualenv tg2env \  
&& . /root/works/tg2env/bin/activate \  
&& pip install tg.devtools gearbox-tools chaussette waitress simplejson
requests psycopg2 pymongo redis mysql-python  
  
  
VOLUME /etc/supervisor.d  
VOLUME /etc/circus.d  
VOLUME /root/works  
  
EXPOSE 8080  
CMD ["circusd", "/etc/circus.ini"]  

