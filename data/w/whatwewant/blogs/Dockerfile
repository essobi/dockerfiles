# Online Learning Platform  
#  
# Version 1.0.1  
# auto build from my github project: https://github.com/whatwewant/OLP  
FROM ubuntu:14.04  
# make sure the package repository is up to date  
RUN apt-get -y update && apt-get install -y python python-pip  
RUN echo "mysql-server-5.6 mysql-server/root_password password pw123456" |
sudo debconf-set-selections  
RUN echo "mysql-server-5.6 mysql-server/root_password_again password
pw123456"| sudo debconf-set-selections  
RUN apt-get -y install mysql-server-5.6  
RUN apt-get -y install python-dev libmysqlclient-dev libjpeg-dev  
RUN apt-get -y install git nginx  
RUN apt-get -y install supervisor  
RUN rm -rf /etc/nginx/sites-available/default  
  
RUN cd /opt; git clone -b working https://github.com/whatwewant/OLP.git  
# RUN cd /opt/OLP; pip install -r requirements.txt  
RUN rm -rf /opt/OLP/OLP/settings.py  
  
ADD default /etc/nginx/sites-available/default  
ADD settings.py /opt/OLP/OLP/settings.py  
ADD supervisor.conf /etc/supervisor/conf.d/supervisor.conf  
  
RUN service mysql start  
ADD mysql-init.sh /opt/mysql-init.sh  
RUN /bin/bash /opt/mysql-init.sh  
  
ADD config_python.sh /opt/config_python.sh  
ADD uwsgi.ini /opt/OLP/uwsgi.ini  
RUN /bin/bash /opt/config_python.sh  
RUN pip install uwsgi  
ADD run.sh /opt/run.sh  
RUN /bin/bash /opt/run.sh  
  
ADD JianShu.py /opt/OLP  
ADD po.sh /opt/po.sh  
ADD cron /opt/cron  
RUN /usr/bin/crontab /opt/cron  
  
RUN apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]  
  
MAINTAINER Eason, uniquecolesmith@gmail.com  

