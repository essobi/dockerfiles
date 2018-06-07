# see https://hub.docker.com/r/tensorflow/tensorflow/tags/  
FROM gcr.io/tensorflow/tensorflow:latest-py3  
  
WORKDIR /tensorflow  
ADD . /tensorflow/models  
  
# Grab required packages  
RUN apt-get update  
RUN apt-get install -y git protobuf-compiler  
  
# Install required python packages  
RUN pip install Cython  
RUN pip install jupyter  
RUN pip install matplotlib  
  
# Get cocoapi  
RUN git clone https://github.com/cocodataset/cocoapi.git  
WORKDIR /tensorflow/cocoapi/PythonAPI  
RUN make  
RUN cp -r pycocotools /tensorflow/models/research/  
  
# Compile protos  
WORKDIR /tensorflow/models/research  
RUN protoc object_detection/protos/*.proto --python_out=.  
  
# Append PYTHONPATH  
ENV
PYTHONPATH="/:$PYTHONPATH:/tensorflow/models/research:/tensorflow/models/research/slim"  
WORKDIR /tensorflow/models/object_detection  
  
# Make sure it works  
#CMD ["python",
"/tensorflow/models/research/object_detection/builders/model_builder_test.py"]  

