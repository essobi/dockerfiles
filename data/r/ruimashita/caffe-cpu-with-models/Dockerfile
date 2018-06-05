FROM ruimashita/caffe-cpu:rc2  
  
# ignore sha1 download model script  
ADD download_model_binary_ignore_sha1.py
scripts/download_model_binary_ignore_sha1.py  
  
# get latest sh  
RUN git fetch && git checkout origin/master --
scripts/download_model_from_gist.sh  
  
###  
# download models  
###  
  
# bvlc_reference_caffenet  
RUN python scripts/download_model_binary.py models/bvlc_reference_caffenet  
  
# VGG_ILSVRC_16_layers  
# https://gist.github.com/ksimonyan/211839e770f7b538e2d8#file-readme-md  
RUN ./scripts/download_model_from_gist.sh 211839e770f7b538e2d8 \  
&& cd models/211839e770f7b538e2d8 \  
&& wget
http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_16_layers.caffemodel  
  
# GoogLeNet_cars  
# https://gist.github.com/bogger/b90eb88e31cd745525ae  
# RUN ./scripts/download_model_from_gist.sh b90eb88e31cd745525ae \  
# && python scripts/download_model_binary_ignore_sha1.py
models/b90eb88e31cd745525ae  
  
# Place-CNN Places205-VGG  
# http://places.csail.mit.edu/downloadCNN.html  
# RUN cd models && wget http://places.csail.mit.edu/model/places205vgg.tar.gz
\  
# && tar zxvf places205vgg.tar.gz  
  
  
###  
# download data  
###  
  
# download ilsvrc12 data  
RUN cd data/ilsvrc12 && ./get_ilsvrc_aux.sh  
  
# download flickr_style data  
# RUN python examples/finetune_flickr_style/assemble_data.py --workers=-1
--images=2000 --seed=831486  

