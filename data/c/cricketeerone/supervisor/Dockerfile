FROM python:2-alpine  
  
RUN pip install -q \--no-cache-dir supervisor \  
&& mkdir -p /etc/supervisord.d /var/log/supervisor \  
&& echo_supervisord_conf > /etc/supervisord.conf \  
&& sed -i 's/^pidfile=.*/pidfile=\/var\/run\/supervisord.pid/'
/etc/supervisord.conf \  
&& sed -i 's/^logfile=.*/logfile=\/var\/log\/supervisor\/supervisord.log/'
/etc/supervisord.conf \  
&& sed -i 's/^;childlogdir=.*/childlogdir=\/var\/log\/supervisor/'
/etc/supervisord.conf \  
&& echo "[include]" >> /etc/supervisord.conf \  
&& echo "files = /etc/supervisord.d/*.conf" >> /etc/supervisord.conf  
  
WORKDIR /etc/supervisord.d  
  
ENTRYPOINT ["/usr/local/bin/supervisord", "-n"]  
CMD []  

