FROM metocean/ops-bare  
MAINTAINER Andre Lobato andre@metocean.co.nz  
  
RUN yum -y install gcc python-devel python-pip netcdf-devel libffi-devel
openssl-devel tkinter  
RUN yum clean all  
  
COPY . /tmp/radar  
  
RUN echo "-------- Install Requirements ----------" &&\  
cd /tmp &&\  
pip install -U pip setuptools &&\  
pip install numpy --no-cache-dir &&\  
pip install -r /tmp/radar/requirements.txt --no-cache-dir  
  
RUN echo "-------- Install radar package ---------" &&\  
cd /tmp/radar &&\  
python setup.py install  

