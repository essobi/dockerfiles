FROM bluedragonx/wsgi:latest  
MAINTAINER Ryan Bourgeois <bluedragonx@gmail.com>  
  
# set up the container environment  
EXPOSE 80  
ENTRYPOINT ["/sbin/my_init"]  
  
# install packages  
RUN apt-get update -qy && \  
apt-get install -qy build-essential git-core libevent-dev libffi-dev liblzma-
dev libssl-dev python-dev python-pip && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install registry source  
RUN rm -rf /app && \  
git clone \--recursive --depth 1 https://github.com/dotcloud/docker-
registry.git /app && \  
pip install -r /app/requirements.txt && \  
rm -rf /app/.git /app/config/*  
  
# create directories and add files we need  
RUN mkdir -p /data && chown app:app /data  
ADD files/nginx.conf /app/  
ADD files/uwsgi.yml /app/  
ADD files/config.yml /app/config/  
RUN chown app /app/config/config.yml && \  
chmod 400 /app/config/config.yml && \  
chmod 644 /app/nginx.conf /app/uwsgi.yml  

