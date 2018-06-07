FROM gcr.io/tensorflow/tensorflow:latest  
  
RUN apt-get update \  
&& apt-get install -y protobuf-compiler  
  
ENV TF_MODELS_DIR=/tensorflow-models  
ENV TF_MODELS_RESEARCH_DIR=${TF_MODELS_DIR}/research  
  
COPY . ${TF_MODELS_DIR}  
  
WORKDIR ${TF_MODELS_RESEARCH_DIR}  
  
RUN protoc object_detection/protos/*.proto --python_out=.  
  
ENV
PYTHONPATH=$PYTHONPATH:${TF_MODELS_RESEARCH_DIR}:${TF_MODELS_RESEARCH_DIR}/slim  
  
RUN pip install lxml  
  
# Packaging the object detection codes  
RUN python setup.py sdist  
WORKDIR slim  
RUN python setup.py sdist  
  
WORKDIR ${TF_MODELS_RESEARCH_DIR}  

