FROM python:2.7  
  
MAINTAINER Boris Serebrov  
  
RUN apt-get update && apt-get install -y \  
gfortran \  
# needed for shapely  
libgeos-c1 libgeos-dev \  
libpq-dev \  
libblas-dev liblapack-dev \  
libmysqlclient-dev \  
python-dev  
  
# Install pandas/ numpy / scipy / scikit-learn and their deps  
RUN pip install six==1.9.0 \  
numpy==1.9.2 \  
scipy==0.15.1 \  
scikit-learn==0.16.1  
  
RUN pip install pandas==0.16.1  
  
RUN pip install Flask==0.10.1 \  
boto==2.38.0 \  
pytz==2015.4 \  
py_descriptive_statistics==0.2 \  
simplejson==3.6.5 \  
xmltodict==0.9.2 \  
markdown2==2.3.0 \  
pygments==2.0.2 \  
pyzmq==13.0.2 \  
protobuf==3.0.0b2 \  
protobuf-to-dict==0.1.0 \  
shapely==1.5.13 \  
psycopg2==2.6.1 \  
SQLAlchemy==1.0.6 \  
Flask-SQLAlchemy-Session==1.1 \  
alembic==0.7.6 \  
sqlalchemy-utils==0.30.12 \  
MySQL-python==1.2.5 \  
pprofile==1.7.3 \  
requests==2.9.1  

