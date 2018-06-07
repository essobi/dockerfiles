FROM haoyangz/cuda-caffe7.0  
## Install mongodb  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv 7F0CEB10  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0
multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list  
RUN apt-get update  
RUN apt-get install -y mongodb-org emacs24-nox nano curl python-pip python-
numpy python-scipy r-base  
  
## Install Spearmint  
RUN pip install pymongo sklearn lmdb scikit-image scikit-learn protobuf cython
h5py  
RUN git clone https://github.com/HIPS/Spearmint.git /scripts/Spearmint  
RUN pip install -e /scripts/Spearmint  
  
## Git clone codes  
RUN git clone https://haoyangz-ro:12312312@bitbucket.org/haoyangz/cwsm-
wrapper.git /scripts/caffe-with-spearmint-wrapper  
RUN git clone https://haoyangz-ro:12312312@bitbucket.org/haoyangz/caffe-with-
spearmint.git /scripts/caffe-with-spearmint  
RUN git clone https://haoyangz-ro:12312312@bitbucket.org/haoyangz/caffe-
cnn.git /scripts/caffe-cnn  
RUN cd /scripts/caffe-with-spearmint && git checkout personalized  
  
## Make pycaffe  
RUN cd /scripts/caffe && make pycaffe  
  
## Set env  
ENV PYTHONPATH /scripts/caffe-with-spearmint:/scripts/caffe/python:$PYTHONPATH  
RUN chmod -R 777 /scripts  
RUN chmod +x /scripts/caffe-with-spearmint-wrapper/run.py  
ENV DOCKER_FIX '  

