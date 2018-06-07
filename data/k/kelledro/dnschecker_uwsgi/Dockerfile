FROM ubuntu  
MAINTAINER kelledro  
RUN \  
apt-get update && \  
apt-get install -y python-dev python-pip gcc && \  
pip install uwsgi boto  
ADD
https://raw.githubusercontent.com/kelledro/dnsChecker/master/app/checker.py
/var/www/  
ADD
https://raw.githubusercontent.com/kelledro/dnsChecker/master/app/checker.ini
/var/www/  
WORKDIR /var/www  
CMD uwsgi --ini checker.ini  

