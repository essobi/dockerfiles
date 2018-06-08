FROM flyingmouse/caffe  
MAINTAINER Haoming Wang <haoming.exe@gmail.com>  
  
RUN cd $CAFFE_ROOT && ./data/ilsvrc12/get_ilsvrc_aux.sh  
  
ADD web-demo /opt/web-demo  
WORKDIR /opt/web-demo  
  
RUN pip install -r requirements.txt && \  
pip install protobuf  
  
EXPOSE 5000  
CMD ["python", "app.py"]  

