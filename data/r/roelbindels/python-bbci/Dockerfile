FROM python:3.5.1  
MAINTAINER Roel Bindels <roel.bindels@inetprocess.com>  
  
RUN pip install git+https://github.com/roelbindels/easywebdav.git && pip
install click  
  
ADD bbci.py /usr/bin/bbci.py  
  
# Give execution rights on the cron job  
RUN chmod 0755 /usr/bin/bbci.py

