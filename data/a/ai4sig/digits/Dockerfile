FROM nvidia/digits:6.0  
LABEL maintainer "AI4SIG"  
# Correct DIGITS version  
COPY version.py /usr/local/lib/python2.7/dist-packages/digits/  
# Modify Caffe LeNet, AlexNet and GoogLeNet  
COPY standard-networks/caffe/* /usr/local/lib/python2.7/dist-
packages/digits/standard-networks/caffe/  
  
# Add Torch weight-init  
COPY tools/torch/weight-init.lua /usr/local/lib/python2.7/dist-
packages/digits/tools/torch/  
# Modify Torch LeNet  
COPY standard-networks/torch/lenet.lua /usr/local/lib/python2.7/dist-
packages/digits/standard-networks/torch/  
# Add Fashion-MNIST downloader  
COPY download_data/* /usr/local/lib/python2.7/dist-
packages/digits/download_data/  
  
# Install all plugins  
WORKDIR /tmp/  
ADD DIGITS-6.0.1-plugins.tar.gz .  
RUN pip install -e /tmp/DIGITS-6.0.1/plugins/data/bAbI/ && \  
pip install -e /tmp/DIGITS-6.0.1/plugins/data/gan/ && \  
pip install -e /tmp/DIGITS-6.0.1/plugins/data/imageGradients/ && \  
pip install -e /tmp/DIGITS-6.0.1/plugins/data/sunnybrook/ && \  
pip install -e /tmp/DIGITS-6.0.1/plugins/data/textClassification/ && \  
pip install -e /tmp/DIGITS-6.0.1/plugins/view/gan/ && \  
pip install -e /tmp/DIGITS-6.0.1/plugins/view/imageGradients/ && \  
pip install -e /tmp/DIGITS-6.0.1/plugins/view/textClassification/  

