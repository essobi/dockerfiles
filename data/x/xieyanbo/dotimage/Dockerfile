# AUTHOR: Xie Yanbo <xieyanbo@gmail.com>  
# DESCRIPTION: Convert profiling output to a image using Gprof2Dot.  
# TO_BUILD: docker build -rm -t dotimage .  
# TO_RUN: docker run -d -p 5000:5000 dotimage  
FROM python:2.7  
RUN apt-get update \  
&& apt-get install -y \  
graphviz \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY . /code  
  
WORKDIR /code  
RUN pip install -r requirements.txt  
  
EXPOSE 5000  
CMD python dotimage.py  

