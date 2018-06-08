FROM python:2.7  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get update \  
&& apt-get install -y gfortran libsqlite3-dev libblas-dev liblapack-dev \  
&& apt-get autoremove -y \  
&& apt-get clean  
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  

