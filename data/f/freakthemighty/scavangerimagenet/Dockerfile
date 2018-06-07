FROM b.gcr.io/tensorflow/tensorflow:latest-devel  
  
WORKDIR /tensorflow/tensorflow/models/image/imagenet  
RUN python ./classify_image.py  
ADD . /imagenet  
WORKDIR /imagenet  
RUN pip install -r requirements.txt  
EXPOSE 80  
CMD ["python", "-u", "/imagenet/classify_image.py"]  
  

