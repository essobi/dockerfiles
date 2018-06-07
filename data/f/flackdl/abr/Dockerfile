FROM ubuntu:14.04  
# update and install dependencies  
RUN apt-get update && \  
apt-get install -y \  
wget \  
python-pip \  
python-dev \  
python-setuptools \  
build-essential \  
python-cairo \  
libffi-dev \  
libxml2-dev \  
libxslt1-dev \  
libz-dev \  
libpango1.0-0  
  
RUN easy_install pip  
RUN pip install virtualenv  
RUN virtualenv /opt/virtualenv  
  
# add app  
ADD . /app/  
WORKDIR /app  
  
# install python dependencies  
RUN /opt/virtualenv/bin/pip install -r requirements.txt  
  
# collect static files  
RUN /opt/virtualenv/bin/python manage.py collectstatic --noinput  
  
# run wsgi app  
CMD /opt/virtualenv/bin/gunicorn -w 3 --timeout 20 -b :${PORT:-80} abr.wsgi  

