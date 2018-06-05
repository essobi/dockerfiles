FROM python:3  
MAINTAINER Lucas Sanders <sanders@whoop.com>  
  
# Fetch dependencies  
# (work around some kind of repo bug)  
RUN apt-get update || apt-get update  
RUN apt-get -y install gfortran libatlas-base-dev  
RUN apt-get clean  
RUN pip install \  
"numpy>=1.8.0,<1.9.0" \  
"scipy>=0.13.2,<0.14.0" \  
"flask>=0.10.1" \  
"gunicorn>=19.1.1,<20.0" \  
"python-dateutil>=2.2.0,<2.3.0" \  
"pgpasslib>=1.0.1" \  
"psycopg2>=2.5.4"  

