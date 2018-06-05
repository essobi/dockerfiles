# Version: 3.3.0  
FROM ubuntu:16.04  
MAINTAINER Wassilios Lytras "w.lytras@bluewin.ch"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y apt-utils  
  
# Install requirements for Paramiko (Cryptography) library for SFTP  
RUN apt-get install -y build-essential libssl-dev libffi-dev  
  
# Install Python and Basic Python Tools  
RUN apt-get install -y python  
RUN apt-get install -y python-dev  
RUN apt-get install -y python-distribute  
RUN apt-get install -y python-pip  
  
RUN pip install --upgrade pip  
  
# Install MySQL Driver for Python 2  
RUN apt-get install -y python-mysqldb  
  
# Install PostgreSQL Driver for Python2  
RUN apt-get install -y python-psycopg2  
RUN pip install psycopg2  
  
# Install Python packages  
RUN pip install cherrypy==8.1.2  
RUN pip install genshi==0.7  
RUN pip install django==1.7  
RUN pip install bots==3.3.0  
RUN pip install suds-jurko==0.6  
RUN pip install xlrd==1.0.0  
RUN pip install isoweek==1.3.1  
RUN pip install pyinotify==0.9.6  
RUN pip install paramiko==2.0.2  
RUN pip install pycrypto==2.6.1  
RUN pip install supervisor==3.3.1  
RUN pip install m3-cdecimal==2.3  
  
# Temporary Patch for jobqueueserver in bots 3.3.0  
COPY jobqueueserver.py /usr/local/lib/python2.7/dist-
packages/bots/jobqueueserver.py  
  
# Install DevCron  
# failed, missing hg/mercurial : RUN pip install -e
hg+https://bitbucket.org/dbenamy/devcron#egg=devcron  
RUN pip install https://bitbucket.org/dbenamy/devcron/get/tip.tar.gz  
  
# Copy Supervisord.conf file  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
CMD ["/usr/local/bin/supervisord"]  
  
# Map persisted files to following directories:  
# /usr/local/lib/python2.7/dist-packages/bots/config  
# /usr/local/lib/python2.7/dist-packages/bots/botssys  
# /usr/local/lib/python2.7/dist-packages/bots/usersys  
# BOTS Management Interface  
EXPOSE 8080  
# Supervisord HTTP Server  
EXPOSE 9001

