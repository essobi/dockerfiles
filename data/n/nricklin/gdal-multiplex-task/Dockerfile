FROM ubuntu:xenial  
  
RUN apt-get update -y && apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable && apt-get update
-y && apt-get install -y --no-install-recommends \  
gdal-bin \  
python-pip \  
python-setuptools  
  
RUN pip install glob2  
  
ADD task.py /task.py  
  
CMD python /task.py  

