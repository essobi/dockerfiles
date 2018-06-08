FROM ubuntu:18.04  
  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils  
RUN apt-get -y upgrade  
  
RUN apt-get -y install python3 bash  
RUN apt-get -y install python3-setuptools  
RUN apt-get -y install python3-pip  
RUN apt-get -y install python3-tk  
  
RUN apt-get -y install vim  
  
RUN pip3 install --upgrade pip setuptools  
  
# TODO build TF from source to get optimizations  
RUN pip3 install tf-nightly  
RUN pip3 install matplotlib  
RUN pip3 install scipy  
RUN pip3 install pillow  
RUN pip3 install h5py  
RUN pip3 install bottle cython pandas  
RUN pip3 install keras  
RUN pip3 install pydot  
RUN pip3 install ipython[all]  
  
RUN pip3 install requests  
RUN pip3 install bs4  
RUN pip3 install pandas-datareader  

