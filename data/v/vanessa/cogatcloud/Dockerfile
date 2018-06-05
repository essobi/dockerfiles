FROM python:2.7  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update && apt-get install -y \  
libopenblas-dev \  
gfortran \  
libhdf5-dev \  
libgeos-dev  
  
MAINTAINER Vanessa Sochat  
  
RUN pip install --upgrade pip  
RUN pip install flask  
RUN pip install numpy  
RUN pip install gunicorn  
RUN pip install pandas  
RUN pip install wordcloud  
RUN pip install Pillow  
RUN pip install matplotlib  
  
ADD . /code  
WORKDIR /code  
  
EXPOSE 5000  

