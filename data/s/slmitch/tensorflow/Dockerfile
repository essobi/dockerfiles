FROM tensorflow/tensorflow:1.7.1-gpu  
  
  
# some more python package needed by our tf custom scripts  
RUN pip install pillow lxml jupyter matplotlib  
  
# needed (optionally) by matplotlib  
# cuda 9.0 requires cudnn 7.0 not 7.1.  
RUN apt-get update && apt-get install -y python-tk && apt-get install -y
--allow-downgrades --no-install-recommends libcudnn7=7.0.5.15-1+cuda9.0
libcudnn7-dev=7.0.5.15-1+cuda9.0 && rm -rf /var/lib/apt/lists/*  

