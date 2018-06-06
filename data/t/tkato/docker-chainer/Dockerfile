FROM ubuntu:14.04  
MAINTAINER KATO Tomohiro  
  
RUN mkdir /work  
  
RUN apt-get update  
  
RUN apt-get install -y libhdf5-dev  
RUN apt-get install -y python-pip  
RUN apt-get install -y python-dev  
RUN apt-get install -y build-essential  
RUN apt-get install -y python-matplotlib  
RUN apt-get install -y vim  
RUN apt-get install -y git  
  
RUN pip install -U setuptools  
RUN pip install python  
RUN pip install cython  
RUN pip install numpy  
RUN pip install pandas  
RUN pip install h5py  
RUN pip install ipython  
RUN pip install jupyter  
  
RUN pip install chainer==1.6.0  
  
ENV HOME /root  
  
EXPOSE 8888  
EXPOSE 80  
EXPOSE 8080  
VOLUME /work  
  
WORKDIR /work  
  
CMD ipython notebook --no-browser --port 8888 --ip=*  

