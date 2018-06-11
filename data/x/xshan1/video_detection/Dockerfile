FROM tensorflow/tensorflow:latest-py3  
  
RUN apt-get update && apt-get -y install git python-opencv wget protobuf-
compiler debconf-utils apt-transport-https  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections  
RUN apt-get install -y ttf-mscorefonts-installer  
RUN fc-cache  
RUN pip3 install Flask opencv-python redis ipython  
  
RUN mkdir /mobilenet  
RUN git clone https://github.com/tensorflow/models.git  
RUN wget
http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2017_11_17.tar.gz
&& \  
tar -xvzf ssd_mobilenet_v1_coco_2017_11_17.tar.gz -C /mobilenet  
  
RUN mkdir /streamapp  
RUN cp -R models/research/object_detection /streamapp  
RUN cd /streamapp && protoc object_detection/protos/*.proto --python_out=.  
WORKDIR /streamapp  
RUN sed -i "s#'arial.ttf',
24#'/usr/share/fonts/truetype/msttcorefonts/arial.ttf', 24#g"
object_detection/utils/visualization_utils.py  
COPY . .  
  
EXPOSE 5001  
CMD python3 app-zombies.py  

