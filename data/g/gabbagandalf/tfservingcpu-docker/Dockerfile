FROM ubuntu:14.04  
  
RUN apt-get update && apt-get install -y \  
wget \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget http://ci.tensorflow.org/job/serving-master-cpu/ws/bazel-
bin/tensorflow_serving/model_servers/tensorflow_model_server -P /usr/bin && \  
chmod +x /usr/bin/tensorflow_model_server  

