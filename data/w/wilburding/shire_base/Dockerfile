FROM wilburding/py_boost  
  
RUN apt-get update && apt-get install -y \  
enchant \  
libfreetype6-dev \  
libjpeg-dev \  
libpng12-dev \  
liblapack-dev \  
libopenblas-dev \  
gfortran  
# liblapack-dev/libopenblas-dev/gfortran for scipy  
COPY pip_req.txt /usr/src/  
RUN pip install -r /usr/src/pip_req.txt  
  
RUN apt-get remove -y gfortran \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache  
  
# fix uid and gid to be same as host www  
RUN groupadd -g 1000 www && useradd -g www -u 1000 www  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
VOLUME ['/usr/src/app', '/var/log']  
  
CMD ["python"]  

