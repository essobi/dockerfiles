FROM tensorflow/tensorflow:1.7.0  
RUN rm -rf ./*  
RUN apt-get update && apt-get install -y git  
RUN pip install tfcoreml  
RUN git clone https://github.com/tensorflow/tensorflow --branch v1.6.0
--single-branch  
RUN python ./tensorflow/tensorflow/examples/image_retraining/retrain.py; exit
0  
COPY coreml.py run.sh ./  
  
CMD ./run.sh  

