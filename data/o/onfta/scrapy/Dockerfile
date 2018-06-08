# khainguyen  
# Dockerfile  
#  
FROM ubuntu:14.04  
MAINTAINER khainguyen "khainguyenptiter@gmail.com"  
RUN apt-get -y update  
  
RUN apt-get install -y gcc g++ python3-dev libssl-dev \  
libxml2-dev libxslt1-dev libffi-dev \  
libmysqlclient-dev python3-pip\  
libtiff5-dev libjpeg8-dev zlib1g-dev \  
libfreetype6-dev liblcms2-dev libwebp-dev \  
tcl8.6-dev tk8.6-dev python3-tk libpq-dev phantomjs  
  
COPY requirements.txt /  
RUN pip3 install -r /requirements.txt  
ENTRYPOINT ["start.sh"]  
  

