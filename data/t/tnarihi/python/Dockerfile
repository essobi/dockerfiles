FROM nvidia/cuda:7.5-cudnn4-devel  
RUN apt-get update  
RUN apt-get install -y python  
RUN apt-get install -y python-dev  
RUN apt-get install -y python-setuptools  
RUN apt-get install -y python-pip  
RUN apt-get install -y python-numpy  
RUN apt-get install -y python-scipy  
RUN apt-get install -y python-matplotlib  
RUN apt-get remove -y python-numpy python-scipy python-matplotlib  
RUN pip install numpy  
RUN apt-get install -y libatlas-dev  
RUN apt-get install -y liblapack-dev  
RUN apt-get install -y gfortran  
RUN pip install scipy  
RUN apt-get install -y libfreetype6-dev  
RUN apt-get install -y pkg-config  
RUN pip install matplotlib  
RUN apt-get install -y libzmq-dev  
RUN pip install ipython  
RUN pip install jupyter  
RUN pip install cython  

