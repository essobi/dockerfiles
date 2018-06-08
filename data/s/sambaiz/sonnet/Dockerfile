FROM tensorflow/tensorflow:1.2.1-py3  
  
# for configure TensorFlow Headers  
ENV PYTHON_BIN_PATH=/usr/bin/python3 \  
PYTHON_LIB_PATH=/usr/local/lib/python3.5/dist-packages \  
TF_NEED_MKL=0 \  
CC_OPT_FLAGS=-march=native \  
TF_NEED_JEMALLOC=1 \  
TF_NEED_GCP=0 \  
TF_NEED_HDFS=0 \  
TF_ENABLE_XLA=0 \  
TF_NEED_VERBS=0 \  
TF_NEED_OPENCL=0 \  
TF_NEED_CUDA=0  
# install git & bazel, Configure TensorFlow Headers, Build and run the
installer  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" | tee /etc/apt/sources.list.d/bazel.list && \  
curl https://bazel.build/bazel-release.pub.gpg | apt-key add - && \  
apt-get update && \  
apt-get install -y git openjdk-8-jdk bazel && \  
git clone --recursive -b v1.8 https://github.com/deepmind/sonnet && \  
cd sonnet/tensorflow && \  
./configure && \  
cd .. && \  
mkdir /tmp/sonnet && \  
bazel build --config=opt --copt="-D_GLIBCXX_USE_CXX11_ABI=0" :install && \  
./bazel-bin/install /tmp/sonnet python3 && \  
pip3 install distribute /tmp/sonnet/*.whl  
  
# TensorBoard  
EXPOSE 6006  
# IPython  
EXPOSE 8888  
  
WORKDIR "/notebooks"  
  
CMD ["/run_jupyter.sh", "--allow-root"]  

