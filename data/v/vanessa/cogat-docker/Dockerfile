FROM python:3.5  
MAINTAINER vsochat@stanford.edu  
  
RUN apt-get update && apt-get install -y \  
libopenblas-dev \  
gfortran \  
libhdf5-dev \  
libgeos-dev \  
netcat  
  
RUN pip install --upgrade pip  
RUN pip install -U docker-compose  
RUN pip install numpy==1.10.2 \  
cython  
RUN pip install decorator==4.0.6  
RUN pip install Django==1.9  
RUN pip install django-crispy-forms==1.5.2  
RUN pip install djangorestframework==3.3.2  
RUN pip install pandas==0.17.1  
RUN pip install py2neo==2.0.8  
RUN pip install python-dateutil==2.4.2  
RUN pip install PyYAML==3.11  
RUN pip install requests==2.9.0  
RUN pip install simplegeneric==0.8.1  
RUN pip install six==1.10.0  
RUN pip install cognitiveatlas  
RUN pip install django-allauth  
RUN pip install psycopg2  
RUN pip install uwsgi  
RUN pip install django-allauth  
  
RUN mkdir /code  
WORKDIR /code  
ADD uwsgi.sh /code/  
  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 4000  

