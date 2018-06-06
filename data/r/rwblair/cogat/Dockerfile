FROM python:3.5  
RUN apt-get update && apt-get install -y \  
libopenblas-dev \  
gfortran \  
libhdf5-dev \  
libgeos-dev \  
netcat  
  
RUN pip install --upgrade pip  
RUN pip install -U docker-compose  
ADD ./requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt  
  
RUN mkdir /code  
WORKDIR /code  
ADD uwsgi.sh /code/  
  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 4000  

