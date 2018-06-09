FROM ubuntu:14.04  
MAINTAINER sushanth reddy "sushanth53@gmail.com"  
RUN apt-get -qq update  
RUN apt-get install -y python-dev python-setuptools supervisor git-core  
RUN easy_install pip  
RUN pip install virtualenv  
RUN pip install uwsgi  
RUN virtualenv --no-site-packages /opt/ve/sushanth  
ADD . /opt/apps/sushanth  
ADD .docker/supervisor.conf /opt/supervisor.conf  
ADD .docker/run.sh /usr/local/bin/run  
RUN (cd /opt/apps/sushanth && git remote rm origin)  
RUN (cd /opt/apps/sushanth && git remote add origin
https://github.com/sushanthpy/dockerizedapp.git)  
RUN /opt/ve/sushanth/bin/pip install -r /opt/apps/sushanth/requirements.txt  
RUN (cd /opt/apps/sushanth && /opt/ve/sushanth/bin/python manage.py
makemigrations --noinput)  
RUN (cd /opt/apps/sushanth && /opt/ve/sushanth/bin/python manage.py migrate
--noinput)  
RUN (cd /opt/apps/sushanth && /opt/ve/sushanth/bin/python manage.py test
\--noinput)  
EXPOSE 8000  
CMD ["/bin/sh", "-e", "/usr/local/bin/run"]  

