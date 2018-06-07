FROM ubuntu:16.04  
MAINTAINER Andrew Cencini <andrew@vapor.io>  
  
ADD requirements.txt .  
  
# install dependencies  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
sudo \  
cron \  
iputils-ping \  
iproute2 \  
make \  
python \  
python-dev \  
python-distribute \  
python-pip && \  
pip2 install --upgrade pip && \  
pip2 install wheel setuptools && \  
pip2 install -I -r requirements.txt && \  
apt-get remove -y \  
build-essential \  
python-pip && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# set ownership of the logs directory such that the flask app can write to it  
RUN mkdir /logs && \  
chown :www-data /logs && \  
chmod 775 /logs && \  
ln -sf /proc/1/fd/1 /logs/err  
  
RUN mkdir /etc/uwsgi && \  
chown -R www-data:www-data /etc/uwsgi  

