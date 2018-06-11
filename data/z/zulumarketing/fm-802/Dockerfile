FROM zulumarketing/python-app  
MAINTAINER Carlos Killpack <carlos@zulumarketing.com>  
  
COPY bin/chain.sh /usr/bin/chain  
COPY supervisor.conf /etc/supervisor/conf.d/fm-802.conf  
COPY app/ /srv/fm-802  
  
RUN chown -R www-data /srv/fm-802  
  
WORKDIR /srv/fm-802  
USER www-data  
RUN virtualenv \--python=python3.4 env > /dev/null \  
&& env/bin/pip install -r requirements.txt > /dev/null  
  
USER root  
EXPOSE 80 443  

