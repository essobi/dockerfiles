FROM nvidia/caffe  
  
RUN apt-get update && apt-get -y install python-pip cython wget unzip && apt-
get clean  
  
# common to all platforms  
WORKDIR /opt  
RUN wget --progress=bar:force https://github.com/Junsong-Wang/pet-
breed/archive/master.zip && unzip master.zip && rm -f master.zip  
WORKDIR /opt/pet-breed-master  
RUN pip install -r requirements.txt  
RUN cd data/stanford-dogs && wget --progress=bar:force -O -
http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar |tar xf -  
RUN cd data/stanford-dogs && wget --progress=bar:force -O -
http://vision.stanford.edu/aditya86/ImageNetDogs/annotation.tar |tar xf -  
RUN cd data/stanford-dogs && wget --progress=bar:force -O -
http://vision.stanford.edu/aditya86/ImageNetDogs/lists.tar |tar xf -  
WORKDIR models/bvlc_googlenet  
RUN wget --progress=bar:force
http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel  
RUN sed -ie 's/gpu 0/gpu all/g' ./train.sh  
ADD benchmark.sh /usr/bin/benchmark.sh  
RUN chmod 0755 /usr/bin/benchmark.sh  
  
# nvidia/caffe specific needs  
RUN ln -s /usr/bin/caffe_convert_imageset /usr/bin/convert_imageset  
ADD 00-nimbix /etc/sudoers.d/00-nimbix  
RUN chmod 0440 /etc/sudoers.d/00-nimbix  
  

