FROM debian:jessie  
  
ENV PYTHONUNBUFFERED true  
ENV DEBIAN_FRONTEND noninteractive  
ENV PROCESSES=1  
ENV MESOS_ENDPOINT=http://leader.mesos:5050  
RUN apt-get update && \  
apt-get --yes --no-install-recommends install \  
nginx \  
gcc \  
python2.7 \  
python-dev \  
python-setuptools \  
python-pip \  
patch \  
supervisor && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN pip install uwsgi  
  
COPY . /prom_mesos_state_exporter  
RUN pip install -r /prom_mesos_state_exporter/requirements.txt  
COPY proxy_params /etc/nginx/proxy_params  
COPY uwsgi_params /etc/nginx/uwsgi_params  
RUN rm /etc/nginx/sites-enabled/default  
COPY nginx_site.conf /etc/nginx/sites-available/nginx_site.conf  
COPY nginx_gzip.conf /etc/nginx/conf.d/nginx_gzip.conf  
RUN ln -s /etc/nginx/sites-available/nginx_site.conf /etc/nginx/sites-
enabled/nginx_site.conf  
COPY supervisor-app.conf /etc/supervisor/conf.d/supervisor-app.conf  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
EXPOSE 9099  
CMD ["/entrypoint.sh"]  

