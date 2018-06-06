FROM tensorflow/tensorflow:1.3.0-devel  
#FROM gcr.io/tensorflow/tensorflow:latest  
MAINTAINER ki-adi-mundi  
  
# Downloading inception v3 2016 model  
RUN mkdir /ready-models && \  
cd /ready-models && \  
curl -O
http://download.tensorflow.org/models/image/imagenet/inception-v3-2016-03-01.tar.gz
&& \  
tar xzf inception-v3-2016-03-01.tar.gz  
  
# installing models  
RUN cd / && \  
git clone https://github.com/tensorflow/models.git && \  
cd /models/research/inception && \  
bazel build //inception:all  
  
RUN cd / && mkdir /train && mkdir /train/images && mkdir /train/output  
  
COPY *.sh /  
RUN chmod +x /*.sh  
  
VOLUME ["/train/images/", "/train/output/"]  
  
WORKDIR "/"  
  
CMD ["/process_training.sh"]  

