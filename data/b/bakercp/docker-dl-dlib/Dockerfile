FROM floydhub/dl-docker:cpu  
MAINTAINER Christopher Baker <info@christopherbaker.net>  
  
#ENV MAKEFLAGS="-j$(nproc) -s"  
ARG DLIB_VERSION=19.3  
# Make sure PIP is up-to-date.  
#RUN pip install --upgrade pip  
RUN pip install opencv-python  
  
# Install dependencies not in dl-docker.  
RUN apt-get update && apt-get install -y \  
graphicsmagick \  
libatlas-dev \  
libgraphicsmagick1-dev \  
libgtk2.0-dev \  
python-protobuf \  
zip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install additional torch packages.  
RUN luarocks install dpnn && \  
luarocks install image && \  
luarocks install optim && \  
luarocks install csvigo && \  
luarocks install torchx && \  
luarocks install tds  
  
# Install dlib.  
RUN cd /root && \  
mkdir -p dlib-tmp && \  
cd dlib-tmp && \  
curl -L \  
https://github.com/davisking/dlib/archive/v${DLIB_VERSION}.tar.gz \  
-o dlib.tar.bz2 && \  
tar xf dlib.tar.bz2 && \  
cd dlib-${DLIB_VERSION}/python_examples && \  
mkdir build && \  
cd build && \  
cmake ../../tools/python && \  
cmake --build . --config Release && \  
cp dlib.so /usr/local/lib/python2.7/dist-packages && \  
rm -rf /root/dlib-tmp  
  
# Install openface.  
RUN git clone \--depth 1 https://github.com/cmusatyalab/openface.git
/root/openface --recursive  
  
RUN cd /root/openface && \  
./models/get-models.sh && \  
pip2 install -r requirements.txt && \  
python2 setup.py install && \  
pip2 install -r demos/web/requirements.txt && \  
pip2 install -r training/requirements.txt  
  
# Install additional utilities  
RUN pip install imagehash  
RUN pip install instaLooter  
  
# Set up working directory and defaults.  
WORKDIR "/root"  
CMD ["/bin/bash"]  

