FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get -y install python-pip libpq-dev python-dev libtiff5-dev
libjpeg8-dev zlib1g-dev \  
libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk -y  
ADD ./ /opt/django-sample/  
WORKDIR /opt/django-sample  
RUN pip install -r requirements.txt  
EXPOSE 8080  
CMD python manage.py migrate --noinput && python manage.py runserver
0.0.0.0:8080

