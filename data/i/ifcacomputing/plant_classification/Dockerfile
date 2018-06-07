FROM nvidia/cuda:8.0-devel-ubuntu16.04  
MAINTAINER Alvaro Lopez <aloga@ifca.unican.es  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
curl \  
build-essential \  
git \  
python-pip \  
python-dev \  
python-setuptools \  
python-flask \  
python-requests \  
python-pil \  
&& \  
apt-get clean  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libopenblas-dev \  
python-numpy \  
python-scipy \  
&& \  
apt-get clean  
  
RUN pip install --upgrade https://github.com/Theano/Theano/archive/master.zip  
RUN pip install --upgrade
https://github.com/Lasagne/Lasagne/archive/master.zip  
  
WORKDIR /opt/resnet50_plants  
  
COPY data data  
COPY scripts scripts  
COPY webpage webpage  
  
ENV SWIFT_CONTAINER https://cephrgw01.ifca.es:8080/swift/v1/Plants/  
ENV THEANO_TR_WEIGHTS resnet50_6182classes_100epochs.npz  
ENV THEANO_TR_JSON resnet50_6182classes_100epochs.json  
ENV SYNSETS synsets_binomial.txt  
ENV INFO info.txt  
  
RUN curl -o ./webpage/model_files/training_weights/${THEANO_TR_WEIGHTS} \  
${SWIFT_CONTAINER}${THEANO_TR_WEIGHTS}  
  
RUN curl -o ./webpage/model_files/training_info/${THEANO_TR_JSON} \  
${SWIFT_CONTAINER}${THEANO_TR_JSON}  
  
RUN curl -o ./webpage/model_files/data/synsets.txt \  
${SWIFT_CONTAINER}${SYNSETS}  
  
RUN curl -o ./webpage/model_files/data/info.txt \  
${SWIFT_CONTAINER}${INFO}  
  
EXPOSE 5000  
WORKDIR ./webpage/webpage_files  
  
CMD python webpage_demo.py 0.0.0.0  
  

