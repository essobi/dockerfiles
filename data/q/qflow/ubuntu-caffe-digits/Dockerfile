FROM qflow/ubuntu-caffe:latest  
MAINTAINER Michal Fojtak <mfojtak@seznam.cz>  
#ENV http_proxy http://proxy.gtm.lilly.com:9000  
#ENV https_proxy http://proxy.gtm.lilly.com:9000  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends graphviz python-dev python-
flask python-flaskext.wtf python-gevent python-h5py python-numpy python-pil
python-pip python-protobuf python-scipy  
  
WORKDIR /workspace  
RUN git clone https://github.com/NVIDIA/DIGITS.git  
ENV DIGITS_ROOT=/workspace/DIGITS  
RUN pip install --upgrade pip  
RUN pip install --upgrade setuptools==33.1.1  
RUN pip install -r $CAFFE_ROOT/python/requirements.txt  
RUN pip install -r $DIGITS_ROOT/requirements.txt  
  
VOLUME /data  
VOLUME /jobs  
WORKDIR $DIGITS_ROOT  
EXPOSE 5000  
ENTRYPOINT ["./digits-devserver"]  

