FROM ubuntu:14.10  
MAINTAINER Bertrand Bordage, bordage.bertrand@gmail.com  
  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install postgresql postgresql-server-dev-9.4 build-essential \  
python-pip python-dev python-opencv python-numpy \  
&& apt-get -y build-dep pillow \  
&& apt-get clean \  
&& apt-get -y autoremove  
  
ADD https://github.com/torchbox/wagtaildemo/archive/master.tar.gz /  
RUN tar -xvf /master.tar.gz -C / && rm /master.tar.gz  
  
WORKDIR /wagtaildemo-master/  
  
RUN pip install -r requirements.txt  
# Uncomment if you want the latest wagtail version  
# RUN pip install https://github.com/torchbox/wagtail/archive/master.tar.gz  
RUN sed -i 's/# Database administrative login by Unix domain socket/&\nlocal
all postgres trust/' /etc/postgresql/9.4/main/pg_hba.conf  
RUN service postgresql start \  
&& psql -U postgres -c 'CREATE DATABASE wagtaildemo;' \  
&& python manage.py migrate \  
&& python manage.py load_initial_data  
RUN echo 'WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = True' >>
wagtaildemo/settings/base.py  
  
# Change your language code using this  
# RUN sed -i "s/LANGUAGE_CODE = 'en-gb'/LANGUAGE_CODE = 'fr'/"
wagtaildemo/settings/base.py  
CMD service postgresql start && python manage.py runserver 0.0.0.0:8000  
EXPOSE 8000  

