FROM ubuntu:trusty  
  
WORKDIR /opt  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y python3 python-pip python3-pip python-dev  
RUN apt-get install -y python3-setuptools  
RUN apt-get install -y zlib1g-dev  
RUN apt-get install -y libjpeg8-dev  
RUN apt-get install -y build-essential  
RUN apt-get install -y git  
RUN apt-get install -y software-properties-common  
RUN apt-get install -y libxml2-dev libxslt1-dev  
RUN apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran  
  
RUN add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl  
RUN apt-get update  
RUN apt-get install -y libpcl-all  
  
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib  
RUN python -m pip install --upgrade pip  
  
RUN pip install setuputils  
RUN pip install -U pip wheel setuptools  
RUN pip3 install cython  
RUN pip3 install Pillow  
RUN pip3 install numpy  
RUN pip3 install scipy  
RUN pip3 install msgpack-python  
RUN pip3 install pyusb  
RUN pip3 install Flask  
RUN pip3 install tinydb  
  
RUN git clone https://github.com/flux3dp/fluxclient  
WORKDIR /opt/fluxclient  
RUN python3 setup.py install  
RUN python3 setup.py install  
  
EXPOSE 5000  

