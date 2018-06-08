FROM debian:latest  
RUN apt-get -y -q update  
  
RUN apt-get -y install python3-pip libpython3.4  
RUN apt-get -y install libxerces-c3.1 apache2 libapache2-mod-wsgi-py3
python3-psycopg2  
RUN apt-get -y install vim wget  
RUN pip3 install openpyxl setuptools  
  
ADD resources/ /resources  
WORKDIR /resources  
RUN dpkg -i frepple_*.deb  
RUN apt-get -f -y -q install  
  
RUN tar -zxvf frepple_3.0.tar.gz  
WORKDIR /resources/django-frepple_3.0  
RUN python3 setup.py install  
RUN pip3 install djangorestframework  
  
ADD settings.py /etc/frepple/djangosettings.py  
ADD start.sh /usr/bin/startfrepple  
CMD ["startfrepple"]  

