FROM debian:jessie  
  
MAINTAINER ReanGD  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD * /home/  
ADD
https://github.com/twbs/bootstrap/releases/download/v3.3.6/bootstrap-3.3.6-dist.zip
/home/bootstrap.zip  
ADD https://github.com/jquery/jquery/archive/2.1.4.zip /home/jquery.zip  
  
RUN echo en_US.UTF-8 UTF-8 > /etc/locale.gen && \  
echo ru_RU.UTF-8 UTF-8 >> /etc/locale.gen && \  
\  
apt-get update && \  
apt-get install -y \--no-install-recommends locales git supervisor && \  
apt-get install -y \--no-install-recommends redis-server python3-redis && \  
apt-get install -y \--no-install-recommends python3-pip python3-psycopg2
python3-lxml && \  
apt-get install -y \--no-install-recommends python3-django libjs-jquery
celeryd python3-django-celery && \  
apt-get install -y \--no-install-recommends python3-six python3-requests && \  
apt-get install -y \--no-install-recommends uwsgi-plugin-python3 && \  
apt-get install -y \--no-install-recommends libssl-dev nginx && \  
apt-get install -y \--no-install-recommends unzip vim && \  
\  
mkdir -p /www/tmp/ && \  
chmod 777 /www/tmp/ && \  
\  
adduser --system \--no-create-home --disabled-login --disabled-password
--group web_user && \  
rm /etc/nginx/sites-enabled/default && \  
pip3 install -r /home/requirements.txt && \  
/home/install_static.sh && \  
apt-get \--purge remove \--auto-remove -y unzip && \  
/home/clean.sh  
  
ENV LANG ru_RU.UTF-8  
ENV LANGUAGE ru_RU.UTF-8  
  
EXPOSE 80/tcp  
  
VOLUME ["/www/tmp", "/www/app"]  
  
CMD /home/run.sh  

