FROM tleyden5iwx/caffe-cpu-master  
MAINTAINER Mike Bartoli "michael.bartoli@pomona.edu"  
RUN apt-get update  
  
RUN apt-get -y --force-yes install python python-dev python-pip build-
essential  
  
RUN pip install pandas matlab numpy jupyter  
  
RUN pip install scikit-image  
  
RUN apt-get -y --force-yes install imagemagick && pip install pillow  
  
RUN mkdir /models && cd /models && wget
http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel  

