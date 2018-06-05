FROM python:2.7  
RUN apt-get update && \  
apt-get install -y \  
libboost-all-dev \  
libblitz0-dev \  
cmake \  
libhdf5-dev \  
libgif-dev \  
liblapack-dev && \  
apt-get clean  
RUN pip install zc.buildout  
COPY buildout.cfg /app/buildout.cfg  
WORKDIR /app  
RUN buildout  
COPY app.py /app/app.py  
CMD bin/python app.py  
EXPOSE 5000  

