FROM nvidia/cuda:latest  
  
RUN apt-get update  
RUN apt-get install software-properties-common python-software-properties -y  
RUN add-apt-repository ppa:jonathonf/python-3.6 -y  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y python3.6 virtualenv python3-pip python3.6-dev  
RUN apt-get install -y awscli  
RUN apt-get install -y swig  
RUN apt-get install -y git  
RUN apt-get install -y libboost-regex-dev libboost-system-dev  
RUN apt-get install -y wget unzip  
RUN apt-get install -y python3.6-tk tk8.6-dev tk-dev  
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6
60  
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 60  
RUN update-alternatives --install /usr/bin/python3-config python3-config
/usr/bin/python3.6-config 60  
RUN update-alternatives --install /usr/bin/python-config python-config
/usr/bin/python3.6-config 60  
RUN pip3 install --upgrade pip setuptools  
RUN pip3 install numpy psycopg2 pandas python-dateutil SQLAlchemy  
RUN pip3 install scipy Flask "yarl<0.11.0" s3fs pika requests scikit-learn
cython six  
RUN pip3 install matplotlib bottleneck  
RUN pip3 install GPy  
RUN pip3 install https://github.com/SheffieldML/GPyOpt/archive/master.zip  
RUN wget https://cmake.org/files/v3.9/cmake-3.9.1-Linux-x86_64.tar.gz  
RUN tar xf cmake-3.9.1-Linux-x86_64.tar.gz && mv cmake-3.9.1-Linux-x86_64
/opt/cmake  
RUN ln -s /opt/cmake/bin/cmake /usr/bin/cmake  
RUN ln -s /usr/lib/x86_64-linux-gnu/libpython3.6m.so /usr/lib/libpython3.6m.so  
  
COPY hfst /usr/local/hfst  
WORKDIR /usr/local/hfst  
RUN swig -c++ -python hfst_lookup.i  
RUN python3.6 setup.py install  

