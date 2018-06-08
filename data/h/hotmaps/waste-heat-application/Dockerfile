#  
# hotmaps/waste-heat-application image Dockerfile  
#  
# Python 2.7 / 3.5  
# Flask 0.12  
# Flask-RESTful 0.3.5  
# Flask-Login 0.4.0  
# Flask-Bcrypt 0.5  
# PuLP  
# Math  
# NumPy  
# Pandas  
# gdal  
# pyqgis  
#  
from ubuntu:16.04  
maintainer Dockerfiles  
  
# setup volume  
RUN mkdir /data  
VOLUME /data  
  
# Build commands  
RUN apt-get update && apt-get dist-upgrade -y && apt-get autoremove -y  
  
# Install required software  
RUN apt-get install -y \  
software-properties-common \  
wget \  
curl \  
git \  
build-essential \  
checkinstall \  
libreadline-gplv2-dev \  
libncursesw5-dev \  
libssl-dev \  
libsqlite3-dev \  
tk-dev \  
libgdbm-dev \  
libc6-dev \  
libbz2-dev \  
python2.7 \  
python3.5 \  
python-pip \  
python3-pip \  
python-dev \  
python3.5-dev \  
python-setuptools \  
python3-setuptools \  
nginx \  
supervisor  
  
# Install GRASS / pyqgis  
RUN add-apt-repository ppa:ubuntugis/ubuntugis-unstable  
RUN sh -c 'echo "deb http://qgis.org/ubuntugis xenial main" >>
/etc/apt/sources.list'  
RUN sh -c 'echo "deb-src http://qgis.org/ubuntugis xenial main " >>
/etc/apt/sources.list'  
RUN wget -O - http://qgis.org/downloads/qgis-2016.gpg.key | gpg --import  
RUN gpg --fingerprint 073D307A618E5811  
RUN gpg --export \--armor 073D307A618E5811 | apt-key add -  
#RUN add-apt-repository "deb-src http://qgis.org/ubuntugis xenial main"  
#RUN add-apt-repository "deb http://ppa.launchpad.net/ubuntugis/ubuntugis-
unstable/ubuntu xenial main"  
#RUN apt-get update && apt-get install -y grass  
RUN apt-get update && apt-get install -y qgis python-qgis gdal-bin  
  
RUN pip3 install virtualenv  
RUN virtualenv -p python3 /home/docker/venvs/venv3  
  
# install uwsgi now because it takes a little while  
run pip3 install uwsgi  
  
# install nginx  
run apt-get install -y software-properties-common python-software-properties  
run apt-get update  
run add-apt-repository -y ppa:nginx/stable  
run apt-get install -y sqlite3  
  
# install our settings  
add . /home/docker/settings/  
  
# setup all the configfiles  
run echo "daemon off;" >> /etc/nginx/nginx.conf  
run rm /etc/nginx/sites-enabled/default  
run ln -s /home/docker/settings/nginx-app.conf /etc/nginx/sites-enabled/  
run ln -s /home/docker/settings/supervisor-app.conf /etc/supervisor/conf.d/  
  
# install backend - python 2.7  
RUN virtualenv -p python2.7 /home/docker/venvs/venv2  
  
# run pip install  
run /home/docker/venvs/venv3/bin/pip install -r
/home/docker/settings/python3/requirements.txt  
run /home/docker/venvs/venv2/bin/pip install -r
/home/docker/settings/python2/requirements.txt  
  
WORKDIR /data  
  
expose 80  
cmd ["supervisord", "-n"]  

