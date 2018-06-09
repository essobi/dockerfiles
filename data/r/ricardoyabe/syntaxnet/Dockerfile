FROM tensorflow/syntaxnet  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
g++ \  
git \  
libfreetype6-dev \  
libpng-dev \  
libzmq3-dev \  
pkg-config \  
python-dev \  
python-pip \  
software-properties-common \  
swig \  
unzip \  
zip \  
zlib1g-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN update-ca-certificates -f  
  
# Syntaxnet dependencies  
WORKDIR /root  
  
RUN pip install flask tqdm scikit-learn flask-swaggerui  
RUN pip install gunicorn  
COPY br /opt/tensorflow/syntaxnet/examples/dragnn/data/br  
COPY flask_server.py /root  
COPY test.py /root  
  
ENV PYTHONPATH /opt/tensorflow/syntaxnet/bazel-
bin/dragnn/tools/oss_notebook_launcher.runfiles:/opt/tensorflow/syntaxnet/bazel-
bin/dragnn/tools/oss_notebook_launcher.runfiles/protobuf/python:/opt/tensorflow/syntaxnet/bazel-
bin/dragnn/tools/oss_notebook_launcher.runfiles/protobuf:/opt/tensorflow/syntaxnet/bazel-
bin/dragnn/tools/oss_notebook_launcher.runfiles/six_archive:/opt/tensorflow/syntaxnet/bazel-
bin/dragnn/tools/oss_notebook_launcher.runfiles/org_tensorflow:/opt/tensorflow/syntaxnet/bazel-
bin/dragnn/tools/oss_notebook_launcher.runfiles/__main__:/usr/lib/python2.7:/usr/lib/python2.7/plat-x86_64-linux-
gnu:/usr/lib/python2.7/lib-tk:/usr/lib/python2.7/lib-
old:/usr/lib/python2.7/lib-dynload:/usr/local/lib/python2.7/dist-
packages:/usr/lib/python2.7/dist-
packages:/usr/lib/pymodules/python2.7:/usr/local/lib/python2.7/dist-
packages/IPython/extensions:/root/.ipython  
  
  
CMD gunicorn -w 4 flask_server:app  

