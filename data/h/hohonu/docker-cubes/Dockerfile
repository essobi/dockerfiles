FROM ubuntu:14.04  
MAINTAINER pdodds philip@hohonu.com  
RUN apt-get update  
RUN apt-get install -y python curl postgresql-9.3 postgresql-server-dev-9.3
python-dev  
  
# Install Pip  
RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py
| python2.7  
  
# Install Cubes  
RUN pip install cubes  
RUN pip install flask  
RUN pip install redshift-sqlalchemy  
RUN pip install sqlalchemy  
  
# Mountpoint for your cubes project  
VOLUME ["/data"]  
  
# Cubes port  
EXPOSE 5000  
CMD ["slicer","serve","slicer.ini"]  

