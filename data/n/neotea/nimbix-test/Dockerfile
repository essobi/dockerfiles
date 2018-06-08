FROM nimbix/base-ubuntu-nvidia  
  
USER root  
RUN apt-get update && \  
apt-get install --no-install-recommends -y --force-yes \  
git \  
graphviz \  
python-dev \  
python-flask \  
python-flaskext.wtf \  
python-gevent \  
python-h5py \  
python3-h5py \  
python-numpy \  
python-pil \  
python-pip \  
python3-pip \  
python-protobuf \  
python-scipy \  
python3-scipy \  
libpng12-0 \  
libpng12-dev \  
libfreetype6 \  
libjpeg-dev \  
libjpeg8 \  
libfreetype6-dev \  
build-essential \  
cmake \  
git \  
gfortran \  
libatlas-base-dev \  
libboost-all-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
libhdf5-serial-dev \  
libleveldb-dev \  
liblmdb-dev \  
libopencv-dev \  
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler \  
python-all-dev \  
python-dev \  
python-h5py \  
python3-h5py \  
python-matplotlib \  
python-numpy \  
python-opencv \  
python-pil \  
python-pip \  
python3-pip \  
python-protobuf \  
python-scipy \  
python3-scipy \  
  
python-skimage \  
python-sklearn \  
&& apt-get build-dep -y --force-yes python-matplotlib \  
&& apt-get clean  
  
# Update pip  
RUN sudo pip install pip --upgrade  
RUN sudo pip3 install pip --upgrade  
  
#WORKDIR /usr/share  
#RUN git clone https://github.com/nimbix/DIGITS.git digits  
#ENV DIGITS_ROOT=/usr/share/digits  
#WORKDIR ${DIGITS_ROOT}  
#RUN git checkout digits-5.0-https  
#RUN sudo pip install --upgrade -r $DIGITS_ROOT/requirements.txt  
#RUN sudo pip install -e $DIGITS_ROOT  
# Install AETROS  
VOLUME /tmp  
WORKDIR /tmp  
USER nimbix  
RUN sudo pip3 install aetros  
RUN sudo pip install aetros  
  
# Install Tensorflow for python  
RUN sudo pip3 install pip --upgrade && sudo pip3 install tensorflow-gpu  
RUN sudo pip install pip --upgrade && sudo pip install tensorflow-gpu  
RUN sudo pip install scipy --upgrade  
# Install Caffe  
VOLUME /tmp  
WORKDIR /tmp  
USER nimbix  
RUN sudo apt-get install -y devscripts \  
dh-make \  
build-essential && sudo apt-get clean && \  
git clone https://github.com/NVIDIA/nccl.git && \  
cd /tmp/nccl && \  
make -j4 && \  
make debian && \  
make deb && \  
sudo dpkg -i build/deb/*.deb && cd /tmp && rm -rf /tmp/nccl  
  
# example location - can be customized  
USER root  
ENV CAFFE_ROOT=/usr/local/caffe-nv  
RUN git clone -b caffe-0.15 https://github.com/NVIDIA/caffe.git $CAFFE_ROOT &&
\  
pip install -r $CAFFE_ROOT/python/requirements.txt  
WORKDIR $CAFFE_ROOT  
RUN mkdir build && cd ${CAFFE_ROOT}/build && cmake -DUSE_NCCL=ON
-DUSE_CUDNN=ON .. && make -j4 && make install  
  
# RUN mkdir -p /db  
#RUN python /usr/share/digits/digits/download_data mnist /db/mnist  
# RUN python /usr/share/digits/digits/download_data cifar10 /db/cifar10  
#RUN python /usr/share/digits/digits/download_data cifar100 /db/cifar100  
#RUN chown -R nimbix:nimbix /db  
#RUN chown -R nimbix:nimbix /usr/share/digits  
#RUN apt-get install -y --force-yes nginx && apt-get clean  
# Add our custom configuration  
#ADD ./conf/nginx.conf /etc/nginx/nginx.conf  
#ADD ./conf/digits.site /etc/nginx/sites-available/digits.site  
#RUN ln -sf /etc/nginx/sites-available/digits.site /etc/nginx/sites-
enabled/digits.site  
# Add the JARVICE app-specific files  
#ADD ./NAE/url.txt /etc/NAE/url.txt  
#ADD ./NAE/help.html /etc/NAE/help.html  
#ADD ./NAE/AppDef.json /etc/NAE/AppDef.json  
#ADD ./scripts /usr/local/scripts  
#ADD ./conf/digits.cfg /usr/share/digits/digits/digits.cfg  
# Keep the digits logs in the standard place...append this to the output  
#RUN mkdir -p /var/log/digits && touch /var/log/digits/digits.log && chown -R
nimbix:nimbix /var/log/digits && chown -R nimbix:nimbix /usr/local/scripts  
#RUN mkdir -p /usr/share/digits/digits  
#RUN ln -sf /data/DIGITS/jobs /usr/share/digits/digits/jobs  
#USER nimbix  
#CMD ["/usr/local/scripts/start.sh"]  

