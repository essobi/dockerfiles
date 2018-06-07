FROM debian:latest  
MAINTAINER Ryan Grieve <me@ryangrieve.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
libjpeg-dev \  
zlib1g-dev \  
libfreetype6-dev \  
python \  
python-dev \  
python-pip \  
python-matplotlib \  
&& apt-get clean  
  
RUN pip install -U distribute  
RUN pip install \  
pillow \  
matplotlib \  
numpy  

