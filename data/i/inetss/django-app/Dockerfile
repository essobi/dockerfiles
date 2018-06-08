FROM ubuntu:16.04  
ENV LANG=en_US.UTF-8  
RUN \  
locale-gen en_US.UTF-8 && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
nginx \  
python \  
python-dev \  
python-pip \  
python3 \  
python3-dev \  
python3-pip \  
sudo \  
supervisor \  
uwsgi \  
uwsgi-plugin-python \  
uwsgi-plugin-python3 && \  
rm -rf /var/lib/apt/lists/*  
  
COPY supervisor/app.conf /etc/supervisor/conf.d/  
COPY uwsgi/app.ini /etc/uwsgi/apps-enabled/  
COPY nginx/app.conf /etc/nginx/sites-enabled/default  
COPY entrypoint.sh /  
COPY setup /setup  
  
# Default Ubuntu entrypoint is bash, keep it  
CMD ["/entrypoint.sh"]  
  
EXPOSE 80  
RUN mkdir -p /app/var/media && chown www-data /app/var/media  
VOLUME /app/var/media  
  
# Rare changes  
ONBUILD COPY requirements.* /requirements/  
ONBUILD RUN /setup/setup_requirements.sh  
  
# Frequent changes  
ONBUILD COPY . /app/  
ONBUILD RUN touch /app/var/installed.flag  

