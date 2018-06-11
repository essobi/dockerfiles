FROM python:3.6.5-onbuild  
COPY requirements.txt /tmp/  
RUN pip install --requirement /tmp/requirements.txt  
COPY . /tmp/  
  
ADD ./frozen_inference_graph.pb /frozen_inference_graph.pb  
ADD ./labelmap.pbtxt /labelmap.pbtxt  
ADD ./Object_detection_image2.py /Object_detection_image2.py  
ADD ./run.sh /run.sh  
ADD ./2122.jpg /2122.jpg  

